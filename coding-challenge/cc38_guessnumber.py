import random
def guess_a_number():
    guess_count = 0
    number = random.randint(1,10)
    while guess_count<3:
        user_guess = int(input("guess the number: "))
        if user_guess < number:
            print("number too low")
        elif user_guess > number:
            print("number too high")
        elif user_guess == number:
            return "Winner!"
        guess_count += 1
    return"Loser"
print(guess_a_number())