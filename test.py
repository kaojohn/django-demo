import random

# 1~50
x = random.randint(1, 50)
for i in range(5):
    y = int(input("your 答え："))

    if x == y:
        print("YES!!GOOD!! LOVE AND PICE")
        break
    else:
        print("ON~NO!!")
        if x > y:
            print("big")
        else:
            print("すも")
