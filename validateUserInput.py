#validate user input exercise
# 1. user is no more than 12 characters
# 2.User must not contain space
#3. User must not contain digits


username = input ("Enter a username :")

if len(username)>12:
    print("Username must be between 12 characters")
elif not username.find(" ")== -1:
    print("username cant containe spaces")
elif not username.isalpha():
    print("username cant contain numbers")
else:
    print(f"Welcome {username}")