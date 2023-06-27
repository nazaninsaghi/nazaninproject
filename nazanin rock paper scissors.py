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
    choices = ["rock", "paper", "scissors"]
    userscore = 0
    computerscore = 0
    while True:
        player1 = input("entekhab konid (rock/paper/scissors): ")
        if player1 not in choices:
            print("eshtebah entekhab kardi !")
            continue
        computerchoice = random.choice(choices)
        print("Computer chose:", computerchoice)
        if player1 == computerchoice:
            print("Tie!")
        elif player1 == "rock" and computerchoice == "scissors":
            print("You win!")
            userscore += 1
        elif player1 == "paper" and computerchoice == "rock":
            print("You win!")
            userscore += 1
        elif player1 == "scissors" and computerchoice == "paper":
            print("You win!")
            userscore += 1
        else:
            print("Computer wins!")
            computerscore += 1
        print("Your score:", userscore)
        print("Computer score:", computerscore)
        if userscore == 3 or computerscore == 3:
            break
    if userscore > computerscore:
        print("Congratulations, you win!")
    elif computerscore > userscore:
        print("Sorry, you lose!")
    else:
        print("It's a tie!")

if login():
    playgame()