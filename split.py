#initial parts. This will be the least extended part,
#but I imagine stuff will be added for some language features
stack=[]
program=[i.lower() for i in input().split()]
pop=lambda:stack.pop() if stack else 0
for command in program: #the part that will be the most extended
    {
        "five":         lambda: stack.append(5),
        "divide":       lambda: stack.append(pop()//pop()),
        "add":          lambda: stack.append(pop()+pop()),
        "derp":         lambda: print("Derp" if input()=="derp" else "Nope"),
        "derp-nocase":  lambda: print("Derp" if input().lower()=="derp" else "Nope"),
    }.get(command, lambda:None)()
print(' '.join(str(i) for i in stack))