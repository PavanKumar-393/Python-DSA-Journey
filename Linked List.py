
class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None

head= Node(10)
second= Node(20)
third= Node(30)

head.next=second
second.next=third

# print
temp=head
while temp:
    print(temp.data, end="->")
    temp= temp.next
print("None")

# inserting at beginning ====================
"""new_node= Node(5)

new_node.next=head
head=new_node

temp=head
while temp:
    print(temp.data, end="->")
    temp= temp.next
print("None")"""

# inserting at end=============
'''
new_node=Node(40)

temp= head
while temp.next:
    temp=temp.next 
    

temp.next=new_node

print("none")

temp=head
while temp:
    print(temp.data, end="->")
    temp= temp.next
print("None")'''

# inserting at specific position====================
'''
new_node=Node(25)

key=20
temp=head
while temp.data != key:
    temp= temp.next

if temp.data==key:
    new_node.next=temp.next
    temp.next=new_node

temp=head
while temp:
    print(temp.data, end="->")
    temp= temp.next
print("None")'''



# remove at beginning==================
'''
head= head.next
temp=head
while temp:
    print(temp.data, end="->")
    temp= temp.next
print("None")
'''
# remove at end===================
'''
temp=head
while temp.next.next:
    temp= temp.next

temp.next= None

temp=head
while temp:
    print(temp.data, end="->")
    temp= temp.next
print("None")
'''


# Doubly  linked list===================================================

class Node:
    def __init__(self,data):
        self.prev= None
        self.data= data
        self.next= None

head=Node(10)
second=Node(20)
third= Node(30)

head.next=second
second.prev=head
second.next=third
third.prev=second


temp=head

while temp:
    print(temp.data, end= "<->")
    temp=temp.next

print("None")


# insert at beginning============
"""
new_node= Node(1)

new_node.next=head
head= new_node
temp=head

while temp:
    print(temp.data, end= "<->")
    temp=temp.next

print("None")
"""
# Insert at ending===============
"""
new_node=Node(40)
temp=head
while temp.next:
    temp=temp.next


temp.next= new_node
new_node.prev= temp

temp=head

while temp:
    print(temp.data, end= "<->")
    temp=temp.next

print("None")
"""


# delet at specific value =========
'''
key=20
temp=head

while temp:
    if temp.data==key:
        break
    temp=temp.next

if temp:
    temp.prev.next= temp.next
    temp.next.prev= temp.prev

temp=head
while temp:
    print(temp.data, end= "<->")
    temp=temp.next

print("None")
'''

# delet at beginnig===========
'''
head= head.next
head.prev=None

temp=head
while temp:
    print(temp.data, end= "<->")
    temp=temp.next

print("None")
'''

# Delet at ending===========

temp=head

while temp.next:
    temp=temp.next

temp.prev.next = None

temp=head
while temp:
    print(temp.data, end= "<->")
    temp=temp.next

print("None")


# Circular linked list=========================================

class Node:
    def __init__(self,data):
        self.data= data
        self.next= None


head= Node(10)
second= Node(20)
third= Node(30)


head.next=second
second.next=third
third.next=head


temp=head
while temp:
    print(temp.data, end= "->")
    temp=temp.next

    if temp==head:
        break

print(("back to head"))

temp


# Insert at beginning ========
"""
new_node= Node(1)
temp=head
while temp.next != head:
    temp=temp.next

new_node.next= head
temp.next= new_node
head= new_node

temp= head
while temp:
    print(temp.data, end="->")
    temp= temp.next
    if temp==head:
        break
"""

# inserting at end=============
'''
new_node= Node(40)

temp=head
while temp.next != head:
    temp=temp.next

temp.next=new_node
new_node.next=head

temp= head
while temp:
    print(temp.data, end="->")
    temp= temp.next
    if temp==head:
        break

'''

# Delete at beginning ========
temp = head
while temp.next !=head:
    temp=temp.next

temp.next= head.next
head= head.next 


# delete at ending=========
temp=head 
while temp.next.next != head:
    temp= temp.next

temp.next= head

# delete specific value ==============
key=30
temp= head 
while temp.next.data != key:
    temp= temp.next

temp.next= temp.next.next




