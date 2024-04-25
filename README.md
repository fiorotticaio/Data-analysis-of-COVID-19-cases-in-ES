# COVID-19 Data Analysis

This repository contains a Python script for analyzing COVID-19 case data. The script reads data from a CSV file and provides five main functionalities:

1. **List states with more than N cases:** The script prompts the user to enter a threshold value (N). It then lists all the cities that have reported more than N cases of COVID-19, in alphabetical order.

2. **Count cases between dates:** The script prompts the user to enter a start date and an end date. It then counts the number of COVID-19 cases reported between these two dates.

3. **List cities with the highest number of cases between dates:** The script prompts the user to enter a number (N), a start date, and an end date. It then lists the top N cities with the highest number of COVID-19 cases reported between these two dates.

4. **Calculate percentage metrics:** The script prompts the user to enter a municipality name or leave it blank for all municipalities. It then calculates and displays various percentage metrics related to COVID-19 cases for the specified municipality or all municipalities.

5. **Calculate death statistics:** The script calculates and displays various statistics related to COVID-19 deaths.

### Prerequisites

- Python 3.x
- pandas library
- datetime library

### Installing

1. Clone the repository to your local machine.
2. Donwload the COVID-19 case data from the following link: https://coronavirus.es.gov.br/painel-covid-19-es
3. Install the required Python packages using pip:

```bash
pip install pandas
pip install datetime
```
3. Run the script using the following command:

```bash
python main.py
```