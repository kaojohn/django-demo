import random

# 1~50

start = 1
end = 50


x = random.randint(start, end)

for i in range(5):
    y = int(input(f"find number {start}~{end} your 答え："))

    if x == y:
        print("YES!!GOOD!! LOVE AND PICE")
        break
    else:
        print("ON~NO!!")
        if x > y:
            print("big!!")
            if start < y:
                start = y + 1
        else:
            if end > y:
                end = y - 1
            print("すも!!")
if i == 4:
    print(f"ans:{x}!!!")
