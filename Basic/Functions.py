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