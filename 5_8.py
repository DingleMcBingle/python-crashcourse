usernames = ['admin','adam','ryan','amy','matthew']
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    if username != 'admin':
        print("Hello " + username + " thanks for logging on.")