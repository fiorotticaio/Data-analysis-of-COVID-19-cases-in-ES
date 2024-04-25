import pandas as pd
from analytics import *



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