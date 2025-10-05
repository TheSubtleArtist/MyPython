import argparse

rules = {
    frozenset(("rock", "scissors")): ("rock", "crushes"),
    frozenset(("scissors", "paper")): ("scissors", "cuts"),
    frozenset(("paper", "rock")): ("paper", "covers"),
}

options = {"rock", "paper", "scissors"}

def rock(player1, player2):
    """Return the result of a rock-paper-scissors game.

    Returns:
        None for a tie
        (winner, action, loser) tuple for a win
    """
    if player1 not in options or player2 not in options:
        raise ValueError("Invalid input")

    if player1 == player2:
        return None

    winner, action = rules[frozenset((player1, player2))]
    loser = player2 if winner == player1 else player1
    return (winner, action, loser)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("player1", choices=options)
    parser.add_argument("player2", choices=options)
    args = parser.parse_args()

    print("Player 1 played", args.player1)
    print("Player 2 played", args.player2)
    print()

    try:
        result = rock(args.player1, args.player2)
    except ValueError as e:
        print(e)
    if result is None:
        print("It's a tie")
    else:
        winner, action, loser = result
        print(winner.capitalize(), action, loser)
        print()
        if winner == args.player1:
            print("Player 1 wins")
        else:
            print("Player 2 wins")

if __name__ == "__main__":
    main()