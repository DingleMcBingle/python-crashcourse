print("Give me two numbers and I will add them.")
print("Enter quit to quit.")

while True:
    first_number = input("First number: ")
    if first_number == 'quit':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("That's a letter, moron.")
    else:
        print(answer)