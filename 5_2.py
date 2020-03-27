topping = 'mushroom'
topping == 'mushroom'

password = 'bingus'
if password != 'dingus':
    print("try again")

car = 'Porsche'
car == 'porsche'
car.lower() == 'porsche'

age = 19
age > 18
age < 18
age >= 19
age > 19

age_0 = 21
age_1 = 24
age_0 >= 21 and age_1 >= 21
age_0 > 21 and age_1 >= 21
age_0 < 21 or age_1 > 21
age_0 < 21 or age_1 < 21

expensive_cars = ['mercedes', 'porsche', 'bmw','bugatti']
'bugatti' in expensive_cars
'volkswagen' in expensive_cars
car = 'volkswagen'
if car not in expensive_cars:
    print("The brand " + car.title() + " is not very expensive.")
