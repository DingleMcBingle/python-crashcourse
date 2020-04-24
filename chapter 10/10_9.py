filenames = ['dogs.txt','cats.txt']

for filename in filenames:
    print("File: " + filename)
    try:
        with open(filename) as file_object:
            contents = file_object.read()
            print(contents.title() + "\n")
    except FileNotFoundError:
        pass

