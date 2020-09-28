import random

highest =1000
answer=random.randint(1,highest)
print(answer)
guess=0

print("Please guess number between 1 and {}: ".format(highest))


while guess!=answer:
    guess=int(input())


    if guess==0:
        break
    if guess==answer:
        print("you did correct")
        break
    else:
        if guess>answer:
            print("guess lower")
        else:
            print("guess higher")
