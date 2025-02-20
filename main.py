import os
from busybee import loadboard, whosturn, checkval

places = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : "6", 7 : '7', 8 : '8', 9 : '9'}

turn = 0



online = True


while online:
  os.system('cls' if os.name == 'nt' else 'clear')
  loadboard(places)
 
  
  if whosturn(turn) == 'X':
    move = input("Player 1: Where do you want to move? ")
    while checkval(move, places) == False:
      move = input("Player 1: Where do you want to move? ")
    places[int(move)] = 'X'
        
    
  else:
  
    move = input("Player 2: Where do you want to move? ")
    while checkval(move, places) == False:
      move = input("Player 2: Where do you want to move? ")
    
    places[int(move)] = 'O'

  turn = turn + 1