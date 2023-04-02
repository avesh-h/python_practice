
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