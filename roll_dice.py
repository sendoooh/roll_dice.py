import random
import time

print("Hi there!")
print("-----------------------------------------------")
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print("-----------------------------------------------")

start_time = time.time()

def generate_unique_4digit_number():
    while True:
        number = random.randrange(1000, 10000)
        digits = str(number)
        if len(set(digits)) == 4:
            return [int(d) for d in digits]

def bulls_and_cows(secret, guess):  
    bulls = 0
    cows = 0
    secret_copy = secret[:]
    guess_copy = guess[:]

    # First, count bulls
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
            secret_copy[i] = None
            guess_copy[i] = None

    # Then, count cows
    for i in range(4):
        if guess_copy[i] is not None and guess_copy[i] in secret_copy:
            cows += 1
            secret_copy[secret_copy.index(guess_copy[i])] = None  # Remove the matched cow

    return bulls, cows

skryté_číslo = generate_unique_4digit_number()

attempts = 0

while True:
    try:
        uguess_number = int(input("Enter a number: "))
        uguess_number = str(uguess_number)
        if not uguess_number.isdigit() or len(uguess_number) != 4:
            print("Please enter a 4 digit number.")      
            continue

        guess = [int(a) for a in uguess_number]
        attempts += 1

        bulls, cows = bulls_and_cows(skryté_číslo, guess)
        print(f"{bulls} bulls, {cows} cows")
        
        if bulls == 4:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            print(f"It took you {elapsed_time:.2f} seconds.")
            break

    except ValueError:
        print("Invalid digits")

    print("-----------------------------------------------")
