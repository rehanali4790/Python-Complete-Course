class employee:
    #this is the class variable
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    def print_det(self):
        return f"following are the details of employee \n Name : {self.name} \n" \
               f"salary is : {self.salary} \n Role : {self.role} "
    no_of_leaves = 8
    @classmethod
    def changeleaves(cls, new_l):
        cls.no_of_leaves = new_l
    @classmethod
    def from_str(cls, string):
        param_ = string.split("-")
        return cls(*string.split("-"))
    @staticmethod
    def printgood(string):
        print(string + "is a good boy")

    pass

rehan = employee("Rehan",5668,"Instructor")
ali = employee("ali", 6778,"stu")
samo = employee.from_str("samo-67778-student")
rehan.printgood("rehan")