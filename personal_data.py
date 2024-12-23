class PersonalData:
    def __init__(self, first_name, last_name, email, country, city, id_number):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.city = city
        self.id_number = id_number

    def __str__(self):
        return f"{self.email}, {self.first_name}, {self.last_name}, {self.city}, {self.country}, {self.id_number}"