responses = {}

polling_active = True
while polling_active:
    name = input("What is your name? ")
    response = input("If you could visit one place in the world, where would it be? ")

    responses[name] = response
    repeat = input("Would you like to let someone else respond? (yes/no)" )
    if repeat == 'no':
        polling_active = False

print("\n\t~~~POLL RESULTS~~~")
for name, response in responses.items():
    print(name + " Wants to go to " + response + ".")