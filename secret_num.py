import datetime
import json
import random
import operator

player = input("Hello!!!. What is your name: ")

secret = random.randint(1, 30)
attempts = 0

with open("score_list.txt") as score_file:
    score_list = json.loads(score_file.read())

score_list.sort(key=operator.itemgetter("attempts"))

for score_dic in score_list[:3]:
    score_text = "Player {0} had {1} attempts on {2}. The secret number was {3}. The wrong guesses were {4}"\
        .format(score_dic.get("player"),
                str(score_dic.get("attempts")),
                score_dic.get("date"),
                score_dic.get("secret"),
                score_dic.get("wrong_guesses"))

    print(score_text)

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1
    wrong_guess = (attempts - 1)

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        score_data = ({"player": player,
                       "attempts": attempts,
                       "date": str(datetime.datetime.now()),
                       "secret": secret, "wrong_guesses": wrong_guess})

        score_list.append(score_data)

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")