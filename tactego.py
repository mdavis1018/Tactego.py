"""
File:    tactego.py
Author:  Marcus Davis
Date:    11/29/2023
Section: 58-Dis(8021)
E-mail:  marcusd2@umbc.edu
Description: creates a tactego game and allows two teams to play
"""

import random


def tactego(pieces_file, length, width):
    """
    Tactego is the main function in my code. This function is used to run the game.
    :param pieces_file: the file that holds the data for the pieces in the game. User chooses this file.
    :param length: user inputed desired length dimension of tactego board
    :param width: user inputed desired width dimension of tactego board
    """
    board = initialize_board(length, width)
    values_array = read_file(pieces_file)
    place_random_pieces(board, values_array)
    draw_board(board)
    players = ['Red', 'Blue']

    # end game logic. If the game over is true then the code calls the take_turn function until is_game_over is false
    if is_game_over:
        take_turn(board, players)
    print("Game Over")


def is_game_over(board):
    """
    is_game_over determines if the game will run. Tests to see if a win condition has been met.
    :param board: the 2d list containing the that is used to create the board
    """
    # checks to see if there are any Red/Blue pieces left on the board respectively that aren't the flag or a mine
    red_pieces_remaining = any(cell.startswith(
        'R') and cell != 'RF' and cell != 'RM' for row in board for cell in row)
    blue_pieces_remaining = any(cell.startswith(
        'B') and cell != 'BF' and cell != 'BM' for row in board for cell in row)

    # Checks if the flags are not on the board
    red_flag_missing = not any('RF' in row for row in board)
    blue_flag_missing = not any('BF' in row for row in board)

    if not (red_pieces_remaining and blue_pieces_remaining) or (red_flag_missing or blue_flag_missing):
        # if one of the game over conditions is met
        if blue_flag_missing:
            print("The Red Team has Won!")
        if red_flag_missing:
            print("The Blue Team has Won!")
        if not (blue_pieces_remaining):
            print("The Red Team has Won!")
        if not (red_pieces_remaining):
            print("The Blue team has Won!")
        return True  # Game over condition


def initialize_board(length, width):
    """
    initialize_board fills in the board with empty strings using the dimensions of the board
    :param length: the user inputed length
    :param width: the user inputed width
    """
    return [['  ' for _ in range(width)] for _ in range(length)]


def draw_board(board):
    """
    draw_board draws the board using the 2d list created
    :param board: the 2d list created using the initialze_board function
    """
    # Print column numbers
    print("\t", end="")
    for col in range(len(board[0])):
        print(f"{col}\t", end="")
    print()

    # Print board with row numbers
    for row_num, row in enumerate(board):
        print(f"{row_num}\t", end="")
        for cell in row:
            print(f"{cell}\t", end="", sep="")
        print()


def read_file(file_name):
    """
    read_file reads the user inputed file that contains the pieces to play with.
    :param file_name: the user inputed file that contains the pieces to play with
    """
    # Open the file in read mode
    with open(file_name, 'r') as file:
        value_array = []
        for line in file:
            # Split each line into a list of values
            values = line.split()
            value_array.append(values)

            # Process the values based on your requirements
            if values[0] == 'F':
                # Handle case where the first value is 'F'
                {values[1]}
            elif values[0] == 'A':
                # Handle case where the first value is 'A'
                {values[1]}
            elif values[0] == 'S':
                # Handle case where the first value is 'A'
                {values[1]}
            elif values[0] == 'M':
                # Handle case where the first value is 'A'
                {values[1]}
            else:
                # Process other cases
                value1 = int(values[0])
                value2 = int(values[1])

    final_array = red_blue_values(value_array)
    return final_array  # returning final_array to be passed to another function


