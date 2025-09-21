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