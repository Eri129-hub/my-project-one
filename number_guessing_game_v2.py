import random

answer = random.randint(1, 10)

count = 0

while count < 3:

    guess = int(input("Guess a number (1-10): "))

    count = count + 1

    if guess == answer:

        print("🎉 Correct!")

        break

    elif guess < answer:

        print("📉 Too Low!")

    else:

        print("📈 Too High!")

if guess != answer:

    print("❌ Game Over!")

    print("The answer was", answer)