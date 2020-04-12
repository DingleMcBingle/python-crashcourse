parrot = "\nTell me something, and I'll say it back to you."
parrot += "\n Enter 'quit' to end the program."

active = True
while active:
    message = input(parrot)
    
    if message == 'quit':
        active = False
    else:
        print(message)


question = ("\nWhat pizza topping do you want?")
question += ("\nEnter 'quit' to stop the program. ")

active = True
while active:
    message = input(question)
    if message == 'quit':
        break
    else:
        print("Okay, adding " + message + " to the pizza.")