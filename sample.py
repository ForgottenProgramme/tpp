import random
myNumber= random.randint(1,10)
print("I am thinking of a number between 1 and 10. Make a guess!")

for guessesMade in range (1, 7):
    guess = int(input())
    if guess<myNumber:
        print("you guessed too low")
    elif guess>myNumber:
        print("you guessed too high")
    else:
        break

if guess == myNumber:
    print(f"That's right! You guessed the number in {guessesMade} attempts")
else:
    print(f"you have exhausted your attempts. Sorry.")