file = open("day5_input.txt","r") 
range_list =[]
ids =[]
for i,line in enumerate(file):
    if line == "\n":
        break
    range_value =line.strip().split("-")
    range_list.append((int(range_value[0]),int(range_value[1])))
    range_list.sort()

for i,line in enumerate(file):
    ids.append(int(line.strip()))
file.close()

def getFreshFood():
    fresh_list=[]
    for id in ids:
        for start,end in range_list:
            if id in range(start,end+1):
                fresh_list.append(id)
                break
    return len(fresh_list)

def getAllFreshFood():
    newList =[]
    index = 0
    start =range_list[index][0]
    end =range_list[index][1]
    while (index) <len(range_list):
        try:
            s =range_list[index+1][0]
            e =range_list[index+1][1]
        except IndexError:
             newList.append((start,end))
             break
        if end <s:
            newList.append((start,end))
            start =range_list[index+1][0]
            end =range_list[index+1][1]
        elif end<e:
            end = e
        index+=1
    return countRanges(newList)

def countRanges(range_list):
    total = 0
    for start,end in range_list:
        total += (end-start)+1
    return total

def printList(range_list):
    for start,end in range_list:
        print(f"{start} {end}",end="\n")
    print(f"len: {len(range_list)}",end="\n\n")



#print(len(range_list))
#print(getFreshFood())
#print(getAllFreshFood())
print(f"total: {getAllFreshFood()}")
#newList.sort()
#printList(newList)
#printList(range_list)