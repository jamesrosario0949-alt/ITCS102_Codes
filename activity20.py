from getpass import getpass

islogin = True

while islogin == True:
    username = input("Enter your username:   ")
    password = getpass("Enter your password:   ")

    if username == "James" and password == "James123":
        print("You are logged in")
        islogin = False
    else:
        print("Invalid username or password")
        