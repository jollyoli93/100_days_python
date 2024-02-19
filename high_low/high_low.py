from random import randint

def set_difficulty():
    EASY_LIFE = 10
    HARD_LIVE = 5

    response = input("Select difficulty: Press enter for Easy or type Hard --- press no to quit ")

    if response.lower() == "no":
        return True
    elif response.lower() == "hard":
        return HARD_LIVE
    else:
        return EASY_LIFE

def user_guess(number, lives):
        print("\n")
        guess_str = input("guess my number? ")
        guess = int(guess_str)

        if lives == 0:
            print("Game over")
            return 
        elif guess == number:
            print("Correct!")
            return True
        elif guess > number:
            print("Too high, guess again")
            return 
        elif guess < number:
            print("Too low, guess again")
            return 
        else:
            print("Invalid number")
            return


def game():
    numbers_to_100 = randint(0, 101)

    lives = set_difficulty()

    print(numbers_to_100)
    print(f"You have {lives} lives remaining")
    
    while lives > 0:
        play = user_guess(numbers_to_100, lives)

        if play == True:
            break
        elif lives == 0:
            print("Game over")
            break
        else:
            lives -= 1
            print(f"You have {lives} lives remaining")
    
    return 


game()