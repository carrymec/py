import random

sec = random.randint(1, 10)
temp = input("input num:")
guess = int(temp)
x = 0
while guess != sec:
    temp = input("input num again:")
    guess = int(temp)
    if guess == sec:
        print("ok")
    else:
        x = x + 1
        if guess < sec and x < 3:
            print("small")
        else:
            if x > 3:
                break
            print("bigger")
print("over")
