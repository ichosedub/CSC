favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

people_list = [  'jen', 'sarah','eward', 'foster']
for person in people_list:
    if person in favorite_languages:
        print(f"Thanks for participating, {person.title()}")
    else:
        print(f"{person.title()}, awaiting your response")