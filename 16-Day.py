from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("cyan")
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.color("green")

# screen = Screen()
# print(screen.canvheight)
# screen.title("AI Turtle")
# screen.bgcolor("black")
# screen.exitonclick()

table = PrettyTable()
table.add_column("Name", ["Shiv","Vishnu","Bramaha"])
table.add_column("Location", ['Kailash','Dwarika',"Heaven"])
table.add_column("Power",["Destroyer","Preserver","Creator"])
table.add_rows([["Shakti","Kailash","Feminine Energy"],["Lakshmi",'Dwarika', 'Wealth']])
table.add_row(["Swaraswati","Heaven","Knowledge"])
# table.field_names=["Age","Pet"]
table.align="r"
print(table)
print(table.get_string(fields=["Location", "Power"]))
print(table.align)

# Importing data from a CSV file
# Importing data from a database cursor