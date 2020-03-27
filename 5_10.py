current_users = ['admin','adam','ryan','amy','matthew']
new_users = ['Admin','bingus','user1','user2','user3']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("That username is taken.")
    else:
        print("That username is availiable.")