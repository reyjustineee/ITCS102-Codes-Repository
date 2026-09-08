import getpass

username = "ethan"
password = "775530549"


i = input("Input Username ---> ")
t = getpass.getpass("Input Password ---> ")

if username == i and t == password :
	print("CORRECT")
else :
	print("INCORRECT")