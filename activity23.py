#anime concept
shonen = []
korean = []
isekai = []
adventure = []
fantasy = []

while True:
    ans = input("Do you watch or read any anime? yes/no ---> ")

    if ans == "yes":
        print("What kind of anime do you watch or read? ")
        print("1 shonen\n 2 korean\n 3 isekai\n 4 adventure\n 5 fantasy")

        choice = int(input("Input > "))

        if choice == 1:
            print("Shonen")
            title = input("Please input the title of the ANIME ---> ")
            shonen.append(title)
            print(shonen)
            con = input("Do you wish to continue? yes/no ---> ")
            if con == "yes":
                continue
            else:
                break
        else:
            print("INVALID choice")