
def is_number(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

def readFilePartOne():
    file = open("day6_test.txt","r")
    line = file.readline().strip().split()
    line_length = len(line)
    math_problem =[[] for i in range(line_length)]


    for i,val in enumerate(line):
        if is_number(val):
            math_problem[i].append(int(val))
        else:
            math_problem[i].append(val)

    for line in file:
        line_list = line.strip().split()
        for i,val in enumerate(line_list):
            if is_number(val):
                math_problem[i].append(int(val))
            else:
                math_problem[i].append(val)
    file.close()

file = open("day6_input.txt","r")
math_problem =[]

for line in file:
    line_list = line.strip("\n")
    new_line=[]
    for char in line_list:
        if char == " ":
            new_line.append("x")
        else:
            new_line.append(char)
    math_problem.append(new_line)
file.close()     

sign_list = math_problem[len(math_problem)-1]
sign_list = [x for x in sign_list if x!="x"]
sign_list.reverse()

print(sign_list)



def printMathProblem():
    for i in range(len(math_problem)-1):
        for j in range(len(math_problem[0])):
            print(math_problem[i][j],end=" ")
        print()


def printCephalopodNumbers():
    i = 0
    j = len(math_problem[0])-1
    new_problem = []
    the_numbers=[]
    while j >-1:
        new_str =""
        while i < len(math_problem)-1:
            if math_problem[i][j] == "x":
                i+=1
                continue
            new_str+=math_problem[i][j]
            i+=1
        i=0
        if(new_str !=""):
            new_val = int(new_str)
            the_numbers.append(new_val)
            print(new_val,end="\n")
        else:
            new_problem.append(the_numbers)
            the_numbers=[]
            print("you hit an x",end="\n")

        j-=1
    new_problem.append(the_numbers)
    return new_problem


def printNumbers():
    for i, _ in enumerate(math_problem):
        for j, val in enumerate(math_problem[i]):
            if val == " ":
                print("space", end=" ")
            elif val == "\n":
                 print("return", end=" ")
            else:
                print(val, end=" ")
        print(end="\n")



def rightPad(value,num):
    num_pad = num - len(value)
    padding = " "*num_pad
    return value+padding

def reverseString(value):
    if len(value) == 1:
        return value
    return value[-1] + reverseString(value[:-1])

def getCephalopodNumber():
    last_line = math_problem[len(math_problem)-1]
    print(last_line)
    firstSymbol = 0
    secondSymbol = 0
    for i,val in enumerate(last_line):
        if (val == "*" or val == "+") and i != 0:
            secondSymbol = i
            break
    diff = secondSymbol-firstSymbol


    for j in range(len(math_problem)-1):
        for i in range(len(math_problem)-1):
            pass
            


def transformCephalopodNumbers():
    newMath_list = []
    for questions in math_problem:
        sign =questions[-1]
        questions = questions[:-1]
        text_len = len(str(max(questions)))
        new_num =[[] for x in range(text_len)]

        for val in questions:
            val =  rightPad(str(val),text_len)
            print(val)

            for i,char in enumerate(val):
                new_num[i].append(char)
        new_num.append(sign)
        new_list = []
        for index in range(len(new_num)-1):
            value = int("".join(new_num[index]))
            new_list.append(value)
        new_list.append(sign)
        newMath_list.append(new_list)
    return newMath_list

def doCephalopodMath(math_problem):
    total = 0
    for question in math_problem:
        subtotal =question[0] 
        sign = question[len(question)-1]
        if sign == "*":
            for index in range(1,len(question)-1): 
                subtotal *= question[index]
        elif sign == "+":
            for index in range(1,len(question)-1): 
                subtotal += question[index]
        total +=subtotal
    return total


def doCephalopodMathTwo(math_problem,signs):
    total = 0
    for index,line in enumerate(math_problem):
        subtotal=line[0]
        sign = sign_list[index]
        if sign == "*":
            for i in range(1,len(line)):
                subtotal *=line[i]
            total += subtotal
        elif sign == "+":
            for i in range(1,len(line)):
                subtotal +=line[i]
            total += subtotal   

    return  total

math_problem = printCephalopodNumbers()
print(f"total: {doCephalopodMathTwo(math_problem,sign_list)}")

#getCephalopodNumber()
#printNumbers()
#new_math_problem = transformCephalopodNumbers()

#print(math_problem)
#print(new_math_problem)

#print(f"{doCephalopodMath(math_problem)}")
#print(f"{doCephalopodMath(new_math_problem)}")






