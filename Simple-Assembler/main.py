import sys

complete_input = sys.stdin.read()

memory = {}
queue=[]
registers=[0,0,0,0,0,0,0]


opcodes = {
    "add": "00000",
    "sub": "00001",
    "mov_imm": "00010",
    "mov_reg": "00011",
    "ld": "00100",
    "st": "00101",
    "mul": "00110",
    "div": "00111",
    "rs": "01000",
    "ls": "01001",
    "xor": "01010",
    "or": "01011",
    "and": "01100",
    "not": "01101",
    "cmp": "01110",
    "jmp": "01111",
    "jlt": "10000",
    "jgt": "10001",
    "je": "10010",
    "hlt": "10011"
}


operators=["add","sub","mov","ld", "st",
            "mul", "div", "rs", "ls","xor",
            "or", "and", "not","cmp", "jmp",
            "jlt", "jgt", "je"]

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

memory_counter=0

error = 0
hlt_counter=0

for line in temp:
    line = str(line)
    if line=="":
        continue
    lis = line.split()
    if hlt_counter>0:
        error=1 
    if lis[0] in operators:
        memory[memory_counter]=[line, "operator"]
        memory_counter+=1
    elif lis[0]=="var":
        queue.append(line)
    elif lis[0][-1]==":":
        memory[memory_counter]=[" ".join(lis[1:]) ,"label", lis[0][:-1]]
        if len(lis)>1 and lis[1]=="hlt":
            hlt_counter+=1
        memory_counter+=1

    elif lis[0]=="hlt":
        memory[memory_counter]=[line,"halt"]
        memory_counter+=1
        hlt_counter+=1
    else:
        error = 1

# if list(memory.values())[-1][0].split()[0]!="hlt" or hlt_counter!=1:
#     error=1

error2=0

if error!=0:
    print("ERROR with hlt")
    
if memory_counter>256:
    error=1
    error2=1
    print("Memory error")
    

for i in queue:
    memory[memory_counter] =  [i, "variable"]
    memory_counter+=1

big_ans = []

