#Find the average of array elements.
#Count even and odd numbers.
#Find the maximum and minimum elements.
#Search an element (linear search).
#Perform binary search.



#1. average of array elements====================================
'''
arr= list(map(int,input().split()))
total=0

for num in arr:
    total += num
print("average", total/len(arr))

#2. count even and odd elements.=============================
arr= list(map(int,input().split()))
odd=0
even=0

for i in arr:
    if i %2==0:
        even+=1
    else:
        odd+=1

print("total odd numbers " ,odd)
print(" total even numbers", even)

'''
#3.Find the maximum and minimum elements.=============================
'''arr=list(map(int,input().split()))
maximum=0
minimum=1

for i in arr:
    if i> maximum:
        maximum= i

    if i< minimum:
        minimum= i

print("maximum element",maximum)
print("minimum element", minimum)
'''

# 4. linear search in array==============================
'''arr= list(map(int,input().split()))
search=int(input())

for i in arr:
    if i == search:
        print("linear search is ",i )
else:
    print(" number not found")
'''
'''
arr = list(map(int,input().split()))
search= int(input("enter number"))

for i in range(len(arr)):
    if arr[i]== search:
        print("element is ", i)
        break
else:
    print("element not found")
'''

arr= list(map(int,input(" enter array elements: ").split()))
key= int(input("enetr element to search: "))
# 10 20 30 40 50 60 70
low=0
high= len(arr)-1  #6

while low<= high: # 0<=6 , 
    mid = (low+high)//2  # (0+6)//2 = 3, 

    if arr[mid] == key: # 30==50 false 
        print("element found at index",mid)
        break

    elif arr[mid]<key:  # 30<50
        low = mid+1     # 3+1=4 moved to right half
    else:
        high= mid-1 

if low > high:
    print("element not found")




