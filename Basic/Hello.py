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


# ------------------------------ Strings and methods------------------------------


# template literals in Python

# firstName = "Agent"
# lastName = "carlo"

# print(f'{firstName} {lastName} is here in USA')
# my_str = "Python for Beginners"

# To make string capitalize
# print(my_str.title())

# find method in string
# print(my_str.find("P"))

# in method will give us the boolean value like if we want to check is exist or not
# print('Python' in my_str)

# String methods we learn

# my_str.upper()
# my_str.lower()
# len(my_str)
# "..." in my_str
# my_str.title()
# my_str.find()
# template litrals


# Replace method
# print(my_str.replace("Beginners","Absolute beginner"))

# -----------------Operators--------------------

# Assignment operators

# multiple assigning values in single lines
# a, b, c = 5, 3, True

# print(a != b)

# print(10 / 3) #it will give us 3.33333 (float form)

# print (10 // 3) #it will give us 3 (int form)

# print(10 ** 3) # it will give us 10^3 = 1000


# swap values
# a = 3
# b = 2

# temp = a
# a = b
# b = temp

# print(b)

# Without declaring third varaible

# a = 100

# b = 526

# a, b = (b-a)+a, (a-b)+b


# print(b)

#or (best technic)

# a,b = 2 , 6

# a = a + b #2 + 6 = 8
# b = a - b #b = 8 - 6 = 2
# a = a - b #a = 8-2 = 6


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

# ------------------------Loops and itereators-----------------------------

# While loop

# n=1
# while n<=10:
#   print(n)
#   n+=1


# While loops

# loop_condition = True

# while loop_condition:
#     print("Loop Condition keeps: %s"%(loop_condition))
#     loop_condition = False


# Guess the secret number game

# secret_num = 9

# try_it = 3

# while try_it:
#     enter_num = int(input("Guess:"))
#     if enter_num != secret_num:
#         print("Wrong!")
#         try_it -= 1

#     else:
#         print("You win!")
#         break;


# start = False
# while True:
#   state = input("enter->").lower()
#   if state == "start":
#     if start:
#       print("car is already started!")
#     else:
#       start=True
#       print("Starting...")
#   elif state == "stop":
#     if not start:
#       print("car is already stopped!")
#     else:
#       start=False
#       print("stopping...")
#   elif state == "help":
#     print('''
#     start - car will start.
#     stop - car will stop.
#     help - repeat.
#     ''')
#   elif state.lower() == "quit":break


# For loop
# if we want to give starting range of the for loop

# for i in range(5,11):
#     print(i)

# if we did not mention the starting range of the for loop it will take 0 automatically
# for i in range(11):
#   print(i)

# Loop iteration onto array it looks simply like for in loop in javascript
# books=["sherlock","snakes","life of pi","worlds","the banks"]

# for book in books:
#     print(book)


#continue
# for i in range(1,21):
#     #for even
#     if i % 2:
#         continue
#     print(i)

# Total
# arr2 = [10,20,30]
# total = 0
# for i in arr2:
#     total +=i

# print(total)


# Nested loop

# for x in range(4):
#   for y in range(3):
#     print(f'({x},{y})')

# Pattern

# pattern = [5,2,5,2,2]

# for i in pattern:
#     output = ""
#     for j in range(i):
#         output+="x "
#     print(output)





                                                #--------------- Functions-----------------





# def my_func():
#     print("this is my first function in python")

# my_func()

# Parameters
# Just like we used to do in JS = func(...args) in python = def(*args)

# def the_func(name,*otherInfo):
#     print(name)
#     print(otherInfo) #it will give us in tuple format

# the_func("rajesh","Mumbai",23,1992)


# def the_param(**args):
#     print(args) # it will give us in dictionary format

#     for key,val in args.items():
#         print(key,val)

# user_info = the_param(name="rajesh",age=24,city="mumbai")



# Gobal variables

# a = 10

# b = 20

# def chnge_global():
    
#     print(globals()) #it will give us the whole dictionary of global variables

#     globals()['a'] = 12

# chnge_global()

# print(a)


