import random
import threading
import time

# Global variables
board_layout = [' '] * 9           # 3x3 Tic-Tac-Toe board
lock = threading.Lock()
game_over = False
numbers = list(range(0, 9))  # number of spots available in Tic-Tac-Toe board

# Winning combinations (indices)
win_conditions = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
    [0, 4, 8], [2, 4, 6]              # diagonals
]

def check_winner(player):
    """Check if the given player ('X' or 'O') has won."""
    for combo in win_conditions: # iterate through each list in win_conditions
        if all(board_layout[i] == player for i in combo): # Check if all values at the given indices
                                                            # in board_layout match the player's name
            return True
    return False


def pick_number(player):
    """Thread function: player makes random moves until game ends."""
    global numbers, game_over
    while not game_over:
        with lock:  # only one thread at a time can access the list
            if game_over:
                break

            # Find available moves
            available = [i for i, cell in enumerate(board_layout) if cell == ' ']
            if not available:
                print("Game Over! It's a draw.")
                game_over = True
                break

            # Player picks a random move
            choice = random.choice(numbers)
            numbers.remove(choice)
            board_layout[choice] = player
            print(f"{player} picked {choice}, remaining: {numbers}")
            print_board()

            # Check for win
            if check_winner(player):
                print(f"Game Over! Player {player} wins!")
                game_over = True
                break

        time.sleep(1)  # Small delay so threads alternate

def print_board():
    global board_layout
    # Print the board
    print("\nTic-Tac-Toe Board:")
    for i in range(0, 9, 3):  #Take a number from 0 to 9 every 3 steps, excluding 9
        print(" | ".join(board_layout[i:i + 3]))
        if i < 6:
            print("-" * 10)  # Print a separator line
    print() # print new line

def main():
    t1 = threading.Thread(target=pick_number, args=("X",))  # creating a thread object that will run pick_number function
    t2 = threading.Thread(target=pick_number, args=("O",))

    t1.start()  # this activates the thread
    t2.start()
    t1.join()  # this will wait for t1 to finish before proceeding
    t2.join()

    return 0


if __name__ == "__main__":
    main()
