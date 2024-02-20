# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(200)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

pokemon_types = ["Electric", "Water", "Psycic"]
pokemon_names = ["Pikachu", "Squirtal", "Jigglipuff"]

table.add_column("pokemon_names", pokemon_names)
table.add_column("Types", pokemon_types)

print(table)

