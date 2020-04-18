def show_magicians(names):
    for name in names:
        message = name.title() + " is a magician."
        print(message)

magicians = ['houdini','david copperfield']
show_magicians(magicians)