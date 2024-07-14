import rock_paper_scissors
import number_guessing_game
import hangman
import multiplayer_dice_game

def main():
    descriptions = {
        '1': {
            'name': 'Rock Paper Scissors',
            'type': 'Single Player',
            'description': 'A classic game where you choose rock, paper, or scissors and try to beat the computer.'
        },
        '2': {
            'name': 'Number Guessing Game',
            'type': 'Single Player',
            'description': 'Guess the randomly chosen number between 1 and 100. You have 5 attempts to guess correctly.'
        },
        '3': {
            'name': 'Hangman',
            'type': 'Single Player',
            'description': 'Guess the letters in a secret word. You have 6 attempts to guess the word correctly.'
        },
        '4': {
            'name': 'Multiplayer Dice Game',
            'type': 'Multiplayer',
            'description': 'Two players choose a number below 21. A random dice roll is added to their chosen number. The highest number wins unless it exceeds 21.'
        }
    }

    while True:
        print("\nChoose a game to play:")
        for key, info in descriptions.items():
            print(f"{key}. {info['name']} ({info['type']})")
            print(f"   Description: {info['description']}")
        
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            rock_paper_scissors.rock_paper_scissors()
        elif choice == '2':
            number_guessing_game.number_guessing_game()
        elif choice == '3':
            hangman.hangman()
        elif choice == '4':
            multiplayer_dice_game.multiplayer_dice_game()
        elif choice == '5':
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
