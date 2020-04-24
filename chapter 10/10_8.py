filenames = ['dogs.txt','cats.txt']

for filename in filenames:
    print("File:" + filename)
    try:
        with open(filename) as file_object:
            contents = file_object.read()
            print(contents + "\n")
    except FileNotFoundError:
        print("Error: File not found.\n")
