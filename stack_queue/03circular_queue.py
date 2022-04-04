# 34, 45 , 46,67,78 ,89,23 ,34
# 0  , 1  , 2, 3, 4,  5, 6, 7
#      R ,  F

# (self.rear + 1) % self.size ==self.front
# (1+1)%8 == 2
# 2==2

import re


class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.queue = [None for i in range(self.size)]
        self.front = self.rear = -1

    def enqueue(self,data):
        # checking whether queue is full or not
        if ((self.rear + 1)%self.size == self.front):
            print("Overflow")
            return
        # Adding first element
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1 )%self.size
            self.queue[self.rear] =data

    def dequeue(self):
        # If queue is empty
        if (self.front == -1):
            print("Underflow")
            return
        # if only one element is present
        elif (self.front == self.rear):
            popVal=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return popVal
        else:
            popVal=self.queue[self.front]
            self.front = (self.front+1)%self.size
            return popVal