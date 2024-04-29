import pandas as pd
from datetime import datetime


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


if __name__ == "__name__":
    # Load data from CSV file into a Pandas DataFrame
    filename = '../MICRODADOS.csv'
    data = pd.read_csv(filename, delimiter=';', encoding='latin1', nrows=300000)

    # Prompt the user for start_date and end_date
    N = int(input("Enter with the number of cities in the rank: "))
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")

    # Ensure start_date is earlier than end_date
    if start_date >= end_date:
        print("Error: Start date must be earlier than end date.")
    else:
        # Get the N cities with the highest number of cases between start_date and end_date
        cities_highest_cases = get_cities_with_highest_cases_between_dates(data, N, start_date, end_date)
        print(f"Top {N} cities with the highest number of COVID-19 cases between {start_date} and {end_date}:")
        for city in cities_highest_cases:
            print(city)