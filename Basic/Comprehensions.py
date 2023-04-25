# comprehensions

# list comprehensions

# my_nums = [2,4,5,7,44,33,53,23,8]

# even_nums = []

# for i in range(len(my_nums)):
#     if my_nums[i]%2==0:
#         even_nums.append(my_nums[i])
# print(even_nums)        

# Instead of this big process we can directly do shortcuts with comprehensions

# There is only one line of code
# even_num = [n for n in my_nums if n % 2==0]
# print(even_num)


# example 2

# names = ["Bruce","Barry","Tony","steve","clark"]

# charcters = ["batman","flash","iron man","captain","superman"]

# Without comprehension
# my_dict = {}
# for name,char in zip(names,charcters):
#     my_dict[name] = char

# print(zip(names,charcters))

# With comprehension
# my_dict = {name:char for name,char in zip(names,charcters)}

# print(my_dict)


# example 3

# set comprehension

# nums = [21,3,2,1,4,3,2,4,5,6,4]

# my_set = set()

# for i in nums:
#     my_set.add(i)

# print(my_set) 

# with comprehension

# my_Set = {n for n in nums}
# print(my_Set)

