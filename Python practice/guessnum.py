import random
num = random.randint(1,20)
while True:
    g = int(input("Enter Guess No: "))
    if g==num:
        print("you are correct")
        break
    elif g>num:
        print("you choose > num")
    elif g<num:
        print("you choose < num")