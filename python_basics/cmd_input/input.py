# Accepting Input from Console
"""
User enters the values in the Console and that value is then used in the program as it was required.
To take input from the user we make use of a built-in function input().
"""
# name = input("Enter your name:")
# print(name)

# Typecasting the input
# name = input("Enter a number:")
# print(name)
# print(type(name))
# num = int(name)
# print(num)
# print(type(num))
# Taking multiple inputs from user in Python
nums = input("Enter multiple number:")
nums = nums.split()
for num in nums:
    int_num = int(num)
    print(int_num)
    print(type(int_num))
