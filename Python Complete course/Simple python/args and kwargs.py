def funargs(normal, *args, **kwargs):
    print(normal)
    for items in args:
        print(items)
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

kw = {"rehan":"gud","ali":"gud","samo":"gud"}
normal = "This is a normal fungction"
rehan_ = ["gud","bad","normal"]
funargs(normal,*rehan_,**kw)