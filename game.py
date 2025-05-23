from random import choice


# determine the result of the round
def winner(user, computer):
    if user == computer:
        return "tie"

    elif (user == 'Rock' and computer == 'Scissors') or \
            (user == 'Scissors' and computer == 'Paper') or \
            (user == 'Paper' and computer == 'Rock'):
        return "user wins"

    else:
        return "computer wins"


def main():
    rounds = 5
    user_scores = 0
    computer_scores = 0
    choices = ['Rock', 'Paper', 'Scissors']

    # introducing the rules
    rules = '''Rules: 2 points for a win, \
1 point for a tie, no points for a loss.\
A total of 5 games will be played, \
and the one with the higher scores at the end will win.\n'''

    print("Welcome to the 'rock-paper-scissors'game!\n")
    print(rules)

    # get user's input
    for num in range(1, rounds + 1):
        print(f"This is Round{num}")
        user_choice = input("What is your choice (Rock/Paper/Scissors)? ")

        # prompt for input error
        if user_choice not in choices:
            print("Error input: please choose Rock/Paper/Scissors")

        # computer generate choice randomly
        else:
            computer_choice = choice(['Rock', 'Paper', 'Scissors'])
            print(f"The computer's choice is {computer_choice}")
            print()

        # calculate scores and announce the result of this round
        result = winner(user_choice, computer_choice)
        if result == "user wins":
            user_scores += 2  # two ponits for winning this round
            print("You win this round!")

        elif result == "computer wins":
            computer_scores += 2
            print("You lose this round")

        else:
            user_scores += 1  # one point for a tie
            computer_scores += 1
            print("This is a tie!")

        # show current scores
        print(f"Current score: \
user = {user_scores}, computer = {computer_scores}\n")

    # show final scores
    print("Game over.")
    print(f"The final score: \
user = {user_scores}, computer = {computer_scores}")

    # compare final scores to determine winners and losers
    if user_scores > computer_scores:
        print("\nCongratulations! You won the game!")

    elif user_scores < computer_scores:
        print("\nUnfortunately, you lost.")

    else:
        print("\nThis is a tie!")


if __name__ == "__main__":
    main()
