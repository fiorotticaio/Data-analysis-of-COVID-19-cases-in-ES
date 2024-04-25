import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_covid_evolution(data, city):
    # Filter the data for the specific city
    city_data = data[data['Municipio'] == city]
    
    # Group the data by date and count the number of cases and deaths for each date
    grouped_data = city_data.groupby('DataNotificacao').agg({'DataNotificacao': 'count', 'DataObito': 'count'}).reset_index()
    grouped_data.columns = ['DataNotificacao', 'Cases', 'Deaths']
    
    # Plot the line graph
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=grouped_data, x='DataNotificacao', y='Cases', label='Cases')
    sns.lineplot(data=grouped_data, x='DataNotificacao', y='Deaths', label='Deaths')
    plt.title(f'COVID-19 Cases and Deaths Evolution in {city}')
    plt.xlabel('Date')
    plt.ylabel('Number of Cases/Deaths')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.show()

# Example usage
if __name__ == "__main__":
    # Load the data from CSV into a DataFrame
    filename = '../MICRODADOS.csv'
    data = pd.read_csv(filename, delimiter=';', encoding='latin1', dtype={'DataColetaSorologia': str, 'DataColetaSorologiaIGG': str}, nrows=10000)
    
    # Specify the city of interest
    city = 'VITÓRIA'
    
    # Plot the graph of COVID-19 cases and deaths evolution for the specified city
    plot_covid_evolution(data, city)