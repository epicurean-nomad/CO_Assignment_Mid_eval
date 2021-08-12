import sys

complete_input = sys.stdin.read()
//asdsadas
memory = {}
queue=[]
registers=[0,0,0,0,0,0,0]

operators=["add","sub","mov","ld", "st",
            "mul", "div", "rs", "ls","xor",
            "or", "and", "not","cmp", "jmp",
            "jlt", "jgt", "je", "hlt"]

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

for line in temp:
    line = str(line)
    if line=="":
        continue
    lis = line.split()
    if lis[0] in operators:
        memory[memory_counter]=line
        memory_counter+=1
    elif lis[0]=="var":
        queue.append(line)
    else:
        error = 0

if error!=-1 or (list(memory.values())[-1].split()[0])!="hlt" or (list(memory.values()).count("hlt"))>1:
    print("ERROR")
else:
    print("OK")

for i in queue:
    memory[memory_counter] =  i
    memory_counter+=1

for i in memory.keys():
    print(i, end=" ")
    print(memory[i])
