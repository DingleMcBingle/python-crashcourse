favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
names = ['john','phil','joe']
for name in names:
    if name in favorite_languages.keys():
        print("Thanks for taking the poll, " + name.title() + ".")
    else:
        print("Hey " + name.title() + ", you should take my poll!")