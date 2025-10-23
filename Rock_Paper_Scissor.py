import random as rd
game = ("ROCK","PAPER","SCISSOR")
score = 0
computer_score = 0
for i in range(0,10):
    guess = rd.choice(game)
    user_guess=""
    while True:
        if user_guess not in game:
            user_guess = input("Enter (ROCK, PAPER, OR SCISSOR): ").upper()
        else:
            break
    if user_guess == guess:
        print(f"{user_guess} Same as {guess}")
        print("Its Same 🙂")
        continue
    elif (user_guess=="ROCK" and guess == "SCISSOR") or (user_guess=="PAPER" and guess == "ROCK") or (user_guess == "SCISSOR" and guess == "PAPER"):
        score+=1
        print(f"Yours {user_guess} cuts Opponents {guess}")
        print("You Scored 🥳")
    else:
        computer_score +=1
        print(f"Opponents {guess} cuts Yours {user_guess}")
        print("Opponent Scores 😔")
print(f"Your Score : {score}\nOpponent Score : {computer_score}")
if computer_score > score:
    print(f"Opponent Wins by {computer_score-score} points 😔😔😔")
elif computer_score < score:
    print(f"You Won the game by {score-computer_score} points 🥳🥳🥳")
else:
    print("Its a DRAW 😊😊😊")