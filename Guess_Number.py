import random as rdm

life = int(input("Enter No.of.life : "))
total_score=0
while life!=0:
    number = rdm.randint(1,10)
    guess=int(input("Guess the Number (1 - 10) : "))
    if guess == number:
        print(f"You are Right {guess} is the correct 👍")
        total_score+=1
    else:
        life-=1
        print(f"You are Wrong! 😔 The number is {number}")
        print(f"{life} 💖 Remaining....")
print(f"Total Score : {total_score}")