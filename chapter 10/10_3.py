name = input("What is your name? ")
filename = 'guests.txt'

with open(filename, 'w') as file_object:
    file_object.write(name)

with open('guests.txt') as file_object:
    contents = file_object.read()
    print(contents)