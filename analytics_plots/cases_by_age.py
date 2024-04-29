import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_cases_by_age(data, cities):
    # Filter the data to include only the desired cities
    data_cities = data[data['Municipio'].isin(cities)]

    # Plot the scatter plot
    sns.scatterplot(data=data_cities, x='IdadeNaDataNotificacao', y=data_cities.index)

    # Simplify the display of dates on the x-axis
    plt.xticks(rotation=70) 

    # Add labels and title
    plt.xlabel('Age')
    plt.ylabel('Number of Cases')
    plt.title('Scatterplot of Number of Cases by Age for a Group of Cities')

    # Display the plot
    plt.show()


if __name__ == "__main__":
    # Load the data from CSV into a DataFrame
    filename = '../MICRODADOS.csv'
    data = pd.read_csv(filename, delimiter=';', encoding='latin1', nrows=1000)
    
    # Choose the desired cities
    cities = ['VITORIA', 'SERRA', 'CARIACICA']
    
    # Plot the graph of COVID-19 cases and deaths evolution for the specified city
    plot_cases_by_age(data, cities)