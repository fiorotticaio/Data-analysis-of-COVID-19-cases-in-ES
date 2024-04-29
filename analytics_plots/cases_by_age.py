import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def extract_age(age_str):
    # Extract only the numerical value of age
    age_numeric = age_str.split(' ')[0]  # Split by space and get the first element
    return int(age_numeric)

def plot_cases_by_age(data, cities):
    # Filter the data to include only the desired cities
    data_cities = data[data['Municipio'].isin(cities)]
    
    # Convert age values to numeric by extracting the numeric part
    data_cities['Age'] = data_cities['IdadeNaDataNotificacao'].apply(extract_age)

    # Group the data by age and calculate the total number of cases for each age group
    cases_by_age = data_cities.groupby('Age').size().reset_index(name='Total Cases')

    # Plot the bar chart
    plt.figure(figsize=(12, 6))
    sns.barplot(data=cases_by_age, x='Age', y='Total Cases', palette='viridis')

    # Add labels and title
    plt.xlabel('Age')
    plt.ylabel('Number of Cases')
    plt.title('Number of COVID-19 Cases by Age for a Group of Cities')

    # Display the plot
    plt.xticks(rotation=70) 
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Load the data from CSV into a DataFrame
    filename = '../MICRODADOS.csv'
    data = pd.read_csv(filename, delimiter=';', encoding='latin1', nrows=10000)
    
    # Choose the desired cities
    cities = ['VITORIA', 'SERRA', 'CARIACICA']
    
    # Plot the graph of COVID-19 cases by age for the specified group of cities
    plot_cases_by_age(data, cities)