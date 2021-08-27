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
error2=0
hlt_counter=0

var_start=1
cc=0
for line in temp:
    line = str(line)
    if not line or line.isspace():
        continue
    cc+=1
    lis = line.split()
    if hlt_counter>0:
        error=1 
    if lis[0] in operators:
        memory[memory_counter]=[line, "operator"]
        memory_counter+=1
    elif lis[0]=="var":
        if var_start!=cc:
            error2=1
            print("Variable at Line {} not declared at the beginning".format(cc))
            break
        var_start+=1
        queue.append(line)
    elif lis[0][-1]==":":
        memory[memory_counter]=[" ".join(lis[1:]) ,"label", lis[0][:-1]]
        if(not lis[1:]):
            error2=1
            print("Invalid instruction in Line {}".format(memory_counter+1+(var_start-1)))
            break
        if len(lis)>1 and lis[1]=="hlt":
            hlt_counter+=1
        memory_counter+=1

    elif lis[0]=="hlt":
        memory[memory_counter]=[line,"halt"]
        memory_counter+=1
        hlt_counter+=1
    else:
        memory[memory_counter]=[line]
        memory_counter+=1   

if hlt_counter==0:
    print("Missing hlt instruction")
    error2=1

if hlt_counter>1:
    print("hlt not being used as the last instruction")
    error2=1

if memory_counter>256:
    error=1
    error2=1
    print("Memory error")

for i in queue:
    memory[memory_counter] =  [i, "variable"]
    memory_counter+=1

big_ans = []



