question = ("\nWhy do you like programming?")
question += ("\nEnter 'quit' to stop.")

filename = 'programming_poll.txt'

active = True
while active:
    answer = input(question)
    if answer == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(answer + "\n")

    #with open('programming_poll.txt') as file_object:
        #contents = file_object.read()
        #print(contents)
