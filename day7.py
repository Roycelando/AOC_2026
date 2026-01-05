inputData = []
with open("day7_input.txt") as file:
  for line in file:
    inputData.append(list(line.strip()))

def printInputData():
  for i in range(len(inputData)):
    for j in range(len(inputData[0])):
      print(inputData[i][j],end=" ")
    print()

def getStartCoordinates():
  for i in range(len(inputData)):
    for j in range(len(inputData[0])):
      if inputData[i][j] == "S":
        return (i,j)

def countTheSplits(theSet:set,row:int,col:int):
  try:
    if inputData[row+1][col] == "^" and (row+1,col) not in theSet:
      theSet.add((row+1,col))
      countTheSplits(theSet,row+1,col-1)
      countTheSplits(theSet,row+1,col+1)
    elif inputData[row+1][col] == "^" and (row+1,col) in theSet:
      return
    else:  
      countTheSplits(theSet,row+1,col)
    return theSet
  except IndexError:
    return


startRow,startCol = getStartCoordinates()
print( sorted(list(countTheSplits(set(),startRow,startCol))))
