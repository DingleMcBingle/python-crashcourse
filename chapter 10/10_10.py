filename = 'huckleberry_finn.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("FIle " + filename + " not found.")
else:
    #counts what word appears how many times in a file
    words = contents.split()
    num_word = contents.lower().count('the')
    print('The book Huckleberry Finn says "The" ' + str(num_word) + ' times.')
    print("(I was going to use a different word but didn't want to upload it to Git for anyone to see. But for the record, 214 times!")