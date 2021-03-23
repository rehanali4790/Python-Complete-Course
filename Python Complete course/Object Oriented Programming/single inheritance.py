class employee:

    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    def printdet(self):
        print(f"Name of employee : {self.name} \n Salary of employee : {self.salary} \n"
              f"Role of employee : {self.role}")
    @classmethod
    def from_str(cls, string):
        return cls(*string.split("-"))
    @classmethod
    def change_leaves(cls, new_l):
        cls.no_of_leaves = new_l

sohail = employee.from_str("sohail-8907-role")


rehan = employee.from_str("rehan-46789-instructor")
# rehan.change_leaves(12)
# print(sohail.no_of_leaves)
class programmer(employee):
    def __init__(self,aname,asalary,arole,alanguages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language = alanguages
    def printprog(self):
        print(f"Programmer's name is : {self.name} \n Salary of employee : {self.salary} \n"
              f"Role of employee : {self.role} \n languages : {self.language}")

anu = programmer.from_str("anu-467890-programmer-[python,c++]")
anu.printprog()


