#initial parts. This will be the least extended part,
#but I imagine stuff will be added for some language features
from stack import Stack
stack = Stack([])
tape=[0]
program=[i for i in input().split()]
# commands that can't be lambdas
def hop():
    global i
    if stack.pop():
        i += 1

def better_indents():
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))

    for subdir, dirs, files in os.walk(dir_path):
        for file in files:
            x=os.path.join(subdir, file)
            if x.endswith('.py'):
                filedata = None
                with open(x, 'r') as pyfile:
                    filedata = pyfile.read()

                # Replace the target string
                filedata = filedata.replace(chr(9), chr(32)*4)

                # Write the file out again
                with open(x, 'w') as pyfile:
                    pyfile.write(filedata)
def skip():
    global i; i += 1

def jump():
    global i; i -= stack.pop()+1

def quote():
    global i; i += 1
    print(program[i%len(program)], end='')

def delete():
    del program[i]

def delete_stay():
    delete()
    global i;i-=1

def tape_left():
    global tape_index
    if tape_index==0:
        tape.insert(0,0)
    else: tape_index-=1
def tape_right():
    global tape_index
    if tape_index==len(tape)-1:
        tape.append(0)
    tape_index+=1



commands={
    "five":          lambda: stack.push(5),
    "five-negative": lambda: stack.push(-5),
    "five-unary":    lambda: (stack.push(0)for i in range(5)),
    "divide":        lambda x=stack.pop(),y=stack.pop(): stack.push(x//y if y!=0 else 42),
    "add":           lambda: stack.push(stack.pop()+stack.pop()),
    "derp":          lambda: print("Derp" if input() == "derp" else "Nope"),
    "derp-nocase":   lambda: print("Derp" if input().lower() == "derp" else "Nope"),
    "jump":          jump,
    "skip":          skip,
    "hop":           hop,
    "quote":         quote,
    "spaced-out":    lambda: print(" ", end=""),
    "newline":       lambda: print(),
    "delete":        delete,
    "delete-stay":   delete_stay,
    "tape-right":    tape_right,
    "tape-left":     tape_left,
    "better-indents":better_indents,

    }

i = 0
while i < len(program):
    commands.get(program[i].lower(), lambda:None)()
    i += 1

if stack:
    print(' '.join(str(i) for i in stack))