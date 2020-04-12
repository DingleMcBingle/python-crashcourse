question = ("\nWhat pizza topping do you want?")
question += ("\nEnter 'quit' to stop the program. ")

active = True
while active:
    message = input(question)
    if message == 'quit':
        active = False
    else:
        print("Okay, adding " + message + " to the pizza.")