favorites = {'noah':['8','23'],'brayden':['7','77'],'dalton':['3','25'],'brendan':['20','2']}
for name, numbers in favorites.items():
    print(name.title() + "'s favorite numbers are:")
    for number in numbers:
        print(number)