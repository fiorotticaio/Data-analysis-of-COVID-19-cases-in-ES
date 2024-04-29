import pandas as pd


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


if __name__ == "__name__":
    # Load data from CSV file into a Pandas DataFrame
    filename = '../MICRODADOS.csv'
    data = pd.read_csv(filename, delimiter=';', encoding='latin1', nrows=300000)

    # Prompt the user for municipality name or leave it blank for all municipalities
    municipality = input("Enter the municipality name or leave blank for all municipalities: ")

    # Calculate percentage metrics
    percentage_metrics = calculate_percentage_metrics(data, municipality)
    print(percentage_metrics)