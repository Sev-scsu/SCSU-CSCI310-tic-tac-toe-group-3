import random

nums = list(range(1, 10)) #number of spots available in tic tac toe board

def pick_number(numbers):
    if not numbers:
        return None  # no numbers left
    choice = random.choice(numbers)
    numbers.remove(choice)
    return choice



def main():
    nums = list(range(1, 10))  

    print(pick_number(nums))  # random number from 1–9
    print(nums)               # list now has one less number

    return 0

if __name__ == "__main__":
    main()




def print_board(board, x_positions, o_positions):
    """
    Prints the current state of the Tic-Tac-Toe board without numbers.
    The positions for 'X' and 'O' are determined by the x_positions and o_positions lists.
    
    board: A list of size 9 (indicating the 9 board positions).
    x_positions: A list of indices where 'X' is placed.
    o_positions: A list of indices where 'O' is placed.
    """
    # Create a board with empty spaces
    board_layout = [' '] * 9

    # Place 'X' and 'O' in their respective positions
    for x in x_positions:
        board_layout[x] = 'X'
    for o in o_positions:
        board_layout[o] = 'O'

    # Print the board
    print("\nTic-Tac-Toe Board:")
    for i in range(0, 9, 3):
        print(" | ".join(board_layout[i:i+3]))
        if i < 6:
            print("-" * 5)  # Print a separator line
