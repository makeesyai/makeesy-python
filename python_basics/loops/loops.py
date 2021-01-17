# WHILE LOOP
# count = 0
# while count < 3:
#     print("Hello Python")
#     count = count + 1
# Single statement while block
# while count < 3 : print("Hello python"); count += 1; print("Hello world")

# FOR LOOP
# for in Loop:For loops are used for sequential traversal. For example: traversing a list or string or array etc.
# fruits = ["orange", "mango", "kivi"]
# for fruit in fruits:
#     print("The fruit name is: ", fruit)

# Range(): Return an object that produces a sequence of integers from start (inclusive)
# nums = range(20)
# print(list(nums))
# for i in range(3, 10, 2):
#     print(i)

# Iterating by index of sequences
# fruits = ["orange", "mango", "kivi"]
# for index in range(len(fruits)):
#     print("The fruit name is: ", fruits[index])

# Nested Loops
# for i in range(5):
#     for j in range(i):
#         print(i, end=' ')
#     print()

# Loop Control Statements: continue and break
# string = "hello world"
# for ch in string:
#     if ch == 'l':
#         continue
#     print(ch)

# string = "hello world"
# for ch in string:
#     if ch == 'z': # if this is true the else part of the FOR loop wont run
#         break
#     print(ch)
# else:
#     print("The break statement is not executed") # This will only run when the loop exhausts listing all the elements
#
# print("Outside for loop")

count = 0
while count < 10:
    print("I'm less than 10")
    if count == 20:  # if this is true the else part for the WHILE loop wont run
        break
    count += 1
else:
    print("While is completed without break")  # This will only run when the loop terminates with condition count < 10
print("outside while loop")

# Using else statement with while loops :
# The else clause is only executed when your while condition becomes false.
# If you break out of the loop, or if an exception is raised, it won’t be executed.

# Using else statement with for loops: similar to while loop
