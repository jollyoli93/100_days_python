from random import randint
from game_data import data
from art import logo, vs

rand_num1 = randint(0, len(data) - 1)
rand_num2 = randint(0, len(data) - 1)


#generate two random categories
def compare(cat1, cat2):
  first_follower = cat1['follower_count']
  second_follower = cat2['follower_count']

  if first_follower > second_follower:
    return 1
  elif first_follower < second_follower:
    return 2


def print_func(person):
  print(person['name'], person['description'], person['country'])

def welcome():
  print(logo)
  print(vs)

def high_or_low(num1, num2):
  welcome()
  game_over = False
  new_person = randint(0, len(data) - 1)

  while not game_over:
    first_person = data[num1]
    second_person = data[num2]

    if first_person['name'] == second_person['name']:
      second_person = new_person

    print_func(first_person)
    print(f"{first_person['follower_count']} million")
    print_func(second_person)
    print("\n")
    #get player input
    question = input('Higher or Lower? press 1 or 2: ')
    player_input = int(question)

    highest = compare(first_person, second_person)

    #if True make [0] == [1] person and generate new number for [1]
    if player_input == highest:
      print("Player wins, next question")
      print("\n")
      high_or_low(num2, new_person)
    else:
      game_over = True
      print(second_person['follower_count'])
      print("Player loses")
      high_or_low(new_person, new_person)


high_or_low(rand_num1, rand_num2)
