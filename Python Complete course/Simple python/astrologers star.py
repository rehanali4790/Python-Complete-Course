print("enter number of rows")
rows_ = int(input())
c = int(input("0 or 1\n"))
b = bool(c)
if c == True:
    a = ""
    print("Printing true pattern")
    while rows_ != 0:
        rows_ -=1
        a += "*"
        print(a)
else:
    a = "*"
    print("Printing false pattern")
    while rows_ != 0:
        print(a*rows_)
        rows_ -=1













