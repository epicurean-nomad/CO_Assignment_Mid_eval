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


def fn(pc):
    
    print("{:08b}".format(pc), end=" ")
    for i in reg:
        print("{:016b}".format(i), end = " ")
    faltu="0"*12
    flag_val=faltu
    for i in flags:
        flag_val+=str(i)
    print(flag_val)
    pc+=1

j = 0
while j<len(temp):
    line = temp[j]
    opcode = line[:5]
    
    if(opcode == "00000"): #add
        flags = [0,0,0,0]
        reg1 = line[7:10]
        reg2= line[10:13]
        reg3 = line[13:16]
        reg[binaryToDecimal(reg1)] = reg[binaryToDecimal(reg2)]+reg[binaryToDecimal(reg3)]
        if(reg[binaryToDecimal(reg1)]>pow(2,16)):
            flags[0]=1
            reg[binaryToDecimal(reg1)] = pow(2,16)-reg[binaryToDecimal(reg1)]
        fn(pc)
        pc+=1

    elif(opcode=="00010"): #mov imm
        flags=[0,0,0,0]
        reg1 = binaryToDecimal(line[5:8])
        imm_val = binaryToDecimal(line[8:16])
        reg[reg1] = imm_val
        fn(pc)
        pc+=1
    
    elif(opcode=="00011"): #mov reg
        flags=[0,0,0,0]
        reg1 = binaryToDecimal(line[10:13])
        reg2 = binaryToDecimal(line[13:16])
        reg[reg1] = reg[reg2]
        fn(pc)
        pc+=1





    elif (opcode == "01111"): #jmp uncd 
        flags = [0,0,0,0]
        j = binaryToDecimal(line[8:])
        fn(pc)
        pc+=1
        j+=1
        continue

    elif (opcode == "10000"):   #jlt
        if flags[1]==1:
            j = binaryToDecimal(line[8:])
            flags = [0,0,0,0]
            fn(pc)
            pc+=1
            j+=1
            continue
        flags = [0,0,0,0]
        fn(pc)
        pc+=1

    elif (opcode == "10001"):  #jgt
        if flags[2]==1:
            j = binaryToDecimal(line[8:])
            flags = [0,0,0,0]
            fn(pc)
            pc+=1
            j+=1
            continue
        flags = [0,0,0,0]
        fn(pc)
        pc+=1    

    elif (opcode == "10010"): #je
        if flags[3]==1:
            j = binaryToDecimal(line[8:])
            flags = [0,0,0,0]
            fn(pc)
            pc+=1
            j+=1
            continue
        flags = [0,0,0,0]
        fn(pc)
        pc+=1

    elif (opcode == "01110"): #cmp
        reg1=line[10:13]
        reg2 = line[13:16]
        if(binaryToDecimal(reg1)>binaryToDecimal(reg2)):
            flags[2]=1
        elif(binaryToDecimal(reg1)==binaryToDecimal(reg2)):
            flags[3]=1
        else:
            flags[1]=1
        fn(pc)
        pc+=1
    
    elif(opcode == "00001"): #sub
        flags = [0,0,0,0]
        reg1 = line[7:10]
        reg2= line[10:13]
        reg3 = line[13:16]
        reg[binaryToDecimal(reg1)] = reg[binaryToDecimal(reg2)]-reg[binaryToDecimal(reg3)]
        if(reg[binaryToDecimal(reg1)]>pow(2,16)):
            flags[0]=1
            reg[binaryToDecimal(reg1)] = pow(2,16)-reg[binaryToDecimal(reg1)]
        fn(pc)
        pc+=1

    elif(opcode == "00110"): #mul
        flags = [0,0,0,0]
        reg1 = line[7:10]
        reg2= line[10:13]
        reg3 = line[13:16]
        reg[binaryToDecimal(reg1)] = reg[binaryToDecimal(reg2)]*reg[binaryToDecimal(reg3)]
        if(reg[binaryToDecimal(reg1)]>pow(2,16)):
            flags[0]=1
            reg[binaryToDecimal(reg1)] = pow(2,16)-reg[binaryToDecimal(reg1)]
        fn(pc)
        pc+=1

    elif(opcode == "01010"): #xor
        flags = [0,0,0,0]
        reg1 = line[7:10]
        reg2= line[10:13]
        reg3 = line[13:16]
        reg[binaryToDecimal(reg1)] = reg[binaryToDecimal(reg2)]^reg[binaryToDecimal(reg3)]
        
        fn(pc)
        pc+=1
        
    elif(opcode == "01011"): #or
        flags = [0,0,0,0]
        reg1 = line[7:10]
        reg2= line[10:13]
        reg3 = line[13:16]
        reg[binaryToDecimal(reg1)] = reg[binaryToDecimal(reg2)]|reg[binaryToDecimal(reg3)]
        
        fn(pc)
        pc+=1

    elif(opcode == "01100"): #and
        flags = [0,0,0,0]
        reg1 = line[7:10]
        reg2= line[10:13]
        reg3 = line[13:16]
        reg[binaryToDecimal(reg1)] = reg[binaryToDecimal(reg2)]&reg[binaryToDecimal(reg3)]
        
        fn(pc)
        pc+=1
    
    elif (opcode == "00111"): #div
        reg3=line[10:13]
        reg4 = line[13:16]
        reg[0] = reg[binaryToDecimal(reg3)]//reg[binaryToDecimal(reg4)]
        reg[1] = reg[binaryToDecimal(reg3)]%reg[binaryToDecimal(reg4)]
        fn(pc)
        pc+=1
        
    elif (opcode == "01101"): #not
        reg1=line[10:13]
        reg2 = line[13:16]
        reg[binaryToDecimal(reg1)] = ~(reg[binaryToDecimal(reg2)])
        fn(pc)
        pc+=1
    
    elif(opcode == "10011"): #halt
        flags = [0,0,0,0]
        fn(pc)
        pc+=1

    j+=1
