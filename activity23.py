#anime concept
shonen = []
korean = []
isekai = []
adventure = []
fantasy = []

while True:
    ans = input("Do you watch or read any anime? yes/no ---> ".title())

    if ans == "yes":
        print("What kind of anime do you watch or read? ")
        print("1 shonen\n 2 korean\n 3 isekai\n 4 adventure\n 5 fantasy".lower())

        choice = int(input("Input > "))

        if choice == 1:
            print("Shonen")
            title = input("Please input the title of the ANIME ---> ".upper())
            shonen.append(title)
            print(shonen)
            con = input("Do you wish to continue? yes/no ---> ".title())
            if con == "yes":
                continue

            delete = input("Do you want to delete an anime title? yes/no".lower())
            if delete == "yes":
                number = (input("Enter the anime title you want to delete: "))
                shonen.remove(number)
                print(shonen)
            else:
                break
        else:
            print("INVALID choice")
    else:
        break 