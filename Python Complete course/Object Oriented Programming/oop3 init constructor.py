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

    pass

rehan = employee("Rehan",5668,"Instructor")
rehan.changeleaves(45)
print(rehan.no_of_leaves)

