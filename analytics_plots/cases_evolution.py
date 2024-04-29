import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_covid_evolution(data, city):
    # Filter data for the specified city
    city_data = data[data['Municipio'] == city]

    # Count the number of notifications and deaths per day
    cases_per_day = city_data['DataNotificacao'].value_counts().sort_index()
    deaths_per_day = city_data['DataObito'].dropna().value_counts().sort_index()

    # Calculate the cumulative sum of cases and deaths
    cumulative_cases = cases_per_day.cumsum()
    cumulative_deaths = deaths_per_day.cumsum()

    # Plot the data with customized styles
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=cumulative_cases.index, y=cumulative_cases.values, label='Cases', color='skyblue', linewidth=2)
    sns.lineplot(x=cumulative_deaths.index, y=cumulative_deaths.values, label='Deaths', color='salmon', linewidth=2, linestyle='--')
    
    # Add title and labels
    plt.title(f'COVID-19 Cases and Deaths Evolution in {city}', fontsize=16)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Number of Cases/Deaths', fontsize=14)
    plt.xticks(rotation=45)
    
    # Add legend
    plt.legend(fontsize=12)

    # Add grid lines
    plt.grid(True, linestyle='--', alpha=0.7)

    # Show the plot
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Load the data from CSV into a DataFrame
    filename = '../MICRODADOS.csv'
    data = pd.read_csv(filename, delimiter=';', encoding='latin1', dtype={'DataColetaSorologia': str, 'DataColetaSorologiaIGG': str}, nrows=10000)
    
    # Specify the city of interest
    city = 'VITORIA'
    
    # Plot the graph of COVID-19 cases and deaths evolution for the specified city
    plot_covid_evolution(data, city)