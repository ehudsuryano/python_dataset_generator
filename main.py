from user_generator import UserGenerator as gen

def main():
    """preprocessing of files"""

    firstname_file = "first-names.txt"
    lastname_file = "last-names.txt"
    countries_cities_file ='worldcities.csv'
    generator = gen(firstname_file, lastname_file, countries_cities_file)

    try:
        num_sequences = int(input("Enter the number of personal data sets to generate: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    """Generate the specified number of personal data sets using the UserGenerator class generator.generate_personal_data() 
    method and save them to a CSV file overwriting the file also print the list."""
    filename = 'PersonalData.csv'
    try:
        existing_sequences = set()
        for _ in range(num_sequences):
            new_sequence = generator.generate_personal_data()
            print(new_sequence)
            existing_sequences.add(new_sequence)

        generator.save_sequence(filename, existing_sequences)
    except IOError:
        print(f"An error occurred while trying to save to {filename}.")
        return


if __name__ == "__main__":
    main()