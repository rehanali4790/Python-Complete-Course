# n! = n*(n-1)!

# def factorial_iterative(n):
#     """This function print factorials"""
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac
# def factorial_recursive(n):
#     """This function print factorials"""
#     if n == 1 or n==0:
#         return n
#     else:
#         return n* factorial_recursive(n-1)
# number_ = int(input("Please enter a number"))
# print("Fctorial using iterative method",factorial_iterative(number_))
# print("Fctorial using recursive method",factorial_recursive(number_))
def fibonacci(n):
    """This function calculates the fibonacci series"""
    if n == 1 :
        return 0
    elif n == 2 :
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
number_ = int(input("Please enter a number"))
print(fibonacci(number_))