statements_n = 9
while statements_n > 0:
    statements_n -=1
    print("Number of tries left", statements_n)
    print("Please guess the number")
    n = int(input())
    if statements_n >0:
        if n > 18 and n > 25:
            print("Your number is too much bigger\n" + "please try again")
            statement = input("press y for try again")
            if statement == "y":
                continue
            else:
                break
        elif n > 18 and n < 25:
            print("number is slightly much bigger \n" + "please try again")
            statement = input("press y for try again \t")
            if statement == "y":
                continue
            else:
                break
        elif n < 18 and n < 10:
            print("number is too much lesser \n" + "please try again")
            statement = input("press y for try again \t")
            if statement == "y":
                continue
            else:
                break
        elif n < 18 and n > 10:
            print("number is slightly much lesser \n" + "please try again")
            statement = input("press y for try again \t")
            if statement == "y":
                continue
            elif n == 18:
                print("Congratulations you win You guess right" + n)
                break
            else:
                break
    else:
        print("sorry game over no tries left")
