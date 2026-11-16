#Reverse a string
#Check palindrome
#Check anagram
#Count vowels and consonants
#Count character frequency


# 1. Reverse a string======================================
'''
str= input("Enter a string: ")

reverse_str= str[::-1]

print(reverse_str)

# using loop======
str= input("Enter a string: ")

reverse=" "
for i in str:
    reverse= i+ reverse 

print(reverse)
'''

# 2. Check palindrome====================================
'''
str= input("enter a string: ")

if str==str[::-1]:
    print("palindrome")
else:
    print("not palindrome")


# without using slicing======

str= input("eneter a string")  # madam

left=0  # 1, 
right=len(str)-1 # 4, 3

while left< right:   # 0<4, 1<3 
    if str[left] != str[right]: # m != m  flase
        print("not a palindrome")
        break
    left +=1      # left becomes 1, 2
    right -=1     # rgiht becomes 3, 2
else:
    print("palindrome")
'''

# 3. Check anagram==================================
'''
str1= input("eneter str1 :")
str2= input("eneter str2 :")

if sorted(str1)==sorted(str2):
    print("anagram")
else:
    print("not anagram")

'''

# 4. Vowel and consonent counter================================

text = input("Enter a string: ")

vowels = "aeiouAEIOU"

vowel_count = 0
consonant_count = 0
digit_count = 0
space_count = 0
special_count = 0

for ch in text:
    
    if ch in vowels:
        vowel_count += 1
    elif ch not in vowels and ch.isalpha():
        consonant_count += 1
    elif ch.isdigit():
        digit_count += 1
    elif ch.isspace():
        space_count += 1
    else:
        special_count += 1

print("Vowels            :", vowel_count)
print("Consonants        :", consonant_count)
print("Digits            :", digit_count)
print("Spaces            :", space_count)
print("Special Characters:", special_count)

## 5. Count character frequency=============================

str= input("enter a string: ")
freq= {}

for i in str:
    if i in freq:
        freq[i] +=1
    else:
        freq[i] =1

for key,value in freq.items():
    print(key, ":",value)




    