import sys

complete_input = sys.stdin.read()

temp=[]
temp2 = ""
for char in complete_input:
    if char=='\n':
        temp.append(temp2)
        temp2=""
    else:
        temp2+=char
if temp2!="":
    temp.append(temp2)
    temp2=""

reg = [0,0,0,0,0,0,0]
flags = [0,0,0,0]

pc = 0

def binaryToDecimal(n):
    return int(n,2)

for line in temp:
    opcode = line[:5]
    if(opcode == "00000"): #add
        flags = [0,0,0,0]
        reg1 = line[7:10]
        reg2= line[10:13]
        reg3 = line[13:16]
        reg[binaryToDecimal(reg1)] = reg[binaryToDecimal(reg2)]+reg[binaryToDecimal(reg3)]
        print("{:08b}".format(pc), end=" ")
        for i in reg:
            print("{:016b}".format(i), end = " ")
        faltu="0"*12
        flag_val=faltu
        for i in flags:
            flag_val+=str(i)
        print(flag_val)
        pc+=1
