# def func1():
#     print("subscribe now")
# func2 = func1
# del func1
# func2()

def dec1(func1):
    def nowexec():
        print("now executing")
        func1()
        print("executed")
    return nowexec
@dec1
def this_is_rehan():
    print("this is rehan")


# this_is_rehan = dec1(this_is_rehan)

this_is_rehan()
