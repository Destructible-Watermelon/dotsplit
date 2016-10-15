#initial parts. This will be the least extended part,
#but I imagine stuff will be added for some language features
stack=[]
program=[i.lower() for i in input().split()]
pop=lambda:stack.pop() if stack else 0
# commands that can't be lambdas
def hop():
    global i
    if pop():
        i+=1
def skip():
    global i; i+=1
def jump():
    global i; i-=pop()+1
commands={
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
    }
i=0
while i<len(program):
    commands.get(program[i], lambda:None)()
    i+=1
if stack:print(' '.join(str(i) for i in stack))