# f = open("rehan.txt")
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# #print(f.readline())
#
#
with open("rehan.txt") as f:
    a = f.readline(4)
    print(a)