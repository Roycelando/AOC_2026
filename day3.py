file = open("day3_input.txt")
banks =[]
for line in file: 
    banks.append(line.strip())
file.close()

def maxPower(banks) ->int:
    powerSum =0
    for bank in banks:
        currBank = list(bank)
        bigbig =(0,0)
        big = (0,0)

        for i,bat in enumerate(currBank):
            bat = int(bat)
            if bat > bigbig[1]:
                bigbig = (i,bat)
        for i in range(bigbig[0], len(currBank)):
            bat = int(currBank[i])
            if bat > big[1] and i != bigbig[0]:
                big = (i,bat)
        if big[1] ==0:
            for i,bat in enumerate(currBank):
                bat = int(bat)
                if bat > big[1] and i != bigbig[0]:
                    big = (i,bat)
            newVal =  int(str(big[1]) + str(bigbig[1]))
        else :    
            newVal =  int(str(bigbig[1]) + str(big[1]))
        print(newVal)
        powerSum += (newVal)
    return powerSum


def solveMaxPowerImporved(banks,batSize)->int:
    total =0
    for bank in banks:
        total+= int(maxPowerImporoved(bank,batSize))
    return total


def maxPowerImporoved(bank, batLen) ->str:
    #print(f"{bank} {batLen}",end="\n")
    if batLen <=0:
        return ""
    largest = -1
    largestIndex = -1
    for i,char in enumerate(bank):
        if int(char) > largest and len(bank[i+1:]) >=(batLen-1):
            largest = int(char)
            largestIndex = i
    
    return str(largest) + maxPowerImporoved(bank[largestIndex+1:],batLen-1)

print(f"total: {solveMaxPowerImporved(banks,2)}")
    


#print(f"sum: {maxPower(banks)}")