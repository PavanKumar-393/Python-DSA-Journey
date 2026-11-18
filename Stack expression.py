
"""Expression
│      ├── Infix → Postfix
│      ├── Postfix Evaluation
│      ├── Reverse Polish Notation
│      ├── Basic Calculator
│      └── Basic Calculator II
│"""

# Infix → Postfix===================================================




exp= input("enter infix expression ")

stack=[]
output= ""

precedence= {
    "+" : 1,
    "-" : 1,
    "*" : 2,
    "/" : 2,
    "^" : 3

}

for ch in exp:
    if ch.isalnum():
        output += ch

    elif ch == "(":
        stack.append(ch)

    elif ch == ")":
        while stack and stack[-1] != "(":
            output +=stack.pop()
        stack.pop()
    else:
        while (stack and stack[-1] != "(" and 
              precedence[stack[-1]]>= precedence[ch]):

            output += stack.pop()
        stack.append(ch)
while stack:
    output +=stack.pop()
print(output)


# postfix Evalution==========================================

postfix= input("enter postfix expression:").split()
                                         # 2 3 4 * +
stack=[]  # 2 3 4

for i in postfix:
    if i.isdigit():
        stack.append(int(i))

    else:
        b= stack.pop()  #4
        a= stack.pop()   # 3

        if i== "+":
            stack.append(a+b)
        elif i== "-":
            stack.append(a-b)
        elif i== "*":
            stack.append(a*b)
        elif i== "/":
            stack.append(a/b)
print(stack.pop())

# Reverse Polish Notation  == it is another name of post fix expression.
# adavantage of this is no need parentheses


postfix= input().split()

stack= []

for i in postfix:
    if i.isdigit():
        stack.append(int(i))

    else:
        b= stack.pop()
        a.stack.pop()


        if i == "+":
            stack.append(a+b)
        elif i == "-":
            stack.append(a-b)
        elif i== "*":
            stack.append(a*b)
        elif i == "/":
            stack.append(a/b)

print(stack.pop())