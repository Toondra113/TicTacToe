import os
from busybee import loadboard, whosturn

places = {1 : 'A', 2 : 'B', 3 : 'C', 4 : 'D', 5 : 'E', 6 : "F", 7 : 'G', 8 : 'H', 9 : 'I'}

turn = 0



online = True


while online:
  os.system('cls' if os.name == 'nt' else 'clear')
  loadboard(places)
 

  if whosturn(turn) == 'X':
    move = input("Player 1: Where do you want to move? ")
  else:
    move = input("Player 2: Where do you want to move? ")

  turn = turn + 1