#Functions
def function1():
    print("hello world")
def function2(a,b):
    """This a function which will give average of two numbers"""
    average = (a+b)/2
    #print(average)
    return average
#v = function2(6,5)
#function2(1,2)
#print(function2(5,6))
print(function2.__doc__)