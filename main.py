import pandas as pd
from datetime import datetime


def get_cities_with_cases_above_threshold(data, threshold):
    # Filter the data for cities with more than N cases
    filtered_data = data[data.groupby('Municipio')['DataNotificacao'].transform('size') > threshold]
    # This last line of groups the data by the name of the municipality ('Municipio') and then calculates the size of
    # each group, that is, it counts how many occurrences of notification dates ('DataNotificacao') there are for each 
    # municipality. This returns a Series with the number of occurrences for each row in the original DataFrame.
    
    cities = filtered_data['Municipio'].unique() # Get unique values of the 'Municipio' column
    cities.sort() # Sort cities alphabetically
    
    return cities


def count_cases_between_dates(data, start_date, end_date):
    # Convert start_date and end_date to datetime objects
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # Convert 'DataNotificacao' column to datetime objects
    data['DataNotificacao'] = pd.to_datetime(data['DataNotificacao'])
    
    # Filter data for cases between start_date and end_date
    filtered_data = data[(data['DataNotificacao'] >= start_date) & (data['DataNotificacao'] <= end_date)] 
    
    # Count the number of rows in filtered_data, which represents the number of cases
    num_cases = len(filtered_data)
    
    return num_cases


def get_cities_with_highest_cases_between_dates(data, N, start_date, end_date):
    # Convert start_date and end_date to datetime objects
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # Convert 'DataNotificacao' column to datetime objects
    data['DataNotificacao'] = pd.to_datetime(data['DataNotificacao'])
    
    # Filter data for cases between start_date and end_date
    filtered_data = data[(data['DataNotificacao'] >= start_date) & (data['DataNotificacao'] <= end_date)] 
    
    # Group data by city and count the number of cases
    city_cases = filtered_data.groupby('Municipio').size()
    
    # Sort cities by number of cases in descending order
    city_cases = city_cases.sort_values(ascending=False)
    
    # Get the N cities with the highest number of cases
    cities = city_cases.head(N).index
    
    return cities


def calculate_percentage_metrics(data, municipality=None):
    # Filter data by municipality if specified
    if municipality:
        filtered_data = data[data['Municipio'] == municipality]
    else:
        filtered_data = data

    # Count total number of confirmed cases
    total_cases = len(filtered_data)

    # Count number of cases where individuals were hospitalized
    hospitalized_cases = filtered_data['FicouInternado'].eq('Sim').sum()

    # Count number of deaths
    deaths = filtered_data['DataObito'].notnull().sum() # Count number of rows where 'DataObito' is not null        

    # Count number of hospitalized individuals who died
    hospitalized_deaths = filtered_data[(filtered_data['FicouInternado'] == 'Sim') &
                                        (filtered_data['DataObito'].notnull())].shape[0]

    # Calculate percentages
    percent_hospitalized = (hospitalized_cases / total_cases) * 100
    percent_deaths = (deaths / total_cases) * 100
    percent_hospitalized_deaths = (hospitalized_deaths / hospitalized_cases) * 100 if hospitalized_cases > 0 else 0

    return {
        'Percent Hospitalized': percent_hospitalized,
        'Percent Deaths': percent_deaths,
        'Percent Hospitalized Deaths': percent_hospitalized_deaths
    }


# Função para converter os valores da idade para o formato numérico
def extract_age(value):
    # Verifica se o valor é uma string
    if isinstance(value, str):
        # Extrai os números da string
        numeric_part = ''.join(filter(str.isdigit, value))
        # Converte a parte numérica para inteiro
        return int(numeric_part)
    else:
        # Se não for uma string, retorna o valor original
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
    print(total_deaths)
    deaths_without_comorbidity = len(no_comorbidity_death_data)
    print(deaths_without_comorbidity)
    percent_deaths_without_comorbidity = (deaths_without_comorbidity / total_deaths) * 100 if total_deaths > 0 else 0

    return {
        'Mean Age of Deceased': mean_age,
        'Standard Deviation of Age of Deceased': std_age,
        'Percent Deaths without Comorbidities': percent_deaths_without_comorbidity
    }


if __name__ == "__main__":
    # Load data from CSV file into a Pandas DataFrame
    filename = 'MICRODADOS.csv'
    data = pd.read_csv(filename, delimiter=';', encoding='latin1', nrows=300000)

    # =============== 1 ==============
    # Prompt the user for the value of N
    # N = int(input("Enter the threshold value (N): "))
    
    # # Get the list of cities with more than N cases of COVID-19
    # cities_above_threshold = get_cities_with_cases_above_threshold(data, N)
    
    # # Print cities in alphabetical order
    # print(f"Cities with more than {N} COVID-19 cases:")
    # for city in cities_above_threshold:
    #     print(city)


    # # =============== 2 ==============
    # # Prompt the user for start_date and end_date
    # start_date = input("Enter the start date (YYYY-MM-DD): ")
    # end_date = input("Enter the end date (YYYY-MM-DD): ")

    # # Ensure start_date is earlier than end_date
    # if start_date >= end_date:
    #     print("Error: Start date must be earlier than end date.")
    # else:
    #     # Count the number of cases between start_date and end_date
    #     num_cases = count_cases_between_dates(data, start_date, end_date)
    #     print(f"Number of COVID-19 cases between {start_date} and {end_date}: {num_cases}")


    # =============== 3 ==============
    # Prompt the user for start_date and end_date
    # N = int(input("Enter with the number of cities in the rank: "))
    # start_date = input("Enter the start date (YYYY-MM-DD): ")
    # end_date = input("Enter the end date (YYYY-MM-DD): ")

    # # Ensure start_date is earlier than end_date
    # if start_date >= end_date:
    #     print("Error: Start date must be earlier than end date.")
    # else:
    #     # Get the N cities with the highest number of cases between start_date and end_date
    #     cities_highest_cases = get_cities_with_highest_cases_between_dates(data, N, start_date, end_date)
    #     print(f"Top {N} cities with the highest number of COVID-19 cases between {start_date} and {end_date}:")
    #     for city in cities_highest_cases:
    #         print(city)


    # =============== 4 ==============
    # Prompt the user for municipality name or leave it blank for all municipalities
    # municipality = input("Enter the municipality name or leave blank for all municipalities: ")

    # # Calculate percentage metrics
    # percentage_metrics = calculate_percentage_metrics(data, municipality)
    # print(percentage_metrics)


    # =============== 5 ==============
    # Prompt the user for start_date and end_date
    start_date = input("Enter the start date (format YYYY-MM-DD): ")
    end_date = input("Enter the end date (format YYYY-MM-DD): ")

    # Calculate death statistics
    death_statistics = calculate_death_statistics(data, start_date, end_date)
    print(death_statistics)