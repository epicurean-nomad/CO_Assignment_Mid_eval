import sys
temp_l = []
temp_s = ""
complete_input = sys.stdin.read()

for char in complete_input:
    if char=='\n':
        temp_l.append(temp2)
        temp_s=""
    else:
        temp_s+=char