for i in memory.keys():
    if(error ==1 or error2 ==1):
        break
    ans=""
    inp = memory[i]
    index = 0

    if list(inp[0].split())[index] == "add":
        f = 0
        for i in range(1,4):
            reg_val = int(inp[0].split()[i][1:])
            if reg_val not in range(7):
                print("ERROR: Wrong argument for register")
                error2=1
                f = 1
                break
        if f == 1:
            break
        if len(list(inp[0].split()))==4:
            ans+=opcodes["add"]+"00"
            ans+="{:03b}".format(int(inp[0].split()[1][1]))
            ans+="{:03b}".format(int(inp[0].split()[2][1]))
            ans+="{:03b}".format(int(inp[0].split()[3][1]))
            big_ans.append(ans)
        else:
            print("ERROR: Not correct arguments for add\n")
            error2=1


    elif list(inp[0].split())[index] == "sub":
        f = 0
        for i in range(1,4):
            reg_val = int(inp[0].split()[i][1:])
            if reg_val not in range(7):
                print("ERROR: Wrong argument for register")
                error2 =1
                f = 1
                break
        if f == 1:
            break
        if len(list(inp[0].split()))==4:
            ans+=opcodes["sub"]+"00"
            ans+="{:03b}".format(int(inp[0].split()[1][1]))
            ans+="{:03b}".format(int(inp[0].split()[2][1]))
            ans+="{:03b}".format(int(inp[0].split()[3][1]))
            big_ans.append(ans)
        else:
            print("ERROR: Not correct arguments for sub")
            error2=1

    elif list(inp[0].split())[index] == "mul":
        if len(list(memory[i][0].split()))==4:
            ans+=opcodes["mul"]+"00"
            ans+="{:03b}".format(int(inp[0].split()[1][1]))
            ans+="{:03b}".format(int(inp[0].split()[2][1]))
            ans+="{:03b}".format(int(inp[0].split()[3][1]))
            big_ans.append(ans)
        else:
            print("ERROR: Not correct arguments for multiplication")
            error2=1


    elif list(inp[0].split())[index] == "div":
        if len(list(memory[i][0].split()))==3:
            ans+=opcodes["div"]+"00000"
            ans+="{:03b}".format(int(inp[0].split()[1][1]))
            ans+="{:03b}".format(int(inp[0].split()[2][1]))
            big_ans.append(ans)
        else:
            print("ERROR: Not correct arguments for division")
            error2=1


    elif list(inp[0].split())[index] == "not":
        if len(list(memory[i][0].split()))==3:
            ans+=opcodes["not"]+"00000"
            ans+="{:03b}".format(int(inp[0].split()[1][1]))
            ans+="{:03b}".format(int(inp[0].split()[2][1]))
            big_ans.append(ans)
        else:
            print("ERROR: Not correct arguments for bitwise NOT")
            error2=1
    elif list(inp[0].split())[index] == "cmp":
        if len(list(memory[i][0].split()))==3:
            ans+=opcodes["cmp"]+"00000"
            ans+="{:03b}".format(int(inp[0].split()[1][1]))
            ans+="{:03b}".format(int(inp[0].split()[2][1]))
            big_ans.append(ans)
        else:
            print("ERROR: Not correct arguments to compare")
            error2=1   


    elif list(inp[0].split())[index] == "and":
        if len(list(memory[i][0].split()))==4:
            ans+=opcodes["and"]+"00"
            ans+="{:03b}".format(int(inp[0].split()[1][1]))
            ans+="{:03b}".format(int(inp[0].split()[2][1]))
            ans+="{:03b}".format(int(inp[0].split()[3][1]))
            big_ans.append(ans)
        else:
            print("ERROR: Not correct arguments for bitwise AND")
            error2=1


    elif list(inp[0].split())[index] == "or":
        if len(list(memory[i][0].split()))==4:
            ans+=opcodes["or"]+"00"
            ans+="{:03b}".format(int(inp[0].split()[1][1]))
            ans+="{:03b}".format(int(inp[0].split()[2][1]))
            ans+="{:03b}".format(int(inp[0].split()[3][1]))
            big_ans.append(ans)
        else:
            print("ERROR: Not correct arguments for bitwise OR")  
            error2=1     


    elif list(inp[0].split())[index] == "xor":
        if len(list(memory[i][0].split()))==4:
            ans+=opcodes["xor"]+"00"
            ans+="{:03b}".format(int(inp[0].split()[1][1]))
            ans+="{:03b}".format(int(inp[0].split()[2][1]))
            ans+="{:03b}".format(int(inp[0].split()[3][1]))
            big_ans.append(ans)
        else:
            print("ERROR: Not correct arguments for bitwise XOR")
            error2=1


    elif list(inp[0].split())[index] == "mov":
        if inp[0].split()[2][0] == "$":
            if int(inp[0].split()[1][1:]) not in range(7):
                print("ERROR: Wrong argument for register")
                error2=1
                break
            if len(list(inp[0].split()))==3:
                    ans+=opcodes["mov_imm"]
                    ans+="{:03b}".format(int(inp[0].split()[1][1]))
                    ans+="{:08b}".format(int(inp[0].split()[2][1:]))
                    big_ans.append(ans)
            else:
                    print("ERROR: Not correct arguments for mov")

        elif inp[0].split()[2][0] == "R":
            if int(inp[0].split()[1][1:]) not in range(7) or int(inp[0].split()[2][1:]) not in range(7):
                print("ERROR: Wrong argument for register")
                error2=1
                break

            if len(list(memory[i][0].split()))==3:
                    ans+=opcodes["mov_reg"]+"0"*5
                    ans+="{:03b}".format(int(inp[0].split()[1][1]))
                    #if(inp[0].split()[2] != "FLAGS"):
                    ans+="{:03b}".format(int(inp[0].split()[2][1]))
                    
                    big_ans.append(ans)
            else:
                    print("ERROR: Not correct arguments for mov")
                    error2=1
        elif inp[0].split()[2] == "FLAGS":
            if int(inp[0].split()[1][1:]) not in range(7):
                print("ERROR: Wrong argument for register")
                error2=1
                break
            ans+=opcodes["mov_reg"]+"0"*5
            ans+="{:03b}".format(int(inp[0].split()[1][1]))
            ans+="111"
            big_ans.append(ans)
        else:
            print("ERROR: Invalid 2nd argument")
            error2=1


    elif list(inp[0].split())[index] == "ld":
        if len((list(inp[0].split())))!=3:
            print("ERROR in load")
            error2=1
        ans+=opcodes["ld"]
        ans+="{:03b}".format(int(inp[0].split()[1][1]))
        for j in memory.keys():
            if memory[j][1]=="variable" and memory[j][0].split()[1]==inp[0].split()[2]:
                ans+="{:08b}".format(j)
        big_ans.append(ans)


    elif list(inp[0].split())[index] == "st":
        if len((list(inp[0].split())))!=3:
            print("ERROR in load")
            error2=1
        ans+=opcodes["st"]
        ans+="{:03b}".format(int(inp[0].split()[1][1]))
        for j in memory.keys():
            if memory[j][1]=="variable" and memory[j][0].split()[1]==inp[0].split()[2]:
                ans+="{:08b}".format(j)
        big_ans.append(ans)


    elif list(inp[0].split())[index] == "rs":
        if int(inp[0].split()[1][1:]) not in range(7):
            print("ERROR: Wrong argument for register")
            error2=1
            break
        if len(list(inp[0].split()))==3:
                ans+=opcodes["mov_imm"]
                ans+="{:03b}".format(int(inp[0].split()[1][1]))
                ans+="{:08b}".format(int(inp[0].split()[2][1:]))
                big_ans.append(ans)
        else:
                print("ERROR: Not correct arguments for rs")
                error2=1


    elif list(inp[0].split())[index] == "ls":
        if int(inp[0].split()[1][1:]) not in range(7):
            print("ERROR: Wrong argument for register")
            error2=1
            break
        if len(list(inp[0].split()))==3:
                ans+=opcodes["mov_imm"]
                ans+="{:03b}".format(int(inp[0].split()[1][1]))
                ans+="{:08b}".format(int(inp[0].split()[2][1:]))
                big_ans.append(ans)
        else:
                print("ERROR: Not correct arguments for ls")
                error2=1


    elif list(inp[0].split())[index] == "jmp":
        tempp = list(inp[0].split())[1]
        if len(list(inp[0].split()))==2:
            maddr=-1
            for j in memory.keys():
                if memory[j][1]=="label" and memory[j][2]==tempp:
                    maddr = j
            if maddr==-1:
                print("label not found")
                error2=1
                continue
            ans+=opcodes["jmp"]+"0"*3
            ans +="{:08b}".format(maddr)
            big_ans.append(ans)
        else:
            print("ERROR: Not correct arguments for jmp")            
            error2=1
    elif list(inp[0].split())[index] == "jlt":
        tempp = list(inp[0].split())[1]
        if len(list(inp[0].split()))==2:
            maddr=-1
            for j in memory.keys():
                if memory[j][1]=="label" and memory[j][2]==tempp:
                    maddr = j
            if maddr==-1:
                print("label not found")
                error2=1
                continue
            ans+=opcodes["jlt"]+"0"*3
            ans +="{:08b}".format(maddr)
            big_ans.append(ans)
        else:
            print("ERROR: Not correct arguments for jlt")
            error2=1
    elif list(inp[0].split())[index] == "jgt":
        tempp = list(inp[0].split())[1]
        if len(list(inp[0].split()))==2:
            maddr=-1
            for j in memory.keys():
                if memory[j][1]=="label" and memory[j][2]==tempp:
                    maddr = j
            if maddr==-1:
                print("label not found")
                error2=1
                continue
            ans+=opcodes["jgt"]+"0"*3
            ans +="{:08b}".format(maddr)
            big_ans.append(ans)
        else:
            print("ERROR: Not correct arguments for jgt")     
            error2=1         

    elif list(inp[0].split())[index] == "je":
        tempp = list(inp[0].split())[1]
        if len(list(inp[0].split()))==2:
            maddr=-1
            for j in memory.keys():
                if memory[j][1]=="label" and memory[j][2]==tempp:
                    maddr = j
            if maddr==-1:
                print("label not found")
                error2=1
                continue
            ans+=opcodes["je"]+"0"*3
            ans +="{:08b}".format(maddr)
            big_ans.append(ans)
        else:
            print("ERROR: Not correct arguments for je")
            error2=1

    elif list(inp[0].split())[index] == "hlt":
        ans+=opcodes["hlt"]+"0"*11
        big_ans.append(ans)
    
    elif list(inp[0].split())[index] == "var":
        pass
    else:
        print("Invalid operation")
        error2=1
        break
    

if(error!=1 and error2!=1):
    for line in big_ans:
        print(line)
