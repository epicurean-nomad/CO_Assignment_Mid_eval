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

error = -1

hlt_counter=0

for line in temp:
    line = str(line)
    if line=="":
        continue
    lis = line.split()
    if lis[0] in operators:
        memory[memory_counter]=[line, "operator"]
        memory_counter+=1
    elif lis[0]=="var":
        queue.append(line)
        memory[memory_counter] =  [line, "variable"]
        memory_counter+=1
    elif lis[0][-1]==":":
        memory[memory_counter]=[line, "label"]
        memory_counter+=1
    elif lis[0]=="hlt":
        memory[memory_counter]=[line,"halt"]
        memory_counter+=1
        hlt_counter+=1
    else:
        error = 0

if error!=-1:
    print("INVALID OPERATION")

if list(memory.values())[-1][0].split()[0]!="hlt" or hlt_counter!=1: #I separated the first OR condition to give it a different Error Message
    print("ERROR with hlt")

#else:
    #print("OK")

#memory.values()

 #x = "{:03b}".format(2)
 #print(type(x))

for i in memory.keys():
    ans=""
    inp = memory[i]


    if list(inp[0].split())[0] == "add":
        f = 0
        for i in range(1,4):
            reg_val = int(inp[0].split()[i][1:])
            if reg_val not in range(7):
                print("ERROR: Wrong argument for register")
                f = 1
                break
        if f == 1:
            break
        if len(list(inp[0].split()))==4:
            ans+=opcodes["add"]+"00"
            ans+="{:03b}".format(int(inp[0].split()[1][1]))
            ans+="{:03b}".format(int(inp[0].split()[2][1]))
            ans+="{:03b}".format(int(inp[0].split()[3][1]))
            print(ans)
        else:
            print("ERROR: Not correct arguments for add\n")


    elif list(inp[0].split())[0] == "sub":
        f = 0
        for i in range(1,4):
            reg_val = int(inp[0].split()[i][1:])
            if reg_val not in range(7):
                print("ERROR: Wrong argument for register")
                f = 1
                break
        if f == 1:
            break
        if len(list(inp[0].split()))==4:
            ans+=opcodes["sub"]+"00"
            ans+="{:03b}".format(int(inp[0].split()[1][1]))
            ans+="{:03b}".format(int(inp[0].split()[2][1]))
            ans+="{:03b}".format(int(inp[0].split()[3][1]))
            print(ans)
        else:
            print("ERROR: Not correct arguments for sub")


    elif list(inp[0].split())[0] == "mul":
        if len(list(memory[i][0].split()))==4:
            ans+=opcodes["mul"]+"00"
            ans+="{:03b}".format(int(list(memory[i][0].split())[1][1]))
            ans+="{:03b}".format(int(list(memory[i][0].split())[2][1]))
            ans+="{:03b}".format(int(list(memory[i][0].split())[3][1]))
            print(ans)
        else:
            print("ERROR: Not correct arguments for multiplication")


    elif list(inp[0].split())[0] == "div":
        if len(list(memory[i][0].split()))==3:
            ans+=opcodes["div"]+"00000"
            ans+="{:03b}".format(int(list(memory[i][0].split())[1][1]))
            ans+="{:03b}".format(int(list(memory[i][0].split())[2][1]))
            print(ans)
        else:
            print("ERROR: Not correct arguments for division")


    elif list(inp[0].split())[0] == "not":
        if len(list(memory[i][0].split()))==3:
            ans+=opcodes["not"]+"00000"
            ans+="{:03b}".format(int(list(memory[i][0].split())[1][1]))
            ans+="{:03b}".format(int(list(memory[i][0].split())[2][1]))
            print(ans)
        else:
            print("ERROR: Not correct arguments for bitwise NOT")
    elif list(inp[0].split())[0] == "cmp":
        if len(list(memory[i][0].split()))==3:
            ans+=opcodes["cmp"]+"00000"
            ans+="{:03b}".format(int(list(memory[i][0].split())[1][1]))
            ans+="{:03b}".format(int(list(memory[i][0].split())[2][1]))
            print(ans)
        else:
            print("ERROR: Not correct arguments to compare")        


    elif list(inp[0].split())[0] == "and":
        if len(list(memory[i][0].split()))==4:
            ans+=opcodes["and"]+"00"
            ans+="{:03b}".format(int(list(memory[i][0].split())[1][1]))
            ans+="{:03b}".format(int(list(memory[i][0].split())[2][1]))
            ans+="{:03b}".format(int(list(memory[i][0].split())[3][1]))
            print(ans)
        else:
            print("ERROR: Not correct arguments for bitwise AND")


    elif list(inp[0].split())[0] == "or":
        if len(list(memory[i][0].split()))==4:
            ans+=opcodes["or"]+"00"
            ans+="{:03b}".format(int(list(memory[i][0].split())[1][1]))
            ans+="{:03b}".format(int(list(memory[i][0].split())[2][1]))
            ans+="{:03b}".format(int(list(memory[i][0].split())[3][1]))
            print(ans)
        else:
            print("ERROR: Not correct arguments for bitwise OR")       


    elif list(inp[0].split())[0] == "xor":
        if len(list(memory[i][0].split()))==4:
            ans+=opcodes["xor"]+"00"
            ans+="{:03b}".format(int(list(memory[i][0].split())[1][1]))
            ans+="{:03b}".format(int(list(memory[i][0].split())[2][1]))
            ans+="{:03b}".format(int(list(memory[i][0].split())[3][1]))
            print(ans)
        else:
            print("ERROR: Not correct arguments for bitwise XOR")


    elif list(inp[0].split())[0] == "mov":
        if inp[0].split()[2][0] == "$":
            if int(inp[0].split()[1][1:]) not in range(7):
                print("ERROR: Wrong argument for register")
                break
            if len(list(inp[0].split()))==3:
                    ans+=opcodes["mov_imm"]
                    ans+="{:03b}".format(int(inp[0].split()[1][1]))
                    ans+="{:08b}".format(int(inp[0].split()[2][1:]))
                    print(ans)
            else:
                    print("ERROR: Not correct arguments for mov")

        elif inp[0].split()[2][0] == "R":
            if int(inp[0].split()[1][1:]) not in range(7) or int(inp[0].split()[2][1:]) not in range(7):
                print("ERROR: Wrong argument for register")
                break

            if len(list(memory[i][0].split()))==3:
                    ans+=opcodes["mov_reg"]+"0"*5
                    ans+="{:03b}".format(int(inp[0].split()[1][1]))
                    ans+="{:03b}".format(int(inp[0].split()[2][1]))
                    print(ans)
            else:
                    print("ERROR: Not correct arguments for mov")
        else:
            print("ERROR: Invalid 2nd argument")


    elif list(inp[0].split())[0] == "ld":
        if len(inp[0].split()[2]) != 8 or set(inp[0].split()[2]) != {'0','1'}:
            print("ERROR: Invalid Memory Address")
            break
        if int(inp[0].split()[1][1:]) not in range(7) :
            print("ERROR: Wrong argument for register")
            break
        if len(list(inp[0].split()))==3:
            ans+=opcodes["ld"]
            ans+="{:03b}".format(int(inp[0].split()[1][1]))
            ans += inp[0].split()[2]
            print(ans)
        else:
            print("ERROR: Not correct arguments for sub")


    elif list(inp[0].split())[0] == "st":
        if len(inp[0].split()[2]) != 8 or set(inp[0].split()[2]) != {'0','1'}:
            print("ERROR: Invalid Memory Address")
            break
        if int(inp[0].split()[1][1:]) not in range(7):
            print("ERROR: Wrong argument for register")
            break
        if len(list(inp[0].split()))==3:
            ans+=opcodes["st"]
            ans+="{:03b}".format(int(inp[0].split()[1][1]))
            ans += inp[0].split()[2]
            print(ans)
        else:
            print("ERROR: Not correct arguments for sub")


    elif list(inp[0].split())[0] == "rs":
        if int(inp[0].split()[1][1:]) not in range(7):
            print("ERROR: Wrong argument for register")
            break
        if len(list(inp[0].split()))==3:
                ans+=opcodes["mov_imm"]
                ans+="{:03b}".format(int(inp[0].split()[1][1]))
                ans+="{:08b}".format(int(inp[0].split()[2][1:]))
                print(ans)
        else:
                print("ERROR: Not correct arguments for rs")


    elif list(inp[0].split())[0] == "ls":
        if int(inp[0].split()[1][1:]) not in range(7):
            print("ERROR: Wrong argument for register")
            break
        if len(list(inp[0].split()))==3:
                ans+=opcodes["mov_imm"]
                ans+="{:03b}".format(int(inp[0].split()[1][1]))
                ans+="{:08b}".format(int(inp[0].split()[2][1:]))
                print(ans)
        else:
                print("ERROR: Not correct arguments for ls")


