
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
    file.close     

file = open("day6_test.txt","r")
line = file.readline().strip()
line_length = len(line)
math_problem =[[] for i in range(line_length)]

for line in file:
    line_list = line.split()
    for i,val in enumerate(line_list):
        if is_number(val):
            math_problem[i].append(int(val))
        else:
            math_problem[i].append(val)
file.close     


def printNumbers():
    for i, _ in enumerate(math_problem):
        for j, _ in enumerate(math_problem[0]):
            if math_problem[i][j] == " ":
                print("space", end=" ")
            else:
                print(math_problem[i][j], end=" ")
        print(end="\n")



def rightPad(value,num):
    num_pad = num - len(value)
    padding = " "*num_pad
    return value+padding

def reverseString(value):
    if len(value) == 1:
        return value
    return value[-1] + reverseString(value[:-1])


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


#new_math_problem = transformCephalopodNumbers()

#print(math_problem)
#print(new_math_problem)

#print(f"{doCephalopodMath(math_problem)}")
#print(f"{doCephalopodMath(new_math_problem)}")






