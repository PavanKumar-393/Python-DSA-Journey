"""'''stack=[]
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

#stack.pop()
#stack.pop()
#print(stack)

# peek
print(stack[-1])
'''

# Full  satck implementation=============================
class stack:
    def __init__(self):
        self.stack= []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.stack:
            print("stack underflow")
            return
        return self.stack.pop()
    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]
    def is_empty(self):
        return len(self.stack)==0

    def display (self):
        print(self.stack)

s= stack()
s.push(10)
s.push(20)
s.push(30)

s.display()
print(s.pop())
print(s.peek())
print(s.is_empty())
s.display()

"""

# Reverse a string in stack====================================
str1="pavan kumar"
stack= []
for i in str1:
    stack.append(i)

reverse = ""
while stack:
    reverse +=stack.pop()

print("reversed string:", reverse)

# check balanced parenthesess===============================



s = input("Enter brackets: ") # ({[]})

stack = []

pairs = {
    ')': '(',
    '}': '{',
    ']': '['
}

balanced = True

for ch in s:

    if ch in "({[":
        stack.append(ch)

    elif ch in ")}]": 

        if not stack:
            balanced = False
            break

        top = stack.pop()

        if top != pairs[ch]:
            balanced = False
            break

if balanced and not stack:
    print("Balanced")
else:
    print("Not Balanced")

# Implementing Min stack=================================

class Minstack:

    def __init__(self):
        self.stack= []
        self.min_stack= []

    def push(self, x):
        self.stack.append(x)

        if not self.min_stack:
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(x, self.min_stack[-1]))
    def pop(self):  # remove top element=
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
    def top(self):
        return self.stack[-1]

    def getmin(self):
        return self.min_stack[-1]

# create object

ms= Minstack()
ms.push(5)
ms.push(2)
ms.push(8)
ms.push(1)

print(" main stack:", ms.stack)
print("min stack:", ms.min_stack)

print("top element:", ms.top())
print(" minimum element:", ms.getmin())

ms.pop()
print("\n after pop")

print("main stack", ms.stack)
print("min stack:", ms.min_stack)

print("top element:", ms.top())
print("minimum element:", ms.getmin())


# Evaluate a postfix expression.=====================================
postfix= input("enter postfix expression:").split()

stack=[]

for i in postfix:
    if i.isdigit():
        stack.append(int(i))

    else:
        b= stack.pop()
        a= stack.pop()

        if i== "+":
            stack.append(a+b)
        elif i== "-":
            stack.append(a-b)
        elif i== "*":
            stack.append(a*b)
        elif i== "/":
            stack.append(a/b)
print(stack.pop())

#Sort a stack using another stack=========================================

stack= [3,1,4,2]
temp_stack= []    # empty 

while stack: # true

    temp= stack.pop()  

    while temp_stack and temp_stack[-1] > temp:  # 
        stack.append(temp_stack.pop())
 
    temp_stack.append(temp) 

print('sorted stack:', temp_stack)