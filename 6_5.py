rivers = {'nile':'egypt','mississippi':'mississippi','colorado':'colorado'}
for river, location in rivers.items():
    print("The " + river.title() + " river is in " + location.title() + ".")

for river in rivers.keys():
    print(river.title())

for location in rivers.values():
    print(location.title())
