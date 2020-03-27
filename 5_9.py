usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        if username != 'admin':
            print("Hello " + username + ", thanks for logging on.")
else:
    print("We need to find some users!")