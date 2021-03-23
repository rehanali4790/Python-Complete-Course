class employee:
    #this is the class variable
    no_of_leaves = 8
    pass

rehan = employee()
ali = employee()
#this is the instance variable
rehan.name = "Rehan"
rehan.sal = 4556
rehan.role = "Python developer"
employee.no_of_leaves = 10

ali.name = "ali"
ali.sal = 45567
ali.role = "developer"
ali.no_of_leaves = 8
print(employee.__dict__)
