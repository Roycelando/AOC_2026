file = open("day4_input.txt","r")
adjDict ={}
matrix = []

#Storing the data
for i,line in enumerate(file):
    line = line.strip()
    matrix.append(list(line))
    for j,char in enumerate(line):
        matrix[i][j] = char
        if char =="@":
            adjDict[(i,j)] =[]
file.close

#print(matrix,end="\n")
#print(adjDict,end="\n")

def getAdjValues(matrix,r,c):
    for i in range(-1,2):
        for j in range(-1,2):
            try:
                if matrix[r+i][c+j] != "@" or (i==0 and j ==0):
                    continue
                if r+i < 0 or c +j <0 :
                    continue
                adjDict[(r,c)].append((r+i,c+j))
            except IndexError:
                continue
    return 

def printMatrix():
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end=" ")
        print(end="\n")

def getTotal():
    total = 0
    count =0
    while True:
        removeList =[]

        for k,v in adjDict.items():
            if len(v) < 4:
                removeList.append(k)
                total+=1
        
        for value in removeList:
            adjDict.pop(value)

        for r in removeList:
            for k,v in adjDict.items(): 
                if r not in v:
                    continue
                adjDict[k] = [(x,y) for (x,y) in v if (x,y) != r]

        if len(removeList) <1:
            break

    return total


def optimizeForkLifts(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != "@" :
                continue
            getAdjValues(matrix,i,j)
    return getTotal()


print(f"Total: {optimizeForkLifts(matrix)}")

