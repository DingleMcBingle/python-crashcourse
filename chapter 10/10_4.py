question = ("\nWhat is your name?")
question += ("\nEnter 'quit' to stop.")

filename = 'guest_book.txt'

active = True
while active:
    name = input(question)
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(name + "\n")

    #with open('guests.txt') as file_object:
    #    contents = file_object.read()
    #    print(contents)