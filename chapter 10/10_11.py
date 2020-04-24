#This covers both 10-11 and 10-12.

import json

filename = 'fav_number.json'

try:
    with open(filename) as f_object:
        fav_number = json.load(f_object)
except FileNotFoundError:
    fav_number = input("What is your favorite number? ")
    with open(filename, 'w') as f_object:
        json.dump(fav_number, f_object)
        print("Thanks, I'll remember that!")
else:
    print("I know your favorite number! it's " + str(fav_number) + ".")