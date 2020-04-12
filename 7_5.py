prompt = input("How old are you? ")

active = True
while active:
    age = prompt
    age = int(prompt)

    if age <= 3:
        print("Your ticket is free.")
        active = False
    if age >= 3 and age < 12:
        print("Your ticket costs $10.")
        active = False
    if age > 12:
        print("Your ticket costs $15.")
        active = False