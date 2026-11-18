
# check balanced parenthesess===============================
'''s= input("enter brackets: ")

stack=[]

pairs= {
    ')':'(',
    ']':'[',
    '}':'{'
}

for i in s:
    if i in "([{":
        stack.append(i)

    else:
        if not stack:
            print(False)
            break

        if stack[-1]==pairs[i]:
            stack.pop()

        else:
            print(False)
            break
else:
    if not stack:
        print(True)
    else:
        print(False)
'''

# # Min stack==================================================
'''
class Minstack:
    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, x):
        self.stack.append(x)

        if not self.min_stack:
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
    
    def top(self):
        return self.stack[-1]
    def getmin(self):
        return self.min_stack[-1]

ms= Minstack()
ms.push(10)
ms.push(20)
ms.push(5)
ms.push(30)

print(ms.stack)
print(ms.min_stack)

print(ms.top())
print(ms.getmin())
ms.pop()
print(ms.top)
print(ms.getmin())

'''
# Asteroid collision========================================
class solution:
    def Asteroidcollision(self,asteroids):

        stack=[]

        for asteroid in asteroids:
            while stack and stack[-1] >0 and asteroid <0:

                if stack[-1]< -asteroid:
                    stack.pop()
                elif stack[-1]== -asteroid:
                    stack.pop()
                    break 
                else:
                    break
            else:
                stack.append(asteroid)
        return stack

obj=  solution()
asteroids= list(map(int,input("eneter asteroid: " ).split()))
result= obj.Asteroidcollision(asteroids)
print(result)