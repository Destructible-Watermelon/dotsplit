#initial parts. This will be the least extended part,
#but I imagine stuff will be added for some language features
from stack import Stack
stack = Stack([])
program=[i for i in input().split()]
# commands that can't be lambdas
tape,tape_index=[0],0
def hop():
	global i
	if stack.pop():
		i += 1

def skip():
	global i; i += 1

def jump():
	global i; i -= stack.pop()+1

def quote():
	global i; i += 1
	print(program[i], end='')

def delete():
    del program[i]

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
<<<<<<< HEAD
    "five":          lambda: stack.append(5),
    "five-negative": lambda: stack.append(-5),
    "five-unary":    lambda: (stack.append(0)for i in range(5)),
    "divide":        lambda: stack.append(pop()//pop()),
    "add":           lambda: stack.append(pop()+pop()),
    "derp":          lambda: print("Derp" if input()=="derp" else "Nope"),
    "derp-nocase":   lambda: print("Derp" if input().lower()=="derp" else "Nope"),
    "jump":          jump,
    "skip":          skip,
    "hop":           hop,
    "quote":         quote,
    "spaced-out":    lambda: print(" ", end=""),
    "newline":       lambda: print(),
    "delete":        delete,
    "tape-right":    tape_right,
    "tape-left":     tape_left,
    }
i=0
while i<len(program):
    commands.get(program[i].lower(), lambda:None)()
    i+=1
if stack:print(' '.join(str(i) for i in stack))
=======
	"five":          lambda: stack.append(5),
	"five-negative": lambda: stack.append(-5),
	"five-unary":    lambda: (stack.append(0)for i in range(5)),
	"divide":        lambda: stack.append(pop()//pop()),
	"add":           lambda: stack.append(pop()+pop()),
	"derp":          lambda: print("Derp" if input() == "derp" else "Nope"),
	"derp-nocase":   lambda: print("Derp" if input().lower() == "derp" else "Nope"),
	"jump":          jump,
	"skip":          skip,
	"hop":           hop,
	"quote":         quote,
	"spaced-out":    lambda: print(" ", end=""),
	"newline":       lambda: print(),
	}

i = 0
while i < len(program):
	commands.get(program[i].lower(), lambda:None)()
	i += 1

if stack:
	print(' '.join(str(i) for i in stack))
>>>>>>> 98239ccad131ec4d3fbdbf8827abab4c730daf80
