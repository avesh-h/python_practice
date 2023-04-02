

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