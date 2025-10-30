def create_car(manufacturer, model, **options):
    car = {'manufacturer': manufacturer, 'model': model}
    for key, value in options.items():
        car[key] = value
    return car

car = create_car ('Dodge', 'Challenger', color='red', tow_package=True)
print(car)