# Conditional printing something
# if condition1 or condition2           # ||
# if condition1 and condition2         # &&
# if not condition                     # !condition


# like we use to add in js like if (!num){console.log("false")} but in python we have to like this

# num2 =0

# if not num2 :
#     print("false")

# num1 = 2

# if num1:
#     print("they are equal")

# else: print("they are not equal")


# In python the type of array it shows type = list

# check = [22]

# print(type(check))

# Recursion function in python

# def fac_func(num):
#     if num < 1 :
#         return 1
    
#     return num * fac_func(num - 1)
     
    
# print(fac_func(5))


# Higher order function in python (map,filter,reduce) (Ternary and lamda function in python)

# Filter function

# def is_odd(n):
#     if n % 2:
#       return n  

# nums = [1,2,5,44,3,34,22,5,3,32]

# odd_list= list(filter(is_odd,nums))

# print(odd_list)


# Map function (lamda function syntax like arrow function in JS)

# def squar(n):
#     return n * n

# num_list = [2,5,3,2,5,6,3]

# map_list = list(map(lambda n : n*n,num_list))

# print(map_list)


# reduce function

# from functools import reduce

# def sum_odd(acc,curr):
#     if curr % 2:
#         acc.append(curr)
    
#     return acc

# num_list = [1,2,54,23,43,52,32,4,33]
# # total_sum = reduce(sum_odd, num_list,[]) 


# With turnary operator and lambda function 
# total_sum = reduce(lambda acc, curr: acc + [curr] if curr % 2 else acc, num_list, [])

# print(total_sum)




# a = [1,10,22]

# b = [2,8,9]

# c = [22,64,644]
# d = a + b + c 

# print(d)
                                # ---------- Tuple therory and practicals-----------------




# Tuples ara exactly like list (arrays) but we cannot update or delete the elements from the tuplse it's immutable

# Tuple example
# x = ('apple', 'banana', 'cherry')
# y = enumerate(x)

# There is method in python calles Unpacking which is similar to the destructuring in Javascript

# destructuring in Python

# cordinates = (1,2,3)

# x,y,z = cordinates

# print(x)

# It also works in List in python

# arr_one=[2,44,"less","yes"]

# x,y,z,r = arr_one

# print(r)




            # -------------------------- List Mehods and practicals -------------------




# and with list method we actually add inside the array so basically list is actually array in python

# print(list(y))

# if we want to declare tuple with command

# for tuple
# tuple1 = tuple()
# OR
# tuple1 = ()
# print(tuple1)

# for list

# arr1 = list()
# OR
# arr1 = []
# print(arr1)

# Find the maximum number inside the array

# my_list = [1,5,3,6,-43,11,-700,-22,44]
# max = 0
# for i in range(len(my_list)):
#   if max < my_list[i]:
#     max = my_list[i]

# print(max)

# List methods

# append - which is push method in python
# my_list = [2,3,5,1]

# my_list.append(22)

# print(my_list)

# Instert method is the method that where we actually want to add the data inside the list first argument is index like where you want to add and second what to add
# my_list.insert(1,4)

# print(my_list)

# Remove method

# it will remove the element from the list
# my_list.remove(3)

# if we want to clear the whole array

# my_list.clear()

# pop method will remove the last element from the array

# my_list.pop()

# findIndex method inside the array of python
# get_index = my_list.index(5)

# like if we want to check the number is exist inside the array or not for the boolean condition
# print(5 in my_list)

# Copy Method there are two way for that

# copy method is like spread operator in python like if don't want to change the original array so first we make copy of that array then apply the oprations

# arr_one = [2,44,3,21,"time"]

# arr_two = arr_one.copy()
# OR

# arr_two = arr_one[:]
# print(arr_two)

# print(arr_two)


# Slice operation in python list

# the_arr = [1,2,3,4,5,6,7,8]

# sliced_arr = the_arr[3:] #ans will give the new array of [4,5,6,7,8]

# sliced_arr2 = the_arr[2:-1] #ans will give the new array of [3,4,5,6,7,8]

# syntax

# Array[startIndex:endIndex:step]

