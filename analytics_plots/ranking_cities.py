import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_cases_ranking(data, cities):
    # Filter the data to include only the desired cities
    data_cities = data[data['Municipio'].isin(cities)]

    # Calculate the total number of cases for each city
    total_cases_by_city = data_cities.groupby('Municipio').size().reset_index(name='Total Cases')

    # Sort the cities by the total number of cases
    total_cases_by_city = total_cases_by_city.sort_values(by='Total Cases', ascending=False)

    # Plot the horizontal bar chart
    plt.figure(figsize=(10, 6))
    sns.set_style("whitegrid")
    sns.barplot(data=total_cases_by_city, x='Total Cases', y='Municipio', hue='Municipio')

    # Add title and axis labels
    plt.title('COVID-19 Cases Ranking for a Group of Cities', fontsize=16)
    plt.xlabel('Total Cases', fontsize=14)
    plt.ylabel('City', fontsize=14)

    # Add annotations with the number of cases on each bar
    for index, value in enumerate(total_cases_by_city['Total Cases']):
        plt.text(value, index, str(value), fontsize=12, ha='left', va='center')

    # Remove unnecessary borders
    sns.despine()

    # Display the plot
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Load the data from the CSV into a DataFrame
    filename = '../MICRODADOS.csv'
    data = pd.read_csv(filename, delimiter=';', encoding='latin1', nrows=10000)
    
    # Choose the desired cities
    cities = ['VITORIA', 'SERRA', 'CARIACICA']
    
    # Plot the graph of cases ranking for the specified group of cities
    plot_cases_ranking(data, cities)