def red_blue_values(values):
    """
    red_blue_values takes in the values list containing read and blue pieces values and splits them into a 2d list containing the red and blue values separately
    :param values: a 2d list containing all pieces values
    """
    red_blue_array = []
    for i in range(len(values)):
        for j in range((int(values[i][1]))):
            red_blue_array.append(f"R{values[i][0]}, B{values[i][0]}")
    new_array = []
    for i in range(len(red_blue_array)):
        new_array.append(red_blue_array[i].split(","))
    return new_array


def place_random_pieces(board, values_array):
    """
    place_random_pieces places a randomized shuffle of red and blue pieces onto the board
    :param board: the 2d list created using the initialze_board function
    :param values_array: the list containing red and blue piece values
    """
    # puts all pieces that start with the letter "R" into the red values list
    red_values = [
        item for sublist in values_array for item in sublist if item.startswith('R')]
    # puts all pieces that start with the letter "B" into the red values list
    blue_values = [item.replace(
        ' ', '') for sublist in values_array for item in sublist if item.startswith(' B')]

    # Place red pieces randomly within the top half of the board
    for i in range(len(board) // 2):
        for j in range(len(board[0])):
            if red_values:
                chosen_value = random.choice(red_values)
                board[i][j] = chosen_value
                red_values.remove(chosen_value)

    # Place blue pieces randomly within the bottom half of the board
    for i in range(len(board) - 1, len(board) // 2 - 1, -1):
        for j in range(len(board[0])):
            if blue_values:
                chosen_value = random.choice(blue_values)
                board[i][j] = chosen_value
                blue_values.remove(chosen_value)


def take_turn(board, player):
    """
    take_turn alternates between the two players and allows them to move their pieces on the board and
    attempt to win
    :param board: the 2d list created using the initialze_board function
    :param player: the list containing the two game players
    """
    player_1 = player[0]
    player_2 = player[1]
    players_turn = player_1

    # entering the loop that alternates between the two players allowing them to take turns until one has fulfilled a win condition
    while True:
        if (players_turn == "Red"):
            print("Red player's turn")
            piece_row = int(
                input("Select piece to move by position (Enter row): "))
            piece_column = int(
                input("Select piece to move by position (Enter column): "))

            # conditions for allowable selected piece
            while not (0 <= piece_row < length and 0 <= piece_column < width and
                       board[piece_row][piece_column][0] == "R" and
                       not board[piece_row][piece_column] == "RF" and
                       not board[piece_row][piece_column] == '  ' and
                       not board[piece_row][piece_column] == "RM"):

                print(
                    "Invalid move. The selected piece does not belong to your team. Try again.")
                piece_row = int(
                    input("Select piece to move by position (Enter row): "))
                piece_column = int(
                    input("Select piece to move by position (Enter column): "))

            move_row = int(
                input("Enter a row coordinate to move the piece to: "))
            move_column = int(
                input("Enter a column coordinate to move the piece to: "))

            # conditions for allowable location to move piece to
            while not (abs(piece_row - move_row) <= 1 and abs(piece_column - move_column) <= 1 and board[move_row][move_column][0] != "R"):
                print("Invalid move. You can only move one square at a time and you cannot move to a square that has your piece on it.")
                move_row = int(
                    input("Enter a row coordinate to move the piece to: "))
                move_column = int(
                    input("Enter a column coordinate to move the piece to: "))

            red_piece = board[piece_row][piece_column]
            location = board[move_row][move_column]

            if (red_piece == "RS"):  # logic for if the piece selected is the sapper
                if (location == "  "):
                    board[move_row][move_column] = red_piece
                elif (location == "BS" or location == "BA" or location == "BF" or location == "BM"):
                    board[move_row][move_column] = red_piece
                elif (location != "BS" or location != "BA" or location != "BF" or location != "BM"):
                    board[move_row][move_column] = location
            else:
                # logic for if the selected piece is an assassin
                if (red_piece == "RA" and location != "BM"):
                    board[move_row][move_column] = red_piece
                else:
                    # Assassin and flag are always defeated in combat
                    if (location == "BF" or location == "BA"):
                        board[move_row][move_column] = red_piece
                    else:
                        # logic for if the position the piece is moving to is occupied by a Blue Piece
                        if (location[0] == "B"):
                            if (location == "BM"):
                                board[move_row][move_column] = "  "
                            else:
                                if (location == "BS"):  # sappers always lose
                                    board[move_row][move_column] = red_piece
                                else:
                                    blue_number = int(
                                        location.replace("B", ''))
                                    red_number = int(
                                        red_piece.replace("R", ''))
                                    if (red_number >= blue_number):  # logic for basic number pieces
                                        board[move_row][move_column] = red_piece
                                    if (blue_number > red_number):
                                        board[move_row][move_column] = location
                        else:
                            # logic for if selected location is empty
                            board[move_row][move_column] = red_piece

            board[piece_row][piece_column] = "  "
            draw_board(board)

            if is_game_over(board):  # if a game over condition is met exit the loop and end game
                return False

        # all the code in this part is the same as the conditions for the red player except for Blue player
        elif (players_turn == "Blue"):
            print("Blue player's turn")
            piece_row = int(
                input("Select piece to move by position (Enter row): "))
            piece_column = int(
                input("Select piece to move by position (Enter column): "))

            while not (0 <= piece_row < length and 0 <= piece_column < width and
                       board[piece_row][piece_column][0] == "B" and
                       not board[piece_row][piece_column] == "BF" and
                       not board[piece_row][piece_column] == '  ' and
                       not board[piece_row][piece_column] == "BM"):
                print(
                    "Invalid move. The selected piece does not belong to your team. Try again.")
                piece_row = int(
                    input("Select piece to move by position (Enter row): "))
                piece_column = int(
                    input("Select piece to move by position (Enter column): "))

            move_row = int(
                input("Enter a row coordinate to move the piece to: "))
            move_column = int(
                input("Enter a column coordinate to move the piece to: "))

            while not (abs(piece_row - move_row) <= 1 and abs(piece_column - move_column) <= 1 and board[move_row][move_column][0] != "B"):
                print("Invalid move. You can only move one square at a time and you cannot move to a square that has your piece on it.")
                move_row = int(
                    input("Enter a row coordinate to move the piece to: "))
                move_column = int(
                    input("Enter a column coordinate to move the piece to: "))

            blue_piece = board[piece_row][piece_column]
            location = board[move_row][move_column]

            if (blue_piece == "BS"):
                if (location == "  "):
                    board[move_row][move_column] = blue_piece
                elif (location == "RS" or location == "RA" or location == "RF" or location == "RM"):
                    board[move_row][move_column] = blue_piece
                elif (location != "RS" or location != "RA" or location != "RF" or location != "RM"):
                    board[move_row][move_column] = location
            else:
                if (blue_piece == "BA" and location != "RM"):
                    board[move_row][move_column] = blue_piece
                else:
                    if (location == "RF" or location == "RA"):
                        board[move_row][move_column] = blue_piece
                    else:
                        if (location[0] == "R"):
                            if (location == "RM"):
                                board[move_row][move_column] = "  "
                            else:
                                if (location == "RS"):
                                    board[move_row][move_column] = blue_piece
                                else:
                                    red_number = int(location.replace("R", ''))
                                    blue_number = int(
                                        blue_piece.replace("B", ''))
                                    if (red_number <= blue_number):
                                        board[move_row][move_column] = blue_piece
                                    if (blue_number < red_number):
                                        board[move_row][move_column] = location
                        else:
                            board[move_row][move_column] = blue_piece
            board[piece_row][piece_column] = "  "
            draw_board(board)

            if is_game_over(board):
                return False

        players_turn = player_2 if players_turn == player_1 else player_1


if __name__ == '__main__':
    random.seed(input('What is seed? '))
    file_name = input('What is the filename for the pieces? ')
    length = int(input('What is the length? '))
    width = int(input('What is the width? '))
    tactego(file_name, length, width)
