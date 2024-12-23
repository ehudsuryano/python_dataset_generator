import random
import pandas as pd
import csv
import os
from personal_data import PersonalData
from collections import Counter

class UserGenerator:
    def __init__(self, first_names_file, last_names_file, countries_cities_file):
        self.first_names = self.parse_files(first_names_file)
        self.last_names = self.parse_files(last_names_file)
        self.countries_cities = self.parse_files(countries_cities_file,0)

    def parse_files(self,filename,header_value = None):
        try:
            data = pd.read_csv(filename,header= header_value)
            return data
        except (pd.errors.ParserError, FileNotFoundError, pd.errors.EmptyDataError,IOError) as e:
            print(f"An error occurred {e} while trying to read {filename}. using default values")
            return None

    def calculate_check_digit(self, id_number):
        """Calculate the check digit for an Israeli ID number."""
        total = 0
        for i, digit in enumerate(id_number, 1):
            num = int(digit)
            # Double every second digit (starting from index 0)
            if i % 2 == 1:
                num *= 2
                # If the result is greater than 9, sum its digits
                if num > 9:
                    num = num // 10 + num % 10
            total += num
        # The check digit is what makes the total a multiple of 10
        check_digit = (10 - (total % 10)) % 10
        return check_digit

    def generate_id_number(self):
        """Generate a valid Israeli ID number."""
        # Generate the first 8 random digits
        id_number = ''.join(random.choices('0123456789', k=8))
        # Calculate the 9th digit (check digit)
        check_digit = self.calculate_check_digit(id_number)
        # Return the full ID number with the check digit
        return id_number + str(check_digit)

    def generate_first_name(self):
        if self.first_names is None:
            return random.choice(['John', 'Jane', 'Alice', 'Bob', 'Eve', 'Charlie', 'David', 'Grace', 'Heidi', 'Ivy'])
        return random.choice(self.first_names[0].to_list())

    def generate_last_name(self):
        if self.last_names is None:
            return random.choice(['Doe', 'Smith', 'Johnson', 'Brown', 'Lee', 'Kim', 'Singh', 'Garcia', 'Martinez', 'Lopez'])
        return random.choice(self.last_names[0].to_list())

    def generate_email(self,first_name, last_name):
        domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'icloud.com']
        return f'{first_name.lower()}.{last_name.lower()}@{random.choice(domains)}'

    def generate_country(self):
        if self.countries_cities is None:
            return random.choice(['USA', 'UK', 'Canada', 'Australia', 'Germany', 'France', 'Italy', 'Japan', 'China', 'India'])
        return random.choice(self.countries_cities['country'].to_list())

    def generate_city(self):
        if self.countries_cities is None:
            return random.choice(['New York', 'London', 'Paris', 'Tokyo', 'Sydney', 'Berlin', 'Rome', 'Beijing', 'Mumbai', 'Toronto'])
        return random.choice(self.countries_cities['city'].to_list())

    def generate_personal_data(self):
        first_name = self.generate_first_name()
        last_name = self.generate_last_name()
        email = self.generate_email(first_name, last_name)
        country = self.generate_country()
        city = self.generate_city()
        id_number = self.generate_id_number()

        return PersonalData(first_name, last_name, email, country, city, id_number)

    def save_sequence(self, filename, new_sequence):
        # Create a DataFrame for the new sequence
        new_row = pd.DataFrame([obj.__dict__ for obj in new_sequence]) #new_row = pd.DataFrame(new_sequence)

        # Append to the CSV file
        new_row.to_csv(filename, header=False, index=False,quoting=csv.QUOTE_NONE)

