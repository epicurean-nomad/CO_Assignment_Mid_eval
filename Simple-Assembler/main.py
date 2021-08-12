import sys

complete_input = sys.stdin.read()

memory = {}
queue=[]
registers=[0,0,0,0,0,0,0]


opcodes = {
    "add": "00000",
    "sub": "00001",
    "mov": "00010",
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
    elif lis[0][-1]==":":
        memory[memory_counter]=[line, "label"]
        memory_counter+=1
    elif lis[0]=="hlt":
        memory[memory_counter]=[line,"halt"]
        memory_counter+=1
        hlt_counter+=1
    else:
        error = 0


if error!=-1 or list(memory.values())[-1][0].split()[0]!="hlt" or hlt_counter!=1:
    print("ERROR with hlt")
else:
    print("OK")

memory.values()

for i in queue:
    memory[memory_counter] =  [i, "variable"]
    memory_counter+=1

# x = "{:03b}".format(2)
# print(type(x))

for i in memory.keys():
    ans=""
    inp = memory[i]
    if list(inp[0].split())[0] == "add":
        if len(list(memory[i][0].split()))==4:
            ans+=opcodes["add"]+"00"
            ans+="{:03b}".format(int(list(memory[i][0].split())[1][1]))
            ans+="{:03b}".format(int(list(memory[i][0].split())[2][1]))
            ans+="{:03b}".format(int(list(memory[i][0].split())[3][1]))
            print(ans)
        else:
            print("ERROR: Not correct arguments for add")
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
