#This is a dictionary, which is a collection of key-value pairs. The key is the name of the variable, and the value is the value of the variable.

def loadboard(places):
  
  board = f"{places[1]}|{places[2]}|{places[3]}\n{places[4]}|{places[5]}|{places[6]}\n{places[7]}|{places[8]}|{places[9]}"
  print(board)

def whosturn(round):
  if round % 2 == 0:
    return "X"
  else:
    return "O"






  

