import random

def roll_dice():
    return random.randint(1, 6)

def main():
    player1 = input("Enter Your Name: ")
    player2 = input("Enter Opponent's Name: ")

    player1_score = 0
    player2_score = 0
    num_rounds = 3

    for round in range(1, num_rounds + 1):
        print(f"\nRound {round}:")

        input(f"{player1}, press Enter to roll the dice !!")
        player1_roll = roll_dice()
        print(f"{player1} rolled a {player1_roll}")
        player1_score += player1_roll

        input(f"{player2}, press Enter to roll the dice !!")
        player2_roll = roll_dice()
        print(f"{player2} rolled a {player2_roll}")
        player2_score += player2_roll

    print("\nGame Over!\n")
    print(f"{player1} scored a total of {player1_score}")
    print(f"{player2} scored a total of {player2_score}")

    if player1_score > player2_score:
        print(f"Congrats, {player1} wins!")
        print(f"{player2} Better Luck Next Time\n")
    elif player2_score > player1_score:
        print(f"Congrats, {player2} wins!")
        print(f"{player1} Better Luck Next Time\n")
    else:
        print("It's a tie!\n")

if __name__ == '__main__':
    main()
