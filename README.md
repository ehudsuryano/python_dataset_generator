# User Generator Program

This project generates random personal data sets, including names, email addresses, countries, cities, and valid Israeli ID numbers. It saves the generated data to a CSV file for further use.

## Features

- Generates random first and last names.
- Creates email addresses based on generated names.
- Selects random countries and cities from a dataset.
- Generates valid Israeli ID numbers with a check digit.
- Saves generated data to a CSV file.
- Displays the generated data in the console.

## Project Structure

- `personal_data.py`: Defines the `PersonalData` class, which represents a person's details.
- `user_generator.py`: Implements the `UserGenerator` class, providing methods to generate and save random personal data.
- `main.py`: Entry point for the application. Handles user input, data generation, and file saving.

## Requirements

- Python 3.8 or higher
- Pandas
- CSV module

## Usage

1. Ensure the following files are present:
   - `first-names.txt`: A file containing a list of first names.
   - `last-names.txt`: A file containing a list of last names.
   - `worldcities.csv`: A CSV file containing country and city information.

2. Install required Python packages:
   ```bash
   pip install pandas