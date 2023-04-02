
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
