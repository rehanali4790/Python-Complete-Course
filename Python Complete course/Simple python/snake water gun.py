import random
game_ = ["snake","water","gun"]
choice_ = random.choice(game_)
print("lets play water ,snake, Gun game \n choose your action \n")
action_ = input("write snake, water or gun \n")
if action_ == "snake" and choice_ == "water":
    print("You win the choice was", choice_)
elif action_ == "water" and choice_ == "gun":
    print("You win the choice was", choice_)
elif action_ == "water" and choice_ == "snake":
    print("you lose the choice was", choice_)
elif action_ == "snake" and choice_ == "gun":
    print("you lose the choice was", choice_)
elif action_ == "gun" and choice_ == "water":
    print("you lose the choice was", choice_)
elif action_ == "gun" and choice_ == "snake":
    print("You win the choice was", choice_)
elif action_ == choice_:
    print("game draw you both choose the same")
else:
    print("invalid action")
input()
