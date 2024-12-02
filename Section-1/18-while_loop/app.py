guess =  0
answer = 5

while answer != guess:
    guess = int(input("Guess: "))
    if guess == answer:
        print("You guessed it!")
    else:
        print("Try again")