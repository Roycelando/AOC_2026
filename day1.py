file = open('day1_input.txt',"r")
myList:list[tuple[str,int]] = []

def createList():
    for line in file:
        line = line.strip()
        myList.append((line[0],int(line[1:])))
    file.close()

def printList():
    for tup in myList:
        print(tup)

def getPasswordBrute(value):
    password = 0
    currPos = value

    for tup in myList:

        if tup[0] == "R":
            for _ in range(1,tup[1]+1):
                currPos = (currPos + 1)%100
                if currPos == 0:
                    password +=1
        elif tup[0] == "L":
             for _ in range(tup[1],0,-1):
                currPos = (currPos -1)%100
                if currPos == 0:
                    password +=1           
    return password 
    

def getPassword(value:int) -> int:
    lastDialPos:int = value
    password:int = 0
    currDialPos:int = value 

    for tup in myList:
        rotations = tup[1]//100
        trueSteps = tup[1] -(100*rotations)
        password+=rotations

        if(tup[0] == 'R'):
            currDialPos = (lastDialPos+trueSteps)%100
            if (lastDialPos + trueSteps) > 100 and currDialPos != 0:
                password+=1
        elif(tup[0] == 'L'):
            currDialPos = (lastDialPos-trueSteps)%100
            if (lastDialPos - trueSteps) <0 and currDialPos !=0:
                password+=1
        if currDialPos==0 :
            password+=1

        lastDialPos = currDialPos
    return password

createList()
print(getPassword(50))
print(getPasswordBrute(50))
        






