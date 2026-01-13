class Node:
  def __init__(self,value:any,left:Node|None = None, right: Node | None = None):
    self._value = value
    self._left = left
    self._right = right

  @property
  def value(self):
    return self._value

  @property
  def left(self):
    return self._left

  @property
  def right(self):
    return self._right

  @value.setter
  def value(self, new_value):
    self._value = new_value
  
  @right.setter
  def right(self,new_right: Node):
    self._right = new_right

  @left.setter
  def left(self,new_left: Node):
    self._left = new_left

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

def countTheSplits(theSet:set,row:int,col:int,headNode:Node,nodeList:list[Node],label:str="down"):
  try:
    if inputData[row+1][col] == "^" and (row+1,col) not in theSet:
      theSet.add((row+1,col))
      headNode.left = Node((row+1,col-1))
      headNode.right = Node((row+1,col+1))
      nodeList.append(headNode.left)
      nodeList.append(headNode.right)
      countTheSplits(theSet,row+1,col-1,headNode.left,nodeList,"left")
      countTheSplits(theSet,row+1,col+1,headNode.right,nodeList,"right")
    elif inputData[row+1][col] == "^" and (row+1,col) in theSet:
      for nodeItem in nodeList:
        if (nodeItem.value == (row+1,col-1) or nodeItem.value == (row+1,col+1)):
          headNode.right = nodeItem
          break
      return
    else:  
      countTheSplits(theSet,row+1,col,headNode,nodeList)
    return theSet
  except IndexError:
    return
  
def createTree(theSet:set,row:int,col:int,currNode:Node,nodeList:list[Node],label:str="down"):
  try:
    if inputData[row+1][col] == "^" and (row+1,col) not in theSet:
      if currNode.value == None:
        theSet.add((row+1,col))
        currNode.value =(row+1,col)
        nodeList.append(currNode)
        createTree(theSet,row+1,col-1,currNode,nodeList,"left")
        createTree(theSet,row+1,col+1,currNode,nodeList,"right")
      else:
        theSet.add((row+1,col))
        temp = Node((row+1,col))
        nodeList.append(temp)
        if label == "left":
          currNode.left = temp
        if label == "right":
          currNode.right = temp
        createTree(theSet,row+1,col-1,temp,nodeList,"left")
        createTree(theSet,row+1,col+1,temp,nodeList,"right")
    elif inputData[row+1][col] == "^" and (row+1,col) in theSet:
      for n in nodeList:
        if n.value == (row+1,col):
          if label == "left":
            currNode.left = n
            break
          if label == "right":
            currNode.right = n
            break
    else:  
      createTree(theSet,row+1,col,currNode,nodeList,label)
    return 
  except IndexError:
    return 

def printNodeStack(head:Node):
  stack:list[Node] = []
  stack.append(head)
  while len(stack) != 0:
    popped_list:list[Node] = []
    for item in stack:
      index = stack.index(item)
      popped_item:Node = stack.pop(index)
      print(popped_item.value, end=" ")
      popped_list.append(popped_item)
    print()

    for item in popped_list:
      if item.left != None:
        stack.append(item.left)
      if item.right != None:
        stack.append(item.right)

def print_tree(node: Node, level=0, label="Root:"):
    if node is None:
        return

    print_tree(node.right, level + 1, "R:")
    print("    " * level*2 + label + str(node.value))
    print_tree(node.left, level + 1, "L:")
    
def countPaths(node:Node,currentPath:list[Node], allPaths:list[list[Node]],level):
  if node == None:
    return 1

  for p in currentPath:  
    if p[0] == node.value:
      return p[1]

  total_paths = countPaths(node.left,currentPath,allPaths,level+1) + countPaths(node.right,currentPath,allPaths,level+1)
  currentPath.append((node.value,total_paths))
  return total_paths


def countNodes(node:Node):
  if node == None:
    return 0

  return  countNodes(node.left) + countNodes(node.right) +1

startRow,startCol = getStartCoordinates()
#head = Node((startRow,startCol))
#path_list = list(countTheSplits(set(),startRow,startCol, head,[]))
allPaths = []
currentPath =[]
#print_tree(head.value)
head = Node(None)
createTree(set(),startRow,startCol,head,[],"down")
#print_tree(head)
print(countPaths(head,currentPath,allPaths,0))
#print(countNodes(head))
#print(countPaths(head,currentPath,allPaths))



