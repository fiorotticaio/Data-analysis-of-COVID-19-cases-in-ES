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


if __name__ == "__main__":
    # Load data from CSV file into a Pandas DataFrame
    filename = 'MICRODADOS.csv'
    data = pd.read_csv(filename, delimiter=';', encoding='latin1', nrows=300000)


    # Prompt the user for the value of N
    N = int(input("Enter the threshold value (N): "))
    
    # Get the list of cities with more than N cases of COVID-19
    cities_above_threshold = get_cities_with_cases_above_threshold(data, N)
    
    # Print cities in alphabetical order
    print(f"Cities with more than {N} COVID-19 cases:")
    for city in cities_above_threshold:
        print(city)


    # Prompt the user for start_date and end_date
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")

    # Ensure start_date is earlier than end_date
    if start_date >= end_date:
        print("Error: Start date must be earlier than end date.")
    else:
        # Count the number of cases between start_date and end_date
        num_cases = count_cases_between_dates(data, start_date, end_date)
        print(f"Number of COVID-19 cases between {start_date} and {end_date}: {num_cases}")