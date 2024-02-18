from random import randint
numbers_to_100 = randint(0, 101)

def game(number):
    game_over = False

    while not game_over:
        response = input("Do you want to play Easy or Hard? or press no to quit ")

        if response.lower() == "no":
            game_over = True
            break
        elif response.lower() == "hard":
            lives = 5
        else:
            lives = 10


        while lives > 0:
            print(f"{lives} Lives")
            print(number)

            guess_str = input("guess my number? ")
            guess = int(guess_str)

            if guess == number:
                print("Correct!")
                break
            elif guess > number:
                print("Too high, guess again")
                lives -= 1
            elif guess < number:
                print("Too low, guess again")
                lives -= 1
            else:
                print("Invalid number")

game(numbers_to_100)