# from enum import Enum
#
#
# class Color(Enum):
#     RED = 'red'
#     GREEN = 'green'
#     BLUE = 'blue'
#
#
# color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))
# match color:
#     case Color.RED:
#         print("I see red!")
#     case Color.GREEN:
#         print("Grass is green")
#     case Color.BLUE:
#         print("I'm feeling the blues :(")

import random

lowest = 0
highest = 100

answer = random.randint(lowest, highest)
print(str(answer) + " 😀" )