for i in memory.keys():
    key_count = i
    ans=""
    inp = memory[i]
    index = 0
    if(not inp[0]):
        continue
    if list(inp[0].split())[index] != "mov":
        for k in list(memory[i][0].split()[1:]):
            if k=="flags" or k=="FLAGS":
                print("Illegal use of FLAGS")
                error2=1
    if(error ==1 or error2 ==1):
        break
    

    if list(inp[0].split())[index] == "add":
       
        f = 0
        for k in range(1,4):
            try:
                reg_val = int(inp[0].split()[k][1:])
                if reg_val not in range(7) or inp[0].split()[k][0]!='R':
                    print("Typos in register name at line {}".format(key_count+var_start))
                    error2=1    
                    f = 1
                    break
            except:
                print("Typos in register name at line {}".format(key_count+var_start))
                error2=1
                f=1
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
            print("Wrong syntax used for add instruction at line {}".format(key_count+var_start))
            error2=1


    elif list(inp[0].split())[index] == "sub":
        f = 0
        for i in range(1,4):
            try:
                reg_val = int(inp[0].split()[i][1:])
                if reg_val not in range(7) or inp[0].split()[i][0]!='R':
                    print("Typos in register name at line {}".format(key_count+var_start))
                    error2 =1
                    f = 1
                    break
            except:
                print("Typos in register name at line {}".format(key_count+var_start))
                error2=1
                f=1
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
            print("Wrong syntax used for sub instruction at line {}".format(key_count+var_start))
            error2=1

    elif list(inp[0].split())[index] == "mul":
        f = 0
        for j in range(1,4):
            try:
                reg_val = int(inp[0].split()[j][1:])
                if reg_val not in range(7) or inp[0].split()[j][0]!='R':
                    print("Typos in register name at line {}".format(key_count+var_start))
                    error2 =1
                    f = 1
                    break
            except:
                print("Typos in register name at line {}".format(key_count+var_start))
                error2=1
                f=1
                break
        if f == 1:
            break
        if len(list(memory[i][0].split()))==4:
            ans+=opcodes["mul"]+"00"
            ans+="{:03b}".format(int(inp[0].split()[1][1]))
            ans+="{:03b}".format(int(inp[0].split()[2][1]))
            ans+="{:03b}".format(int(inp[0].split()[3][1]))
            big_ans.append(ans)
        else:
            print("Wrong syntax used for mul instruction at line {}".format(key_count+var_start))
            error2=1


    elif list(inp[0].split())[index] == "div":
        f = 0
        for i in range(1,3):
            try:
                reg_val = int(inp[0].split()[i][1:])
                if reg_val not in range(7) or inp[0].split()[i][0]!='R':
                    print("Typos in register name at line {}".format(key_count+var_start))
                    error2 =1
                    f = 1
                    break
            except:
                print("Typos in register name at line {}".format(key_count+var_start))
                error2=1
                f=1
                break
        if f == 1:
            break
        if len(list(memory[i][0].split()))==3:
            ans+=opcodes["div"]+"00000"
            ans+="{:03b}".format(int(inp[0].split()[1][1]))
            ans+="{:03b}".format(int(inp[0].split()[2][1]))
            big_ans.append(ans)
        else:
            print("Wrong syntax used for div instruction at line {}".format(key_count+var_start))
            error2=1


    elif list(inp[0].split())[index] == "not":
        f = 0
        for i in range(1,3):
            try:
                reg_val = int(inp[0].split()[i][1:])
                if reg_val not in range(7) or inp[0].split()[i][0]!='R':
                    print("Typos in register name at line {}".format(key_count+var_start))
                    error2 =1
                    f = 1
                    break
            except:
                print("Typos in register name at line {}".format(key_count+var_start))
                error2=1
                f=1
                break
        if f == 1:
            break
        if len(list(memory[i][0].split()))==3:
            ans+=opcodes["not"]+"00000"
            ans+="{:03b}".format(int(inp[0].split()[1][1]))
            ans+="{:03b}".format(int(inp[0].split()[2][1]))
            big_ans.append(ans)
        else:
            print("Wrong syntax used for NOT instruction")
            error2=1
    elif list(inp[0].split())[index] == "cmp":
        f = 0
        for k in range(1,3):
            try:
                reg_val = int(inp[0].split()[k][1:])
                if reg_val not in range(7) or inp[0].split()[k][0]!='R':
                    print("Typos in register name at line {}".format(key_count+var_start))
                    error2 =1
                    f = 1
                    break
            except:
                print("Typos in register name at line {}".format(key_count+var_start))
                error2=1
                f=1
                break
        if f == 1:
            break
        
        if len(list(memory[i][0].split()))==3:
            ans+=opcodes["cmp"]+"00000"
            ans+="{:03b}".format(int(inp[0].split()[1][1]))
            ans+="{:03b}".format(int(inp[0].split()[2][1]))
            big_ans.append(ans)
        else:
            print("Wrong syntax used for CMP instruction at line {}".format(key_count+var_start))
            error2=1   


    elif list(inp[0].split())[index] == "and":
        f = 0
        for i in range(1,3):
            try:
                reg_val = int(inp[0].split()[i][1:])
                if reg_val not in range(7) or inp[0].split()[i][0]!='R':
                    print("Typos in register name at line {}".format(key_count+var_start))
                    error2 =1
                    f = 1
                    break
            except:
                print("Typos in register name at line {}".format(key_count+var_start))
                error2=1
                f=1
                break
        if f == 1:
            break
        if len(list(memory[i][0].split()))==4:
            ans+=opcodes["and"]+"00"
            ans+="{:03b}".format(int(inp[0].split()[1][1]))
            ans+="{:03b}".format(int(inp[0].split()[2][1]))
            ans+="{:03b}".format(int(inp[0].split()[3][1]))
            big_ans.append(ans)
        else:
            print("Wrong syntax used for AND instruction at line {}".format(key_count+var_start))
            error2=1


    elif list(inp[0].split())[index] == "or":
        f = 0
        for i in range(1,3):
            try:
                reg_val = int(inp[0].split()[i][1:])
                if reg_val not in range(7) or inp[0].split()[i][0]!='R':
                    print("Typos in register name at line {}".format(key_count+var_start))
                    error2 =1
                    f = 1
                    break
            except:
                print("Typos in register name at line {}".format(key_count+var_start))
                error2=1
                f=1
                break
        if f == 1:
            break
        if len(list(memory[i][0].split()))==4:
            ans+=opcodes["or"]+"00"
            ans+="{:03b}".format(int(inp[0].split()[1][1]))
            ans+="{:03b}".format(int(inp[0].split()[2][1]))
            ans+="{:03b}".format(int(inp[0].split()[3][1]))
            big_ans.append(ans)
        else:
            print("Wrong syntax used for OR instruction at line {}".format(key_count+var_start))  
            error2=1     


    elif list(inp[0].split())[index] == "xor":
        f = 0
        for i in range(1,3):
            try:
                reg_val = int(inp[0].split()[i][1:])
                if reg_val not in range(7) or inp[0].split()[i][0]!='R':
                    print("Typos in register name at line {}".format(key_count+var_start))
                    error2 =1
                    f = 1
                    break
            except:
                print("Typos in register name at line {}".format(key_count+var_start))
                error2=1
                f=1
                break
        if f == 1:
            break
        if len(list(memory[i][0].split()))==4:
            ans+=opcodes["xor"]+"00"
            ans+="{:03b}".format(int(inp[0].split()[1][1]))
            ans+="{:03b}".format(int(inp[0].split()[2][1]))
            ans+="{:03b}".format(int(inp[0].split()[3][1]))
            big_ans.append(ans)
        else:
            print("Wrong syntax used for XOR instruction at line {}".format(key_count+var_start))
            error2=1


    elif list(inp[0].split())[index] == "mov":
        if inp[0].split()[2][0] == "$":
            try:
                if inp[0].split()[1][0]!='R' or int(inp[0].split()[1][1:]) not in range(7):
                    print("Typos in register name at line {}".format(key_count+var_start))
                    error2=1
                    break
            except:
                print("Typos in register name at line {}".format(key_count+var_start))
                error2=1
                break
            if len(list(inp[0].split()))==3:
                    if(int(inp[0].split()[2][1:])<0 or int(inp[0].split()[2][1:])>255):
                        print("Illegal Immediate value at line {}".format(key_count+var_start))
                        error2=1
                        break
                    ans+=opcodes["mov_imm"]
                    ans+="{:03b}".format(int(inp[0].split()[1][1]))
                    ans+="{:08b}".format(int(inp[0].split()[2][1:]))
                    big_ans.append(ans)
            else:
                    print("Wrong syntax used for MOV instruction at line {}".format(key_count+var_start))

        elif inp[0].split()[2][0] == "R":
            try:
                if inp[0].split()[1][0]!='R' or inp[0].split()[2][0]!='R' or int(inp[0].split()[1][1:]) not in range(7) or int(inp[0].split()[2][1:]) not in range(7):
                    print("Typos in register name at line {}".format(key_count+var_start))
                    error2=1
                    break
            except:
                print("Typos in register name at line {}".format(key_count+var_start))
                error2=1
                break

            if len(list(memory[i][0].split()))==3:
                    ans+=opcodes["mov_reg"]+"0"*5
                    ans+="{:03b}".format(int(inp[0].split()[1][1]))
                    ans+="{:03b}".format(int(inp[0].split()[2][1]))
                    big_ans.append(ans)
            else:
                    print("Wrong syntax used for MOV instruction at line {}".format(key_count+var_start))
                    error2=1
        elif inp[0].split()[2] == "FLAGS":
            try:
                if inp[0].split()[1][0]!='R' or int(inp[0].split()[1][1:]) not in range(7):
                    print("Typos in register name at line {}".format(key_count+var_start))
                    error2=1
                    break
            except:
                print("Typos in register name at line {}".format(key_count+var_start))
                error2=1
                break
            ans+=opcodes["mov_reg"]+"0"*5
            ans+="{:03b}".format(int(inp[0].split()[1][1]))
            ans+="111"
            big_ans.append(ans)
        else:
            print("Wrong syntax used for MOV instruction at line {}".format(key_count+var_start))
            error2=1


    elif list(inp[0].split())[index] == "ld":
        try:
            if len((list(inp[0].split())))!=3 or inp[0].split()[1][0]!='R' or int(inp[0].split()[1][1:]) not in range(7):
                print("Typos in register name at line {}".format(key_count+var_start))
                error2=1
        except:
            print("Typos in register name at line {}".format(key_count+var_start))
            error2=1
            break
        ans+=opcodes["ld"]
        ans+="{:03b}".format(int(inp[0].split()[1][1]))
        found = 0
        for j in memory.keys():
            if memory[j][1]=="variable" and memory[j][0].split()[1]==inp[0].split()[2]:
                found=1
                ans+="{:08b}".format(j)
        if found ==0:
            print("Use of undefined variables at line {}".format(key_count+var_start))
            error2=1
        big_ans.append(ans)


    elif list(inp[0].split())[index] == "st":
        try:
            if len((list(inp[0].split())))!=3 or inp[0].split()[1][0]!='R' or int(inp[0].split()[1][1:]) not in range(7):
                print("Typos in register name at line {}".format(key_count+var_start))
                error2=1
        except:
            print("Typos in register name at line {}".format(key_count+var_start))
            error2=1
            break
        ans+=opcodes["st"]
        ans+="{:03b}".format(int(inp[0].split()[1][1]))
        found=0
        for j in memory.keys():
            if memory[j][1]=="variable" and memory[j][0].split()[1]==inp[0].split()[2]:
                found=1
                ans+="{:08b}".format(j)
        if found ==0:
            print("Use of undefined variables at line {}".format(key_count+var_start))
            error2=1
        big_ans.append(ans)


    elif list(inp[0].split())[index] == "rs":
        try:
            if int(inp[0].split()[1][1:]) not in range(7) or inp[0].split()[1][0]!='R':
                print("Typos in register name at line {}".format(key_count+var_start))
                error2=1
                break
        except:
            print("Typos in register name at line {}".format(key_count+var_start))
            error2=1
            break
        if len(list(inp[0].split()))==3:
                if(int(inp[0].split()[2][1:])<0 or int(inp[0].split()[2][1:])>255):
                    print("Illegal Immediate value at line {}".format(key_count+var_start))
                    error2=1
                    break
                ans+=opcodes["rs"]
                ans+="{:03b}".format(int(inp[0].split()[1][1]))
                ans+="{:08b}".format(int(inp[0].split()[2][1:]))
                big_ans.append(ans)
        else:
                print("Wrong syntax used for RS instruction at line {}".format(key_count+var_start))
                error2=1


    elif list(inp[0].split())[index] == "ls":
        try:
            if int(inp[0].split()[1][1:]) not in range(7) or inp[0].split()[1][0]!='R':
                print("Typos in register name at line {}".format(key_count+var_start))
                error2=1
                break
        except:
            print("Typos in register name at line {}".format(key_count+var_start))
            error2=1
            break
        if len(list(inp[0].split()))==3:
                if(int(inp[0].split()[2][1:])<0 or int(inp[0].split()[2][1:])>255):
                    print("Illegal Immediate value at line {}".format(key_count+var_start))
                    error2=1
                    break
                ans+=opcodes["ls"]
                ans+="{:03b}".format(int(inp[0].split()[1][1]))
                ans+="{:08b}".format(int(inp[0].split()[2][1:]))
                big_ans.append(ans)
        else:
                print("Wrong syntax used for LS instruction at line {}".format(key_count+var_start))
                error2=1


    elif list(inp[0].split())[index] == "jmp":
        tempp = list(inp[0].split())[1]
        if len(list(inp[0].split()))==2:
            maddr=-1
            for j in memory.keys():
                if (memory[j][1]=="label" and memory[j][2]==tempp) or '{:08b}'.format(j) == tempp:
                    maddr = j
            if maddr==-1:
                print("Use of undefined labels at line {}".format(key_count+var_start))
                error2=1
                continue
            ans+=opcodes["jmp"]+"0"*3
            ans +="{:08b}".format(maddr)
            big_ans.append(ans)
        else:
            print("Wrong syntax used for jmp instruction at line {}".format(key_count+var_start))            
            error2=1
    elif list(inp[0].split())[index] == "jlt":
        tempp = list(inp[0].split())[1]
        if len(list(inp[0].split()))==2:
            maddr=-1
            for j in memory.keys():
                if memory[j][1]=="label" and memory[j][2]==tempp:
                    maddr = j
            if maddr==-1:
                print("Use of undefined labels at line {}".format(key_count+var_start))
                error2=1
                continue
            ans+=opcodes["jlt"]+"0"*3
            ans +="{:08b}".format(maddr)
            big_ans.append(ans)
        else:
            print("Wrong syntax used for jlt instruction at line {}".format(key_count+var_start))
            error2=1
    elif list(inp[0].split())[index] == "jgt":
        tempp = list(inp[0].split())[1]
        if len(list(inp[0].split()))==2:
            maddr=-1
            for j in memory.keys():
                if memory[j][1]=="label" and memory[j][2]==tempp:
                    maddr = j
            if maddr==-1:
                print("Use of undefined labels at line {}".format(key_count+var_start))
                error2=1
                continue
            ans+=opcodes["jgt"]+"0"*3
            ans +="{:08b}".format(maddr)
            big_ans.append(ans)
        else:
            print("Wrong syntax used for jgt instruction at line {}".format(key_count+var_start))     
            error2=1         

    elif list(inp[0].split())[index] == "je":
        tempp = list(inp[0].split())[1]
        if len(list(inp[0].split()))==2:
            maddr=-1
            for j in memory.keys():
                if memory[j][1]=="label" and memory[j][2]==tempp:
                    maddr = j
            if maddr==-1:
                print("Use of undefined labels at line {}".format(key_count+var_start))
                error2=1
                continue
            ans+=opcodes["je"]+"0"*3
            ans +="{:08b}".format(maddr)
            big_ans.append(ans)
        else:
            print("Wrong syntax used for je instruction at line {} ".format(key_count+var_start))
            error2=1

    elif list(inp[0].split())[index] == "hlt":
        ans+=opcodes["hlt"]+"0"*11
        big_ans.append(ans)
    
    elif list(inp[0].split())[index] == "var":
        pass
    else:
        print("Typo in instruction name at line {}".format(key_count+var_start))
        error2=1
        break
    

if(error!=1 and error2!=1):
    for line in big_ans:
        print(line)
