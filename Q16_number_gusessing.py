#number guessing

import random
b_score = None
while True:
    n = random.randint(1, 100)
    attempts = 5
    use_attempts = 0

    print("no guessing game")
    print("you have 5 attempts to guess the no. between 1 and 100")
    while attempts > 0:
        guess = int(input("enter your guess:"))
        use_attempts += 1

        if guess == n:
            print("congratulations! you guessed the number in", use_attempts, "attempts.")
            if b_score is None or use_attempts < b_score:
                b_score = use_attempts
                print("new best score:", b_score)
            break
        attempts -= 1
        if guess < n:
            print("too low! attempts left:", attempts)
        else:
            print("too high! attempts left:", attempts)
    if attempts == 0:
        print("game over! the number was", n)
    play_again = input("do you want to play again? (yes/no):")
    if play_again.lower() != "yes":
        print("thanks for playing! your best score was:", b_score)
        break
        
        