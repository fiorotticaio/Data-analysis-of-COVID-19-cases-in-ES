import pandas as pd
from datetime import datetime


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


if __name__ == "__name__":
    # Load data from CSV file into a Pandas DataFrame
    filename = '../MICRODADOS.csv'
    data = pd.read_csv(filename, delimiter=';', encoding='latin1', nrows=300000)
    
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