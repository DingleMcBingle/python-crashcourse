def show_magicians(names):
    for name in names:
        message = name.title() + " is a magician."
        print(message)

def make_great(names):
    for i in range(0,len(magicians_copy)):
        names[i] += " The Great"
    return(names)


magicians = ['houdini','david copperfield']
magicians_copy = ['houdini','david copperfield']

make_great(magicians)
show_magicians(magicians)
show_magicians(magicians_copy)