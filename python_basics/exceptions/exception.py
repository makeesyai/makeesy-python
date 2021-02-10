# Exceptions vs Syntax error
# raise, and assert
# Simple try-except
# Catch named exceptions
# try catch with else
# Use Exception class
# try catch with finally
import sys

a = 10

if a < 100:
    raise Exception("The number is less than 100")

# If the machine is other than Linux it will throw an error
assert ("linux" in sys.platform), "This code is for Linux machine only."

lst = ['a', 0, 'b', 1, 'c']

for item in lst:
    try:
        print("The item is:", item)
        result = 1/item
    except TypeError:
        print('Its a type error')
        print(sys.exc_info()[0])
    except ZeroDivisionError:
        print('Its a zero division error')
        print(sys.exc_info()[0])
    else:
        print("The results is:", result)
    finally:
        print("This will execute whatever...")
