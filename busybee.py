#This is a dictionary, which is a collection of key-value pairs. The key is the name of the variable, and the value is the value of the variable.

def loadboard(places):
  
  board = f"{places[1]}|{places[2]}|{places[3]}\n{places[4]}|{places[5]}|{places[6]}\n{places[7]}|{places[8]}|{places[9]}"
  print(board)

def whosturn(round): #Chceks if the round is even or odd (p1, p2)
  if round % 2 == 0:
    return "X"
  else:
    return "O"

def checkval(move, places): #verifies user input
  if not move.isdigit(): 
    print("Please enter a number")
    return False

  move_num = int(move)

  if move_num < 1 or move_num > 9:
    print("Please enter a number from 1 to 9")
    return False

  if places[move_num] in ['X', 'O']:
    print("That spot is already taken")
    return False

  return True


def wincheck(places): #searches for winner
  #Check horizontal
  if places[1] == places[2] == places[3] or places[4] == places[5] == places[6] or places[7] == places[8] == places[9]:
    return places[1]
  #checks vertical
  elif places[1] == places[4] == places[7] or places[2] == places[5] == places[8] or places[3] == places[6] == places[9]:
    return places[1]
  #checks diagonal
  elif places[1] == places[5] == places[9] or places[3] == places[5] == places[7]:
    return places[1]

#Otherwise no winer
  return False








  

