
queue = []

# Enqueue (Insert elements)
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)

print("Queue:", queue)

queue.pop(0)

print("After Dequeue:", queue)


print("Front element:", queue[0])

# Check if empty
if len(queue) == 0:
    print("Queue is empty")
else:
    print("Queue is not empty")



# linear queue=====================================
class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, data):
        self.q.append(data)

    def dequeue(self):
        if not self.q:
            print("Empty")
        else:
            self.q.pop(0)

    def display(self):
        print(self.q)


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()




# circular queue=================
class CircularQueue:
    def __init__(self, size):
        self.q = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Full")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Empty")
            return

        print("Removed:", self.q[self.front])

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    def display(self):
        print(self.q)


q = CircularQueue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()  


# Priority Queue=========================
class PriorityQueue:
    def __init__(self):
        self.q = []

    def enqueue(self, data, priority):
        self.q.append((priority, data))

    def dequeue(self):
        if not self.q:
            print("Empty")
        else:
            self.q.sort()
            print("Removed:", self.q.pop(0)[1])

    def display(self):
        print(self.q)


q = PriorityQueue()
q.enqueue(10, 2)
q.enqueue(20, 1)
q.enqueue(30, 3)

q.display()
q.dequeue()