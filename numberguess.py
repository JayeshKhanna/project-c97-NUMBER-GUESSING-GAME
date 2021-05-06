import random
print("NUMBER GUESSING GAME")
ran=random.randint(1,9)
##print(ran)
chances=0
print("GUESS A NUMBER BETWEEN 1 TO 9")

while chances < 5:
    guess =int( input("ENTER YOUR GUESS :-"))
    if guess==ran:
        print("CONGRATS ! YOU WON")
        break

    elif guess<ran:
        print("YOUR GUESS IS TOO LOW ENTER A HIGHER NUMBER")

    else:
        print("YOUR GUESS IS TOO HIGH ")  

    chances=chances+1      

if chances>5:
    print("SORRY THE NUMBER IS ",ran)
    