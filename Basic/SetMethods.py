
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