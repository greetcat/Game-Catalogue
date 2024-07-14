import random

def multiplayer_dice_game():
    print("Welcome to the Multiplayer Dice Game!")
    while True:
        player1 = int(input("Player 1, choose a number below 21: "))
        player2 = int(input("Player 2, choose a number below 21: "))
        
        dice_roll1 = random.randint(1, 6)
        dice_roll2 = random.randint(1, 6)
        
        player1_total = player1 + dice_roll1
        player2_total = player2 + dice_roll2
        
        print(f"Player 1 chose {player1} and rolled {dice_roll1}. Total: {player1_total}")
        print(f"Player 2 chose {player2} and rolled {dice_roll2}. Total: {player2_total}")
        
        if player1_total > 21 and player2_total > 21:
            print("Both players exceeded 21. Both players lose.")
        elif player1_total > 21:
            print("Player 1 exceeded 21. Player 1 loses.")
        elif player2_total > 21:
            print("Player 2 exceeded 21. Player 2 loses.")
        else:
            if player1_total > player2_total:
                print("Player 1 wins!")
            elif player2_total > player1_total:
                print("Player 2 wins!")
            else:
                print("It's a tie!")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
