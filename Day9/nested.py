#nest an array within an object
travel_log = {
    "France": [
        "paris",
        "lille",
        "Dijion"
    ],
    "Germany": [
        "Berlin",
        "Hamburg",
        "Stuttgard"
    ]
}
#print only the first item in the first array
print(travel_log["France"][1])

#print only the France array
print(travel_log["France"])

#print the entire travel log
print(travel_log)

print("\n")

# Nesting dictionary within a dictionary
country_visted = {
    "Germany": {
        "cities_visited": [
            "Berlin",
            "Hamburg",
            "Stuttgard"
        ],
        "total_visits": 90
    },
}
# print the first list in the first object
print(country_visted["Germany"]["cities_visited"])

# print country visted
print(country_visted)

print("\n")

# Nested dictionary in list
countries = [
    {
        "name": "France",
        "cities": ["paris", "Lille", "Dijon"],
        "visited": False
    },
    {
        "name": "Germany",
        "cities": ["Berlin", "Hamburg", "Stuttgard"],
        "visited": False
    },
]


# write a function that adds a new entry to the countries array
def add_new_country(name, cities, visited):
    new_country = {"name": name, "cities": cities, "visited": visited}
    countries.append(new_country)


add_new_country("Guyana", ["George-town", "Herstelling", "Berbice"], True)
print(countries)
