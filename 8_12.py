def make_sandwich(*ingredients):
    print("Making a sandwich with the ingredients: ")
    for ingredient in ingredients:
        print("-" + ingredient)

make_sandwich('ham')
make_sandwich('ham','cheese')
make_sandwich('ham','cheese','mustard')