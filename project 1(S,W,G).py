import random
lst=['s','w','g']
chance=5
no_of_chance=0
computer_point=0
human_point=0

print("\t\t\t\t snake,water,gun \n \n")
print("s for snake \n w for water \n g for gun \n")

#making the game by using while loop

while no_of_chance<chance:
    _input=input('snake,water,gun:')
    _random=random.choice(lst)

    if _input==_random:
         print("Tie Both have 0 points")

    #if user enter s

    elif _input== "s" and _random=="g" :
        computer_point=computer_point+1
        print(f"your game {_input} and computer guess is {_random}\n")
        print("computer wins 1 points \n")
        print(f"computer_point is {computer_point} and your print is {human_point}\n")


    elif _input== "s" and _random=="w":
        human_point = human_point+1
        print(f"your guess {_input}and computer guess is {_random}\n")
        print("human wins 1 point \n")
        print(f"computer_point is {computer_point}and your point is {human_point}\n")

    # if user enter w

    elif _input=="w" and _random =="s":
        computer_point=computer_point+1
        print(f"your guess {_input} and computer guess is {_random}\n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point}\n")

    elif _input=="w" and _random =="g":
        human_point=human_point+1
        print(f"your guess {_input} and computer guess is {_random}\n")
        print("human wins 1 point \n")
        print(f"computer_point is{computer_point} and your point is {human_point}\n")
        
     

    # if user enter g


    elif _input=="g" and _random =="s":
        human_point=human_point+1
        print(f"your guess {_input} and computer guess is {_random}\n")
        print("human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is{human_point}\n")

    elif _input=="g" and _random =="w":
        computer_point=computer_point+1
        print(f"your guess {_input} and computer guess is {_random}\n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point}\n")
        


    else:
        print("you have input wrong \n")

no_of_chance = no_of_chance+1
print("f{chance-no_of_chance}is a left out of {chance} \n")

print("GAME OVER")

if computer_point==human_point:
    print("TIE")
elif computer_point>huma_point:
    print("COMPUTER WINNER AND YOU LOSE ")
else:
    print("YOU ARE THE WINNER AND COMPUTER LOSE")

print(f"your point is {human_point} and computer point is {computer_point}")


















        
    
