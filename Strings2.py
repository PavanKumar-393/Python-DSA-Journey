#Remove duplicate characters
#First non-repeating character
#First repeating character
#Longest common prefix
#Reverse words in a sentence


#1. Remove duplicate characters=============================
'''
str= input("enter a string: ")
result=" "

for i in str:
    if  i not in result:
        result +=i

print(result)


str = input("enter a string: ")
seen= set()

result=""

for i in str:
    if i not in seen:
        seen.add(i)
        result +=i

print("string after removing duplicates ", result)

'''

# 2. First non-repeating character
'''
str= input("enter a string: ")

freq={}

for i in str:
    if i in freq:
        freq[i] +=1
    else:
        freq[i] =1

for i in str:
    if freq[i] ==1:
        print("First non-repeating character ", i)
        break
else:
    print("No non-repeating character found ")

'''

# First repeating element ====================================
str= input("enter a string: ")

seen= set()

for i in str:
    if i in seen:
        print("first repeating charecter:",i)
        break
    seen.add(i)
else:
    print("no repeating charaacter found")



#4. Longest common prefix========================================

str= input(" enter string separated by space: ").split()

prefix=str[0] # pavan 

for word in str[1:]:  # pavankumar
    while not word.startswith(prefix): # pavankumar.starswith(pavan)
        prefix = prefix[:-1]    
        if prefix == "": 
            break
if prefix =="":     
    print("longest common prefix is not there")
else:
    print("longest common prefix", prefix)



#Reverse words in a sentence====================================

str=input("enter a string :")

word= str.split()
words= word[::-1]

print(" ".join(words))

#Reverse Each Word (Not the Sentence===========
sentence = input("Enter a sentence: ")

words = sentence.split()

for word in words:
    print(word[::-1], end=" ")

