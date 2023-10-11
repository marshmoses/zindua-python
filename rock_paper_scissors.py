import random

choices = ['Rock', 'Paper', 'Scissors']

def choices_winner(marsh, computer):
    if (marsh == "Rock" and computer == "Paper"):
        print("You lost the bet!")
        return "computer"
    elif (marsh == "Rock" and computer == "Scissors"):
        print("Congratulations! You win the bet!")
        return "marsh"
    elif (marsh == "Scissors" and computer == "Paper"):
        print("Congratulations! You win the bet!")
        return "marsh"
    elif (marsh == "Scissors" and computer == "Rock"):
        print("You lost the bet!")
        return "computer"
    elif (marsh == "Paper" and computer == "Rock"):
        print("Congratulations! You win the bet!")
        return "marsh"
    elif (marsh == "Paper" and computer == "Scissors"):
        print("You lost the bet!")
        return "computer"
    else:
        print("It's a draw, retry!")
        return "Tie"

marshScore = 0
computerScore = 0
tieScore = 0

while True:
    marsh = input("Enter your choice (Rock/Paper/Scissors): ").capitalize()
    
    if marsh not in choices:
        print("Invalid input. Try again.")
        continue
    
    computer = random.choice(choices)
    print("Your hand:", marsh)
    print("Computer hand:", computer)
    
    result = choices_winner(marsh, computer)
    
    if result == "marsh":
        marshScore += 1
    elif result == "computer":
        computerScore += 1
    else:
        tieScore += 1
    
    print("Your score:", marshScore, "Computer score:", computerScore, "Draw:", tieScore)
    
    play_again = input("Do you want to play again? : ").lower()
    if play_again != "yes":
        break


print("Game over! Thank you for playing.")
