import random
import threading
import time

numbers = list(range(1, 10)) #number of spots available in tic tac toe board
lock = threading.Lock()

def pick_number(name):
    global numbers
    while True:
        with lock:  # only one thread at a time can access the list
            if not numbers: #if the list is empty
                break
            choice = random.choice(numbers)
            numbers.remove(choice)
            print(f"{name} picked {choice}, remaining: {numbers}")

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

def main():

    t1 = threading.Thread(pick_number("t1")) #creating a thread object that will run pick_number function
    t2 = threading.Thread(pick_number("t2"))

    t1.start() #this activates the thread
    t2.start()
    t1.join() #this will wait for t1 to finish before proceeding
    t2.join()
    

    return 0

if __name__ == "__main__":
    main()
