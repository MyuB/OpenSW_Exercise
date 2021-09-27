from random import *

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        deque_data = None

        if not self.isEmpty():
            deque_data = self.queue[0]
            self.queue = self.queue[1:]

        return deque_data

    def peek(self):
        peek_data = None

        if not self.isEmpty():
            peek_data = self.queue[0]

        return peek_data

    def isEmpty(self):
        flag = False
        if len(self.queue) == 0:
            flag = True
        return flag

    def queueSize(self):
        return len(self.queue)


i = 0
Q = Queue()

while i < 10:
    num = randint(1, 2)
    print(f"---{i + 1} step---")

    if num == 1:
        Q.enqueue(i)
    else:
        num = Q.dequeue()

    print("Current Queue: ", Q.queue)
    print("Peek data: ", Q.peek())
    print("Queue : ", Q.queueSize())
    i += 1