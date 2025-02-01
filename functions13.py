import random

def guess_the_number():
    print("name?")
    name = input()
    
    print(f"{name} number between 1 and 20.")
    number_to_guess = random.randint(1, 20)
    
    guess_count = 0
    while True:
        print("guess.")
        guess = int(input())
        guess_count += 1
        
        if guess < number_to_guess:
            print("too low.")
        elif guess > number_to_guess:
            print("too high.")
        else:
            print(f"Good job {name}! You guessed {guess_count} times")
            break

guess_the_number()
