file = input('Type file name:')
with open(file, 'r', encoding='utf-8-sig') as f:
    f = f.read()

all_v = {}
line = 0
lines = f.split('\n')
lines = [l.strip() for l in lines if l.strip()]

def interpret_print():
    global line, lines, all_v
    if lines[line+1] == 'v':
        print(all_v[lines[line+2]])
    else:
        print(lines[line+2])

def interpret_input():
    global line, lines, all_v
    all_v[lines[line+1]] = input(lines[line+2])

for i in range(int(len(lines)/3)):
    if lines[line] == 'print':
        interpret_print()
    if lines[line] == 'input':
        interpret_input()
    line += 3
