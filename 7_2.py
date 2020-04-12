group = input("How many people are in your dinner group? ")
group = int(group)

if group >= 8:
    print("You are going to have to wait for an availiable table.")
else:
    print("Okay, your table is ready.")