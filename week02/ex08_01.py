from random import *
#아 이거도 모르겠음......
class Queue:
    queue = []
    def __init__(self):


    def enqueue(self, n):
        queue.append(n)
    def dequeue(self, n):

    def peek(self, n):
        temp = queue.find(n)

    def isEmpty(self):
        return
    def queueSize(self):
        return len(queue)

i = 0
Q = Queue()

while i < 10:
    num = randint(1, 2)
    print(f"---{i + 1} step ---")

    if num == 1:
        Q.enqueue(1)