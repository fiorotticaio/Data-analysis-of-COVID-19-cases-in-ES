import pandas as pd

def get_cities_with_cases_above_threshold(data, threshold):
    # Filter the data for cities with more than N cases
    filtered_data = data[data.groupby('Municipio')['DataNotificacao'].transform('size') > threshold]
    # This last line of groups the data by the name of the municipality ('Municipio') and then calculates the size of
    # each group, that is, it counts how many occurrences of notification dates ('DataNotificacao') there are for each 
    # municipality. This returns a Series with the number of occurrences for each row in the original DataFrame.
    
    cities = filtered_data['Municipio'].unique() # Get unique values of the 'Municipio' column
    cities.sort() # Sort cities alphabetically
    
    return cities


if __name__ == "__main__":
    # Load data from CSV file into a Pandas DataFrame
    filename = '../MICRODADOS.csv'
    data = pd.read_csv(filename, delimiter=';', encoding='latin1', nrows=300000)

    # Prompt the user for the value of N
    N = int(input("Enter the threshold value (N): "))
    
    # Get the list of cities with more than N cases of COVID-19
    cities_above_threshold = get_cities_with_cases_above_threshold(data, N)
    
    # Print cities in alphabetical order
    print(f"Cities with more than {N} COVID-19 cases:")
    for city in cities_above_threshold:
        print(city)