
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

