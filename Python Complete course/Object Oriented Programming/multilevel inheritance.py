class Dad:
    def printfunc(self):
        return "Hey this is class Dad's property"
    pass

class Son(Dad):

    def printf(self):
        return "This is son's property"
    pass

class Grandson(Son):
    pass
rehan = Grandson()
print(rehan.printf())
