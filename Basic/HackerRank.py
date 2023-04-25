# 1)FInd second max value from the array

# arr = [2,3,6,6,5]
# max_val=max(tuple(arr))
# second_max =0
# reverse_arr = sorted(arr,reverse=True)
# for i in reverse_arr:
#     if i < max_val:
#         second_max = i
#         break

# print(second_max)


# 2)Find the second lowest marks in the array

# num_students = int(input("How many Students:"))

# student_arr = []

# for i in range(num_students):
#     name = input("Name: ")
#     marks = float(input("Marks: "))
#     student_arr.append([name,marks])

# student_arr = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]

# print(student_arr)

# marks_arr = list(map(lambda n : n[1],student_arr))

# lowest_marks  = min(tuple(marks_arr))

# sorted_arr = sorted(marks_arr,reverse=False)

# second_lowest_marks = 0
# for i in sorted_arr:
#     if i > lowest_marks:
#         second_lowest_marks = i
#         break

# for i in sorted(student_arr):
#     if i[1] == second_lowest_marks:
#         print(i[0])


# 3)The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

# Input will be like this:
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika


# Ans:

# from functools import reduce
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()

#     total = reduce(lambda acc,curr : acc+curr, student_marks[query_name],0)
#     avg =float(total/len(student_marks[query_name]))
#     rounded_avg=format(avg,".2f") #for two decimal extra
#     print(rounded_avg)


                                # Stack in pyhton


# 4)collections.deque()
# A deque is a double-ended queue. It can be used to add or remove elements from both ends.

# Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same  performance in either direction.

# Click on the link to learn more about deque() methods.
# Click on the link to learn more about various approaches to working with deques: Deque Recipes.

# Sample Input

# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft


# Ans:

# from collections import deque

# operations = int(input())
# d = deque()

# for i in range(operations):

# We add here " " blank space inside the array for the proper values like oper we get operation name and for val we get operation value

#     oper, val, *args = input().split() + ['']
#     eval(f'd.{oper}({val})')
    
# eval() method is let us perform the operation which written inside the string, example string like this "5 + 7" so if we want to say that we want to execute this string as a python code then eval() function is used , in above operation it uses like (f'd.append(val)')
    
# print(*d) #Destructure the deque list values



# we can use deque as a stack and queue as well

# stack approach is LIFO = last in first out
# queue approach is FIFO = first in last out

# so for stack we're gonna use append operation for design stack LIFO approch

# from collections import deque

# class Stack:

#     stack = deque()

#     def addItem(self,item):
#         self.stack.append(item)

#     def removeItem(self):
#         return self.stack.pop()


# my_stack = Stack()

# my_stack.addItem(22)
# my_stack.addItem(12)
# my_stack.addItem(33)
# my_stack.addItem(20)

# print(my_stack.removeItem())

# print(my_stack.stack)

                                                    # Queue

# Now create queue for with deque FIFO approach

# from collections import deque

# class Queue:

#     queue = deque()

#     def addItem(self,item):
#         self.queue.appendleft(item)

#     def removeItem(self):
#         return self.queue.pop()


# my_stack = Queue()

# my_stack.addItem(22)
# my_stack.addItem(12)
# my_stack.addItem(33)
# my_stack.addItem(20)

# print(my_stack.removeItem())

# print(my_stack.queue)


# It is basic example of how linklist basically work


# class LinkedList:
#     def __init__(self,value,nextValue=None):
#         self.value  = value
#         self.nextValue = nextValue



# value1 = LinkedList("3")
# value2 = LinkedList("5")
# value3 = LinkedList("8")
# value4 = LinkedList("19")

# value1.nextValue = value2
# value2.nextValue = value3
# value3.nextValue = value4


# currentVal = value1

# while True:
#     print (currentVal.value,end="->")
#     if currentVal.nextValue is None:
#         print("None")
#         break
#     currentVal = currentVal.nextValue

total = 6    
for i in range(1,total+1):
    print(i)