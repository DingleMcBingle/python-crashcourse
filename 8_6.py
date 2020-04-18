def city_country(city, country):
    """Returns the name of a city and country"""
    name_location = city + ', ' + country
    return name_location.title()

place = city_country(city='Altoona',country='USA')
print(place)

place = city_country('Cologne','Germany')
print(place)

place = city_country('Venice','Italy')
print(place)