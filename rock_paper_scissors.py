import random
options = ["rock", "paper", "scissor"]
print(" rock paper scissors game ".center(50,"="))
count_win = 0
count_lose = 0
while True:
    choice = input("enter your choice : ")
    n = random.choice(options)

    if(choice.lower() == "done"):
        break

    elif choice.lower() not in options:
        print("invalid choice \n")

    elif(choice.lower() == n):
        count_win += 1
        print("you won")
        print(f"win = {count_win} \n lose = {count_lose} \n")

    elif(choice.lower() != n):
        count_lose += 1
        print("you lost")
        print(f"win = {count_win} \nlose = {count_lose} \n")
print(" THANKS FOR PLAYING ".center(50,"="))