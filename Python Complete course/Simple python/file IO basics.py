""" File IO basics
"r" - open file for reading
"w" - open file for writing
"x" - create a file if not exist
"a" - add more content to a file
"t" - text mode
"b" - binary mode
"+" - read and write




"""
f = open("rehan.txt")
print(f.readlines())
# print(f.readline())
# for line in f:
#     print(line,end="")
# content = f.read()
# content = f.read(3445)
# print("1)", content)
# content = f.read(3445)
# print("2)", content)
f.close()