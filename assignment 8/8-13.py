def build_profile(first_name, last_name, **personl_database):
    personl_database['first_name'] = first_name
    personl_database['surname'] = last_name
    return personl_database

personl_profile = build_profile('Adrien', 'Talbot',
    city ='Philadelphia',
    major ='Gaming sim')

print(personl_profile)