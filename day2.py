# Reading input data
def parseDate():
    file = open('day2_input.txt',"r")
    list = file.readline().split(",")
    list = [tuple(a.split("-")) for a in list]
    file.close()
    return list

def printList(list):
    for val in list:
        print(val)

# 1A solution
def invalidRangeSum(list):
    invalidSum = 0
    for tup in list:
        start = int(tup[0]) 
        end = int(tup[1])
        for i in range(start, end+1):
            numstr = str(i)
            if(numstr[0] == "0"): #leading zeor invalid 
                invalidSum += i
                continue
            if(len(numstr)%2 != 0): # not divisible good number
                continue
            mid = len(numstr)//2 
            for p,q in zip(range(0,mid), range(mid,len(numstr))):
                if numstr[p] != numstr[q]:
                    break 
                if p == mid-1 or q == len(numstr)-1:
                    invalidSum +=i
    return invalidSum

#2B solution helper
def isOnlyRepating(str_value:str) -> bool:
    int_val = int(str_value)
    
    divisible = [x for x in range(1,len(str_value)) if len(str_value)%x ==0 and x != len(str_value)]
    for divisor in divisible:
        match = str_value[0:divisor]
        for i in range(0,len(str_value),divisor):
            if str_value[i:i+divisor] != match:
                break
            if i + divisor == len(str_value):
                return True

    return False


#2B solution
def invalidRangeSumTwo(list)->int:
    invalidSum = 0
    for tup in list:
        start = int(tup[0])
        end = int(tup[1])
        for i in range(start, end+1):
            if not isOnlyRepating(str(i)):
                continue
            invalidSum += i
    return invalidSum



list = parseDate()
print(f"final result: {invalidRangeSumTwo(list)}")





