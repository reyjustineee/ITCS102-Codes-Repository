from getpass import getpass

u = "ethan"
p = "reyjustine"

isLogin = False

while isLogin == False:

    username = input("Enter your username: ")

    password = getpass("Enter your password: ")

    if username == u and password == p:
        print("Login Successful")
        isLogin = True
    else:
        print("Login Denied")
        isLogin = False