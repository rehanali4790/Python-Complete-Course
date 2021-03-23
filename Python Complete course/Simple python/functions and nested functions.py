# l = 10
# def funct1():
#     global l
#     #l = 5
#     m = 7
#     l = l+8
#     print(l)
# funct1()
#
#
#
def rehan():
    '''Global variable only try to find elements outside the function not within the function'''
    x = 10
    def ali():
        global x
        x = 44
    print("print x befor calling",x)
    ali()
    print("print x after calling",x)
rehan()
print(x)