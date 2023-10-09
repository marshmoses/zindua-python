class Country:
    def __init__(self, name, population, county):
        self.name = name
        self.population = population
        self.county = county
        self.counties = []

    def add_county(self, county_name):
    
        self.counties.append(county_name)

    def get_largest_county(self):


        
        largest_county = ""
        max_population = 0

        for county in self.counties:
            if county.population > max_population:
                max_population = county.population
                largest_county = county.name

        return largest_county

class county:
    def __init__(self, name, population):
        self.name = name
        self.population = population

# Create a country object
my_country = Country("Kenya", 55000000, "Nairobi")
Nairobi = county("Nairobi", 1000000)
Nyeri = county("Nyeri", 300000)
Mombasa = county("Mombasa", 500000)

my_country.add_county(Nairobi)
my_country.add_county(Nyeri)
my_country.add_county(Mombasa)
largest_county = my_country.get_largest_county()
print(f"The largest county in {my_country.name} is {largest_county}.")

