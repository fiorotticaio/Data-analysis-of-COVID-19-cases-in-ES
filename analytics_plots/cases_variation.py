import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_cases_variation(data, cities):
    # Filter the data to include only the desired cities
    data_cities = data[data['Municipio'].isin(cities)]
    
    # Group the data by date and municipality and count the number of cases
    cases_by_date = data_cities.groupby(['DataNotificacao', 'Municipio']).size().reset_index(name='Cases')
    
    # Plot the line graph with Seaborn style
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=cases_by_date, x='DataNotificacao', y='Cases', hue='Municipio', palette='husl', linewidth=2.5)

    # Add title and axis labels
    plt.title('Cases Variation Over Time for a Group of Cities', fontsize=16)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Number of Cases', fontsize=14)

    # Adjust the date format on the x-axis
    plt.xticks(rotation=45, ha='right')

    # Adjust the legend
    plt.legend(title='City', fontsize=12)

    # Add gridlines to the background of the plot
    plt.grid(True, linestyle='--', alpha=0.5)

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
    
    # Plot the graph of cases variation over time for the specified group of cities
    plot_cases_variation(data, cities)