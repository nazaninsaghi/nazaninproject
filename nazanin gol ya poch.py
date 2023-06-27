import random

def login():
    username = input("Enter your username: ")
    if username == "1401231010":
        password = input("Enter your password : ")
        if password == "0024644285":
            print("Login successful!")
            return True
        else:
            print("Incorrect password!")
            return False
    else:
        print("eshtebah ast!")
        return False

def playgame():
    choices = ["gol","poch"]
    userscore = 0
    computerscore = 0
    while True:
        player1 = input("entekhab konid (gol ya poch?): ")
        if player1 not in choices:
            print("eshtebah entekhab kardi !")
            continue
        computerchoice = random.choice(choices)
        print("Computer chose:", computerchoice)
        if player1 == computerchoice:
            print("You win!")
            userscore += 1
        else:
            print("You Loose")
            computerscore += 1
        print("Your score:", userscore)
        print("Computer score:", computerscore)
        if userscore == 2 or computerscore == 2:
            break
    if userscore > computerscore:
        print("Congratulations, you win!")
    elif computerscore > userscore:
        print("Sorry, you lose!")
    else:
        print("It's a tie!")

if login():
    playgame()
