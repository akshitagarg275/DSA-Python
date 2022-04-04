#TODO: Not recommended

# bad_list=[]

# bad_list.append("superman")
# bad_list.append("batman")
# bad_list.append("flash")

# bad_list.pop(0)

# print(bad_list)

# TODO: using collections

# from collections import deque

# mylist =deque()
# print(type(mylist))

# mylist.append("aquaman")
# mylist.append("batman")
# mylist.append("flash")

# print(mylist)
# mylist.popleft()
# print(mylist)

# TODO:using queue module

from queue import Queue
myList = Queue()
# print(type(myList)) 
# print(myList)

myList.put("Aquaman")
myList.put("batman")
myList.put("flash")

print(myList.get())

# TODO: It immediately tells whether queue is empty or not
print(myList.get_nowait())