# data types

# None , Numeric (int , bool , float , complex) , List , Set , Dictionary , Tuple , String , Range (use for loops)

# Int , boolean , float , string , none ,

# Type conversion

# a = 2

# print(float(a))

# print(bool(a))

# c = False

# print(int(c))

# None type in python will give when if any element is undefined inside the array

# None type represents the absence of the value inside the array or set or dictionary or tuple

# Just like how JS variable works on camelCase in python the variable name is on snake_case

# Note: Install pep8 for formatting python code like block scope in python in javascript we can tell the perticular line of code inside the block scope or not which is inside {} it but in python block scope is added with : this so when we want end our code inside the block scope then at the end we need to add two line breaks in python programming.

# * operator is also used in python for the destructuring or unpacking the remainning of variables and also used in args in function


                # ------------Pass by value and pass by reference---------


# python work is based on pass by assignment or call by object reference

# SO python is actually work differently it behaves differently in python if we pass the variable for change the value so first it will act like pass by reference you can see in the example and when you change the value of the that variable it will act like pass by value in which it will not affect the original value of that memory but it will declare the new variable in memory and store the updated value inside of it.

# before the updatation it will point to the original value and after updation it will change the reference of the value

# def change_val(a):
#     print(id(a))
#     a = 22
#     print("change refernce",id(a))

# a = 10 
# print(id(a))

# change_val(a)


# Base knowledge

# List => []  it's array in python
# Tuple => (1,2,3) It's iterable like array but it's immutable it cannot let us change the value inside of it
# Dictionary => {"key","value"} It's like json object and also iterable in loop and mutable

# -----------if ,elif ,else-----------------


# we can directly store variable without declare var const let like in js

# msg = "hello world"
# print(msg.capitalize())
# newMsg = msg.split()
# print(newMsg)

# name = input()
# print ("hello",name)

# if else statment example

# if 1 > 2:
#   print("1 is greater than 2")
# elif 2 > 1:
#   print("1 is not greater than 2")
# else:
#   print("1 is equal to 2")


# ------------------------------stacks-----------------------------------


# Stack

# In this example we get input from the user and based on that we perform the operation in list

# stack = []

# def push():
#     print("please enter the number to add in stack")
#     selectNum = int(input())
#     stack.append(selectNum)
#     print(stack)

# def pop():
#     if not stack:
#         print("stack is already empty")
#     else:
#        removed_elem = stack.pop()
#        print("Removed:",removed_elem)
#        print(stack)

# while True:
#     print("plese select an operation 1.Add 2.Remove 3.Quit")
#     selected_op = int(input())
#     if selected_op == 1:
#         push()
#     elif selected_op == 2:
#         pop()
#     else:
#         break





