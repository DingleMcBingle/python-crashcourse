def build_car(make,model,**other_info):
    """Builds a car make and model, plus whatever other info you want to give."""
    car = {}
    car['manufacturer'] = make
    car['model'] = model
    for key, value in other_info.items():
        car[key] = value
    return car