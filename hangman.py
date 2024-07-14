import random
import string

def hangman():
    print("Welcome to Hangman!")
    words = ['python', 'programming', 'hangman', 'game', 'computer']
    secret_word = random.choice(words)
    guessed_letters = set()
    attempts = 6
    
    while attempts > 0:
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in secret_word])
        print(f"Word: {display_word}")
        print(f"Attempts left: {attempts}")
        
        if '_' not in display_word:
            print("Congratulations! You guessed the word.")
            break
        
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("Invalid input! Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue
        
        guessed_letters.add(guess)
        
        if guess not in secret_word:
            attempts -= 1
            print("Incorrect guess!")
        
    else:
        print(f"Sorry, you're out of attempts. The word was '{secret_word}'.")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        hangman()
