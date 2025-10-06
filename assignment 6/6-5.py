rivers = {
    'Volga': 'Europe',
    'Yukon': 'Alaska',
    'Indus': 'South Asia'
}


for river, country in rivers.items():
    print(f"The {river} runs through {country}.")


print("\nRivers:")
for river in rivers.keys():
    print(river)


print("\nCountries:")
for country in rivers.values():
    print(country)