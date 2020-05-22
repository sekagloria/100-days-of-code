import random

def game():
    hidden_num = random.randint(1,20)
    guesses = []

    while len(guesses) <5:
        try:
            guess = int(input("Guess a number between  1 and 20:"))
        except ValueError:
            print("{} is not an integer!" .format(guess))
        else:
            if guess == hidden_num:
                print("You won! The number was {}" .format(hidden_num))
                break
            elif guess < hidden_num:
                print("The number is higher than {}" .format(guess))
            else:
                print("The number is lower than {}" .format(guess))
            guesses.append(guess)
    else:
        print ("you guessed wrong! The number was {}".format(hidden_num))  
    play_again = ("Do you want to play again? Y/n")
    if play_again.lower() !="n":  
        game()
    else:
        print ("Good bye")              
game()