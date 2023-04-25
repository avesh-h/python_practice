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


# Lambda function

var = [2,3,4,5]

# This is lambda function it is same as arrow function of the js it can also take multiple arguments
square_rt = lambda n:n*n

result = list(map(square_rt,var))

print(result)



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

# This higher order function is actually return the iterable object and then that object we can convert it into the list ,set , tuple


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

# Map function can also apply on both different lists 

# var1 = [2,3,4]
# var2 = [5,6,7]


# result = list(map(lambda n1,n2: n1 + n2 ,var1,var2))

# print(result)

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

# Generator function

# def my_func():
#     yield 1
#     yield 2
#     yield 3
#     yield 4


# values = my_func()


# # It will give us the single iteraion each time

# print(values.__next__()) #1
# print(values.__next__()) #2
# print(values.__next__()) #3
# print(values.__next__()) #4


# Generator functions each iteration with help of for loop we can also do that with __next__ function()

# def topTenSq():

#     num = 1

#     while num <=10:
#         sq = num * num
#         yield sq
#         num+=1


# values = topTenSq()

# for i in values:
#     print(i)


# Linear search

# position = -1

# def find_func(arr,n):
    
#     for i in range(len(arr)):
#         if n == arr[i]:
#             globals()['position'] = i
#             return True
        
#     return False

# list_arr = [2,3,5,2,1,5,44,6,2,22]


# searched_num = int(input("Enter the number you searching: "))

# if find_func(list_arr,searched_num):
#     print(f"Your search at index {position + 1}")

# else: print("Sorry we coudn't find the number you search!")


