import pickle

# cars = ["audi","ferrari","mercedez"]
#
# file = "cars.pkl"
# fileob = open(file, "wb")
# pickle.dump(cars, fileob)
# fileob.close()
file = "cars.pkl"
fileob = open(file, 'rb')
mycar_ = pickle.load(fileob)
print(mycar_)