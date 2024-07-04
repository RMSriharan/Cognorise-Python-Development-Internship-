import random

def hangman():
    words = ["python", "hangman", "challenge", "programming"]
    word = random.choice(words)
    guessed = "_" * len(word)
    attempts = 6
    guessed_letters = []

    while attempts > 0 and guessed != word:
        guess = input(f"Word: {guessed}\nEnter a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            guessed = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print(f"Incorrect! Attempts left: {attempts}")

    if guessed == word:
        print(f"Congratulations! You've guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")

hangman()
