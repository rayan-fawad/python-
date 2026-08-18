import random

easy_words = ["cat", "dog", "sun", "ball", "book"]
medium_words = ["apple", "river", "table", "tiger", "garden"]
hard_words = ["elephant", "computer", "python", "mountain", "hospital"]

print("=== Welcome To Password Guessing Game ===")
input("Press Enter to Start...")

while True:

    difficulty = input("\nChoose Difficulty (easy/medium/hard): ").lower()

    if difficulty == "easy":
        word = random.choice(easy_words)

    elif difficulty == "medium":
        word = random.choice(medium_words)

    elif difficulty == "hard":
        word = random.choice(hard_words)

    else:
        print("Invalid difficulty!")
        continue

    attempts = 0
    hints_used = 0

    print("\nGuess the secret word!")

    while True:

        guess = input("Enter your guess: ").lower()
        attempts += 1

        if guess == word:
            print("\n🎉 Congratulations!")
            print("Correct word:", word)
            print("Attempts:", attempts)
            print("Hints Used:", hints_used)
            break

        else:
            hints_used += 1

            # count correct letters in correct position
            correct_count = 0

            for i in range(min(len(guess), len(word))):
                if guess[i] == word[i]:
                    correct_count += 1

            print("\nHint:")
            print(f"- Word has {len(word)} letters")
            print(f"- Correct letters in correct position: {correct_count}")

    again = input("\nDo you want to continue? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing!")
        break