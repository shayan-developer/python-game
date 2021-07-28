from random import randint

import termcolor2 as t
print(t.colored("================== Rock , Paper , Scissors ==========","red"))

playerWins = 0
cpuWins = 0
while playerWins<3 and cpuWins<3:
    player = input("Make your move :")
    if player=="q":
        break
    randomNum = randint(0, 2)
    moves = ["rock", "paper", "scissors"]
    cpu = moves[randomNum]
    print(f"cpu move : {cpu}")
    if player == cpu:
       print("Thats tie ...")
    elif player == "rock":
        if cpu == "paper":
            print("cpu wins !")
            cpuWins += 1
        elif cpu == "scissors":
            print("player wins !")
            playerWins += 1
    elif player == "paper":
        if cpu == "rock":
            print("player wins !")
            playerWins += 1
        elif cpu == "scissors":
            print("cpu wins !")
            cpuWins += 1
    elif player == "scissors":
        if cpu == "rock":
            print("player wins !")
            playerWins += 1
        elif cpu == "paper":
            print("player wins !")
            playerWins += 1
    else:
        print(" somethins wrong . . .")
    print(t.colored(f"Player: {playerWins} cpu: {cpuWins}","cyan"))
    print("======================================")

if playerWins>cpuWins:
    print(t.colored("Player is winner \U0001F600","yellow"))
else:
    print(t.colored("Cpu is winner \U0001F600","yellow"))