#     elif list(inp[0].split())[0] == "jmp":
#         if len(inp[0].split()[1]) != 8 or set(inp[0].split()[1]) != {'0','1'}:
#             print("ERROR: Invalid Memory Address")
#             break
#         if len(list(inp[0].split()))==3:
#             ans+=opcodes["jmp"]+"0"*3
#             ans += inp[0].split()[1]
#             print(ans)
#         else:
#             print("ERROR: Not correct arguments for jmp")
    elif list(inp[0].split())[0] == "jmp":
        tempp = list(inp[0].split())[1]
        if len(list(inp[0].split()))==2:
            maddr=-1
            for j in memory.keys():
                if list(memory[j][0].split())[0][0:-1]==tempp:
                    maddr=j
            if maddr==-1:
                print("label not found")
                continue
            ans+=opcodes["jmp"]+"0"*3
            ans +="{:08b}".format(maddr)
            print(ans)
        else:
            print("ERROR: Not correct arguments for jmp")            


    elif list(inp[0].split())[0] == "jlt":
        if len(inp[0].split()[1]) != 8 or set(inp[0].split()[1]) != {'0','1'}:
            print("ERROR: Invalid Memory Address")
            break
        if len(list(inp[0].split()))==3:
            ans+=opcodes["jlt"]+"0"*3
            ans += inp[0].split()[1]
            print(ans)
        else:
            print("ERROR: Not correct arguments for jlt")


    elif list(inp[0].split())[0] == "jg":
        if len(inp[0].split()[1]) != 8 or set(inp[0].split()[1]) != {'0','1'}:
            print("ERROR: Invalid Memory Address")
            break
        if len(list(inp[0].split()))==3:
            ans+=opcodes["jg"]+"0"*3
            ans += inp[0].split()[1]
            print(ans)
        else:
            print("ERROR: Not correct arguments for jg")


    elif list(inp[0].split())[0] == "je":
        if len(inp[0].split()[1]) != 8 or set(inp[0].split()[1]) != {'0','1'}:
            print("ERROR: Invalid Memory Address")
            break
        if len(list(inp[0].split()))==3:
            ans+=opcodes["je"]+"0"*3
            ans += inp[0].split()[1]
            print(ans)
        else:
            print("ERROR: Not correct arguments for je")
            

    elif list(inp[0].split())[0] == "hlt":
        ans+=opcodes["hlt"]+"0"*11
        print(ans)
