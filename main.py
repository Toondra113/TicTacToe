import os
from busybee import loadboard, whosturn, checkval, wincheck

#Define

places = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : "6", 7 : '7', 8 : '8', 9 : '9'}
turn = 0
online = True

#main

while online:
  #wipes console (board)
  os.system('cls' if os.name == 'nt' else 'clear') 
  loadboard(places)
 
  
  if whosturn(turn) == 'X':
    move = input("Player 1: Where do you want to move? ")
    #repeat until valid input
    while checkval(move, places) == False: 
      move = input("Player 1: Where do you want to move? ")
      
    places[int(move)] = 'X'
        
    
  else:
    move = input("Player 2: Where do you want to move? ")
    while checkval(move, places) == False:
      move = input("Player 2: Where do you want to move? ")
    
    places[int(move)] = 'O'

  if wincheck(places) != False:
    if wincheck == 'X':
      os.system('cls' if os.name == 'nt' else 'clear') 
      loadboard(places)
      print("Player 2 wins!")
    else:
      os.system('cls' if os.name == 'nt' else 'clear') 
      loadboard(places)
      print("Player 1 wins!")

    again = input("Play again? (y/n) ")
    if again == 'y':
      turn = -1
      places = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : "6", 7 : '7', 8 : '8', 9 : '9'}
    else: 
      online = False
  
    
  
  
  #Iterate next turn
  turn = turn + 1