#list1 = [["larry",5], ["carry",7], ["marie",8]]
#dict1= dict(list1)

#for item,lollypop in dict1.items():
 #   print(item,lollypop)
list1 = [4,6,7,8,9,"pens",'pencils','erassers',2]
for item in list1:
    if str(item).isnumeric() and item > 6:
        print(item)
