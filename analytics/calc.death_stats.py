import pandas as pd


# Function to convert age values to numeric format
def extract_age(value):
    # Checks if the value is a string
    if isinstance(value, str):
        # Extract numbers from string
        numeric_part = ''.join(filter(str.isdigit, value))
        # Converts the numeric part to integer
        return int(numeric_part)
    else:
        # If not a string, return the original value
        return value

def calculate_death_statistics(data, start_date, end_date):
    # Filter data between start_date and end_date
    filtered_data = data[(data['DataNotificacao'] >= start_date) & (data['DataNotificacao'] <= end_date)]

    # Filter data for deaths
    death_data = filtered_data[filtered_data['DataObito'].notnull()].copy()

    # Aplica a função de extração de idade à coluna 'IdadeNaDataNotificacao'
    death_data['IdadeNaDataNotificacao'] = death_data['IdadeNaDataNotificacao'].apply(extract_age)

    # Calculate mean and standard deviation of age for deceased individuals
    mean_age = death_data['IdadeNaDataNotificacao'].mean()
    std_age = death_data['IdadeNaDataNotificacao'].std()

    # Filter data for deceased individuals without comorbidities
    no_comorbidity_death_data = death_data[death_data.iloc[:, 25:34].eq('Não').all(axis=1)]

    # Calculate percentage of deceased individuals without comorbidities
    total_deaths = len(death_data)
    deaths_without_comorbidity = len(no_comorbidity_death_data)
    percent_deaths_without_comorbidity = (deaths_without_comorbidity / total_deaths) * 100 if total_deaths > 0 else 0

    return {
        'Mean Age of Deceased': mean_age,
        'Standard Deviation of Age of Deceased': std_age,
        'Percent Deaths without Comorbidities': percent_deaths_without_comorbidity
    }


if __name__ == "__name__":
    # Load data from CSV file into a Pandas DataFrame
    filename = '../MICRODADOS.csv'
    data = pd.read_csv(filename, delimiter=';', encoding='latin1', nrows=300000)

    # Prompt the user for start_date and end_date
    start_date = input("Enter the start date (format YYYY-MM-DD): ")
    end_date = input("Enter the end date (format YYYY-MM-DD): ")

    # Calculate death statistics
    death_statistics = calculate_death_statistics(data, start_date, end_date)
    print(death_statistics)