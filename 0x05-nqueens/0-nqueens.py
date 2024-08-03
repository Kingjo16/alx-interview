#!/usr/bin/python3
"""Module for an N queens puzzle solver."""
import sys


results = []
"""A list containing all the valid solutions for the N queens problem."""
board_size = 0
"""The dimension of the chessboard."""
positions = None
"""A list storing the possible positions on the chessboard."""


def parse_arguments():
    """Parses and validates the command line arguments.

    Returns:
        int: The dimension of the chessboard.
    """
    global board_size
    board_size = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        board_size = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)
    return board_size


def are_queens_attacking(queen1, queen2):
    """Determines if two queens are in attacking positions.

    Args:
        queen1 (list or tuple): The position of the first queen.
        queen2 (list or tuple): The position of the second queen.

    Returns:
        bool: True if the queens can attack each other, else False.
    """
    if (queen1[0] == queen2[0]) or (queen1[1] == queen2[1]):
        return True
    return abs(queen1[0] - queen2[0]) == abs(queen1[1] - queen2[1])


def solution_exists(solution_group):
    """Checks if a solution is already in the list of results.

    Args:
        solution_group (list of integers): A set of queen positions.

    Returns:
        bool: True if the solution already exists, otherwise False.
    """
    global results
    for result in results:
        count = 0
        for res_pos in result:
            for sol_pos in solution_group:
                if res_pos[0] == sol_pos[0] and res_pos[1] == sol_pos[1]:
                    count += 1
        if count == board_size:
            return True
    return False


def generate_solution(current_row, current_solution):
    """Generates solutions for the."""
    global results
    global board_size
    if current_row == board_size:
        tmp_solution = current_solution.copy()
        if not solution_exists(tmp_solution):
            results.append(tmp_solution)
    else:
        for column in range(board_size):
            index = (current_row * board_size) + column
            potential_matches = zip(list([positions[index]]) * len(current_solution), current_solution)
            attack_positions = map(lambda x: are_queens_attacking(x[0], x[1]), potential_matches)
            current_solution.append(positions[index].copy())
            if not any(attack_positions):
                generate_solution(current_row + 1, current_solution)
            current_solution.pop(len(current_solution) - 1)


def find_solutions():
    """Finds all the solutions for the N queens problem."""
    global positions, board_size
    positions = list(map(lambda x: [x // board_size, x % board_size], range(board_size ** 2)))
    start_row = 0
    initial_solution = []
    generate_solution(start_row, initial_solution)


board_size = parse_arguments()
find_solutions()
for solution in results:
    print(solution)