# sliced_arr3 = the_arr[1::2]   #like third argument will step for the array for this example it will give even numbers (even indexes)

# sliced_arr3 = the_arr[0::2] #it will give odd numbers from the array with skip one step(odd indexes)


# Update operation of array

# arr_main = [2,55,3,2,44]

# changed_var = 55

# new_arr = arr_main[:]  #create copy of array

# give_index = new_arr.index(changed_var)  #Find the index of the array

# new_arr[give_index] = 23     #update directly

# print(new_arr)


# Count method and different case scenarios

# full_arr = [2,5,4,7,5,4,3,1]

# find_num_in_arr = 22

# for i in range(len(full_arr)):
#     if full_arr.count(find_num_in_arr): # in this condition if it coudn't find it will give 0 that means it false
#         print(f'number: {find_num_in_arr} is exist in the array')
#         break
#     else:
#         print(f'the number :{find_num_in_arr} is not exist in the array')
#         break

# OR

# Check number is exist or not inside array with in keyword python

# if find_num_in_arr in full_arr:
#     print(True)

# else : print(False)

# Remove duplication list and get new array of unique values

# But main problem with this solution is that it will give disordered values inside the arry then the original order of the array elements

# new_arr = list(set(full_arr))
# print(new_arr)

# Or

# unique_arr = []

# for i in range(len(full_arr)):
#   if not full_arr.count(full_arr[i]) > 1:
#     unique_arr.append(full_arr[i])

# print(unique_arr)

# Or

# unique_arr = []

# for number in full_arr:
#     if number not in unique_arr:
#         unique_arr.append(number)
# print(unique_arr)

# ----------------------------- Dictionary mehods and practicals ------------------


# Dictionary : - dictionary is like object of javascript

# Dictionary: Key-Value Data Structure  is exactly JSON in javascript

# This one type is called the dictionary and also we cannot apply for loop onto this
# python_obj = {
#     "val1":"this is one",
#     "val2":"second",
#     "val3":"i am third",
#     "val4":4

# }

# print(type(python_obj))

# print(python_obj["val1"])

# If we want to add something inside the dictionary then it will add name property at the end
# python_obj["name"] = "avesh"

# print(python_obj)


# enumerate

# With enumerate method it will actually adding index number inside the x so it can be iterable like if we want you use in loop or something like that

# after enumerate y will be like (0,"apple"),(1,"banana"),(2,"cherry")

# d = {}
# OR
# print(d)

# d = dict()

# If we want any property inside it
# d["Name"] = "jan"
# d["lastName"] = "doe"
# print(d)

# Here we get the array of keys with key method just like in js Object.keys()
# key_array = d.keys()
# print(key_array)

# value_array = d.values()
# print(value_array)

# we can apply for loop onto that for access the each value of dictionary
# for key in d:
#     print(d[key])


# my_dict = {"one": "avesh", "2": "programming", 3: "red", 4: "true", 5: False}

# for convert the dictioary keys of array and values of array
# print(my_dict.keys())
# print(my_dict.values())

# Get method in dictionary to get key value it requires name of the key
# print(my_dict.get("one"))

# Pop method of dictionary it also require key name to remove the value from the dict and also return the deleted value
# deleted_val = my_dict.pop("2")

# print(my_dict)

# print(deleted_val)

# print(my_dict.popitem())

# Convert the list into the dictionary

# list1 = ["name", "std", "age", "birthYear"]

# list2 = ["jayesh", 6, 14, 2001]

# print(dict(zip(list1, list2)))

# full_dict_list = dict(zip(list1, list2))

# for loop to access the value of the dictionaries keys
# for i in full_dict_list:
#     print(full_dict_list[i])

# How to remove the any property from the dictionary

# i want to remove the property called age from the dictionary

# del full_dict_list["age"]


# user_self = {
#     "name":"user",
#     "study":"mba",
#     "age":29,
# }

# If propery will no exist it will give us our default property which we set

# print(user_self.get("birthDate","Jan 20"))
# print(user_self)


# convert numbers into words

# phone = input("Phone No. ")

