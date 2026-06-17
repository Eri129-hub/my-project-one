import random

answer = random.randint(1, 10)

guess = int(input("Guess a number (1-10): "))

if guess == answer:

    print("🎉 Correct!")

else:

    print("❌ Wrong!")

    print("The answer was", answer)