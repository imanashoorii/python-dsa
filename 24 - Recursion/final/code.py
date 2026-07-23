"""
Call Stack Explanation
"""

def func_three():
    print("Three")

def func_two():
    func_three()
    print("Two")

def func_one():
    func_two()
    print("One")

func_one()


"""
Factorial function that is the most common function for introducing recursion
"""

def factorial(n):
    """
    This function is actually a call stack!
    each time it should calculate the n * factorial(n-1)
    """
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))