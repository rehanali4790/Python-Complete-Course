
print("Enter num 1")
num1 = int(input())
print("enter num2")
num2 = int(input())
operation = input("Enter operation")
if num1==45 and num2 ==3 and operation=="*":
    print("555")
elif num1==56 and num2 ==6 and operation=="+":
    print("77")
elif num1==56 and num2 ==9 and operation=="/":
    print("555")
elif operation=="*":
    print(num1*num2)
elif operation=="+":
    print(num1+num2)
elif operation=="/":
    print(num1/num2)
elif operation=="-":
    print(num1-num2)
else:
    print("invalid operation")