# numbers = {
#     "1":"One",
#     "2":"Two",
#     "3":"Three",
#     "4":"Four",
#     "5":"Five",
#     "6":"Six",
#     "7":"Seven",
#     "8":"Eight",
#     "9":"Nine"
# }

# new_numbers={
#     "1":"One",
#     "2":"Two",
#     "3":"Three",
#     "4":"Four",
# }

# for ch in phone:
#     print(numbers[ch])
# print(new_numbers.get(ch,"not exist"))

# ------------------Set methods-----------------------

# set method is is used to store the unique value inside the array

# if we want to create simple set we can directly add curly braces and add the values that you want to be them as unique as you can see i repeated value of 2 and 3 but we we'll not get repeated in set

# s= {2,3,5,2,4,3}
# print(s)

# s2 = [2,5,3,2,5,4,7,8]
# print(set(s2))

# for declare the set method

# It's not applicable for the the dictionaries
# my_set = set({
#     "name":"user",
#     "age":22,
#     "name":"newUser",
#     "study":"mba",
#     "name":"user2"
# })

# print(my_set)

# me_set_2 = ["2","time",True,"33",2,33,"time"]

# We can also apply the for loop on set Method
# for i in me_set_2:
#     print(i)

# unique_set = set(me_set_2)

# If we want to add something inside the set
# unique_set.add("23")
# here first we remove the duplicate value from the set and then convert it into the array
# print(unique_set)
# mynewList = list(unique_set)

# print("list",mynewList)

# We can also join the two different collection of set with union method it's like join method in js

# Here you can see i add same value inside two different sets but still set method only add one value

# Best thing about this method is that it will return us the new set with both values

# set1 = {22,3,55,True}
# set2 = {"false",5,"33",True}

# full_set = set1.union(set2)

# print(full_set)


# update method

# The update method is same as union we can add new set inside the existing one but it will never return the new set it will update the existing one that's why it's called the update method

# set3 = {2,44,"true",False}
# set4 = {"red","yellow",45}

# set3.update(set4)

# print(set3)

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

# ---------------------------------Modules--------------------------------
# Here you can see that i import the class student from another file and use that class create instance of that here
# import oops

# student3 = oops.Student("ramesh")

# print(student3.show())







                            # -----------------Module Array------------------

# It is array but in python we have to declare the type of value that we are want to store inside the array as you can see in below example

# import array as arr


#OR like destucture
# from array import array

#i is type of integer we can say f for float and s for string u for characters

# arr1 = arr.array("i",[3,5,55,3,23])

# arr1.append(6)

# print(arr1)



# example find the index of users array

# print("How Many values you want in array?")

# n = int(input("Enter the value: "))

# user_arr = arr.array("i",[])

# for i in range(n):
#     val = int(input("Enter: ")) 
#     user_arr.append(val)


# print("serch the value for the Index")

# serched_val = int(input("Enter serch Number:"))

# for e in user_arr:
#     print(e)
#     if e == serched_val:
#         print("Index is:",user_arr.index(e))
#         break

                                # -------------Module numpy for 2d array----------

# Numpy libraray used for 2d array

# from numpy import *

# array_one = array([2,3,5,3,5,3])

# my_arr = array_one[:]

# print("My",my_arr)

# print(id(array_one))
# print(id(my_arr))

# mul_arr = array([
#     [1,2,3] ,
#     [2,1,4]
# ])

# print(mul_arr.shape)

# Convert into single Array

# print(mul_arr.flatten())


# Special varaibles

# def main():

#     print("Hello")
#     print ("Welcome user")


# if __name__ == "__main__":
#     main()


# connected with oops module 

# in this issue we have two different modules in this module we are calling mul() function from the oops module and in oops module that mul function is called inside the main function so the problem is when we calls that mul() function in this module it will first call the main function of oops module and then mul() function will execute so to stop this we're gonna use special variable __name__ which can you see inside oops module.


# from oops import mul


# def checkCall():
#     print("check is called")
#     mul()



# def main():
#     print(f"Main of {__name__} module called")
#     checkCall()   


# main()     




