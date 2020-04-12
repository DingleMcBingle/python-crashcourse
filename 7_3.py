number = input("Give me a number and I will tell you if it is a multiple of ten. ")
number = int(number)

if number % 10 == 0:
    print("\nThat number is a multiple of ten.")
else:
    print("\nThat number is not a multiple of ten.")