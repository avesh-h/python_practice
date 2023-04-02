# OOP programming in python

# class contains of two things:
#     1) Attributes
#     2) Methods

# constructor method is the method that creates the object or it's been called whenever we declare the new object and one of the major use of constructor is use to declare the initial state of the variables during development

# constructor is also set the properties of the each instances if we don't want to declare the property like (student1.name) then we have to pass the parameter to the student1 = Student("name") like this

# ------------------------------- Basic structure of class and instances----------------------------------

# class Computer:

# Constructor function
# def __init__(self,cpu,ram):
#     self.cpu = cpu
#     self.ram = ram

# Self is always going to be first argument for just like this in javascript it's indicates like for which instance we are calling the config method for com1 or com2 . Self is to point out the current object
# def config(self):
# print("this is my pc config")
# print("computer",self.cpu , self.ram)


# Instances of Computer class

# That's how we create object in python
# with help of this it will call the constructor internally and work of the constructor is to create object from class
# com1 = Computer("i3",8)
# com2 = Computer("i5",16)

# Computer.config(com1) #this is here pass as like config(self)
# Or
# com2.config()


# Example 2

# class Student :

#     def __init__(self,marks,name):
#         self.name = name
#         self.marks = marks

#     def compareMarks(self,student2):
#         if self.marks > student2.marks:
#             print("student 1 got highest marks")
#         else:
#             print("student2 got highest marks")


# student1 = Student(90,"Ramesh")
# student2 = Student(66,"jayesh")

# student1.compareMarks(student2)

# -------------Theory-------------------

# There are two types of variable

# 1)Instance variable - The variable which value will be different for the all the instances then that variable is called the instance variable

# 2) Class variable - if we describe the variable outside the constructor function or we can say the variable value will be the same for all the instance of the object then that variable is called class variable

# Instance variable are those varaibles who deals with instance object properties like midified it show it etc.

# Class variable are the varaible who only do have common in all the instancese so for this we only going to access those variable with class name

# there are three types of methods
# 1)instance method - getrs,setters  getters only get or display the values of the instance but setters are the function that modify the value  (getters = accessors , setters = mutators)

# 2)Class methods - if we working with class variables then that method is called class method if we want to access the class variable inside method then in parametrs instead of use self parameter we gonna use 'cls' example my_classMethod(cls)

# 3) static methods - the method which nothing to do with class variable and nothing to do with instance variable those methods are called as the static method


# example `1`

# class Solution(object):

#     def __init__(self,nums,target):
#         self.nums = nums
#         self.target = target

#     def twoSum(self):
#         for i,j in enumerate (self.nums):
#             print(j)


# sol1 = Solution([3,2,3],6)
# sol1.twoSum()

# --------------------------- Inner Class-------------------------------

# class inside the anathor class

# class Student :

#     def __init__(self,name):
#         self.name = name
#         self.lap = self.Laptop()

#     def show(self):
#         print(f'The name of the student is {self.name}')

#     class Laptop:
#         def __init__(self):
#                 self.os = 'Windows'
#                 self.brand = 'HP'
#                 self.ram = 8

# def show(self,os,ram,brand):
#  print(f'The OS of Laptop is {self.os} and ram {self.ram} and brand is {self.brand}')
#  print(f'The OS of Laptop is {os} and ram {ram} and brand is {brand}')


# student1 = Student("jayesh")

# student1.name = "jayesh"


# print(student1.name)

# student2 = Student()

# student3 = Student("Rajesh")

# print("3rd student",student3.lap.brand)

# student1.lap.show("windows",4,"samsung")

# --------------------- Inheritance--------------------------

# class Animal:

#     legs = 4

#     def __init__(self,name) :
#         self.name = name

#     def walk(self):
#         print( f'This {self.name} can walk.')

#     def show_legs(cls): #cls is the key word that we can access the current class variable
#         print(f'this animals have {cls.legs} legs')

# class Dog(Animal): #that's how we can inherite one class with another
#     def __init__(self, name):
#         super().__init__(name)

#     def show_name(self):
#         print(f"Name of the Dog is {self.name}")


# my_dog = Dog("tommy")
# my_dog.show_name()
# my_dog.walk()
# my_dog.show_legs()

# --------------------- Constructure inheritance ----------------

# Basic Example

# class A:
#     def __init__(self) :
#           print("constructor of A")


#     def method1():
#          print("method 1 code")


#     def method2():
#          print("method 2 code")


# class B(A):
#     def __init__(self):
#         super().__init__()                   #constructor inheritance
#         print("constructor of B")

#     def method3():
#         print("method 3 code")

#     def method4():
#         print("method 4 code")


# In constructor inheritance if we inherit the A class in B and if we did not mention the constructor of B then the instance of B class will directly preferred the constructor of A , but constructor of B class will present then the instance of B Class will preferred the constructor of B

# Then if we inherit the constructor of both class with super keyword and declare the instance of the B then it will call the both constructor first will A then B constructor


# Declare the object of class B

# b1 = B()


# Example 2 Multiple Inheritance method

# class A:
#     def __init__(self) :
#           print("constructor of A")


#     def method1(self):
#          print("method 1 code")


#     def method2(self):
#          print("method 2 code")


# class B:
#     def __init__(self):
#         print("constructor of B")

#     def method3(self):
#         print("method 3 code")

#     def method4(self):
#         print("method 4 code")


# class C(B,A):

#     def __init__(self):
#         super().__init__()
#         print("constructor of C")

#     def methodC(self):
#          super().method3()
#          print("method c")

# c1 = C()

# c1.methodC()

#  ------------ Polymoprphism (operator overloading)--------------

# In this method we overloading the Add method of + with overwrite the built in add function of python for class because python doesn't know how plus for two different instances of class

# class Student:
#      def __init__(self,m1,m2):
#           self.m1 = m1
#           self.m2 = m2

#      def __add__(self,other):
#         m1=self.m1 + other.m1
#         m2=self.m2 + other.m2
#         s3 = Student(m1,m2)
#         return s3


# s1 = Student(22,25)
# s2 = Student(20,22)

# s3 = s1 + s2

# print(s3.m1,s3.m2)

# --------- Method Overloading(polymorphism)----------
# In this method if we sometime add one arg or two arg or three arg the method should behave the same so that's why we add the condition and add parameters to None if they are undefine
# class Student:
#     def __init__(self) -> None:
#         pass

#     def sum(self,a=None,b=None,c=None):
#         if not a == None and not b == None and not c== None:
#             s = a + b +c
#             print (s)
#         elif not a == None and not b == None:
#             s = a+b
#             print(s)
#         else:
#             s = a
#             print(s)

# s1 = Student()
# s1.sum(2)

# class Solution(object):
#     def twoSum(self, nums, target):
#         isExist = dict()
#         for i in range(len(nums)):
#             num = nums[i]
#             exist = target - nums[i]
#             if num in isExist:
#                 # we're searching current num of array is inside the target object or not
#                 return [isExist[num], i]
#             else:
#                 # after first execution {7:0} so we're storing the target num and current index
#                 isExist[exist] = i
#                 print("first", isExist)


# s1 = Solution()

# print(s1.twoSum([2, 7, 11, 15], 9))

# print(s1.twoSum([3,6,3],6))





# def add():
#     print("add values")


# def sub():
#     print("subtract values")


# def mul():
#     print("multiplication values")


# def main():
#     print(f"Main func of {__name__} module called")
#     add()
#     sub()
#     mul()

# in this condition we're simply saying that if this main function will called in it's own file then call this function othewise not call main()    

# if __name__ == "__main__":
#     main()