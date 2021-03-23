import time
initial = time.time()
k = 0
while k < 45:

    print("Iam rehan")
    time.sleep(2)
    k += 1
print(f"while loop ran in {time.time() - initial} seconds")
initial2 = time.time()
for i in range(45):
    print("rehan im")
print(f"for loop ran in {time.time() - initial} seconds")
# local_time = time.asctime(time.localtime(time.time()))
# print(local_time)
