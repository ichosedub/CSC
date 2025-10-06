cities = {
    'tokyo': {
        'country': 'japan',
        'population': 37_036_200,
        'fact': 'Known for having one of the most busiest streets, Shiubuya Crossing.'
    },
    'mexico city': {
        'country': 'mexico',
        'population': 21_000_000,
        'fact': 'Known for its rich history, vibrant culture, and world-class cuisine.'
    },
    'beijing': {
        'country': 'china',
        'population': 19_000_000,
        'fact': 'known for the great war of china.'
    }
}

for city, info in cities.items():
    print(f"\n{city.title()}:")
    print(f"  Country: {info['country'].title()}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}")