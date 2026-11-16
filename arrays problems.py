# Print array elements=================
arr1=[1,2,3,4,5,6,7]
for i in arr1:
    print(i)


# sum of array================================
arr1=[1,2,3,4,5,6,7,8]
sum=0
for i in arr1:
    sum+=i
print(sum)

# sum of array using index=======
arr1=[1,2,3,4,5,6,7,8]
sum=0
for i in range(len(arr1)):
    sum+=arr1[i]

print(sum)

# Taking user input=================

arr = list(map(int, input("Enter numbers: ").split()))

total = 0

for num in arr:
    total += num

print("Sum of array:", total)




# 3. Largest element in array=========================================
arr1= [1,2,3,7,6,6,6,66,5,54,90]
largest=0
for i in arr1:
    if i==max(arr1):
        largest+=i
print(largest)

# user input
'''
arr1= list(map(int,input().split()))
largest= 0


for i in arr1:
    if i> largest:
        largest = i
print(largest)
'''

# 4. Smallest element=========================================================

'''
list1= list(map(int,input().split()))
smallest=0

for i in list1:
    if i<= smallest:
        smallest =i
print(smallest)
'''
# 5. Second largest element in array ================================

arr= list(map(int,input("enter elements:" ).split()))

largest= float('-inf')
second= float('-inf')

for i in arr:
    if i > largest:
        second = largest
        largest= i
    elif i> second and i != largest:
        second= i

if second ==float('-inf'):
    print("second largest does not exist")
else:
    print("largest number is ", second)


 # 6.Reverse array ============================================
arr1= input().split()
a= arr1[::-1]
print(a)

arr1= list(map(int,input().split()))
arr1.reverse()
print(arr1)
    





