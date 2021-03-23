print(" enter anumber")
a = input()
print(" enter number")
b = input()
try:
    print("The sum of your numbers is",
          int(a) + int(b))
except Exception as e:
    print(e)
print("This is a very important line")
c = input("please input a number")
print(c)