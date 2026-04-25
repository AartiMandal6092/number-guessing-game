import random as rd

random_number = rd.randint(1, 100)
print("\n" + "=" * 40)
print(" 🎯 Welcome to Number Guessing Game 🎯")
print("=" * 40)
print("\nI have selected a number between 1 and 100")
print("Try to guess it! 🔍")
attempt = 0
while True:
    attempt += 1
    guess = int(input(" Enter your guess : "))
    if guess == random_number:
        print("\n🎉 Congratulations! You guessed it!")
        print(f"You took {attempt} attempts 🧠")
        break
    elif guess > random_number:
        print(" 📈 Too High , try again ")
    else:
        print(" 📉 Too low , try again ")