#connect 4 game

import numpy as np

# creat a board
board1 = np.zeros((7, 7), dtype=str)
import string

board1[0] = list(string.ascii_uppercase)[0:7]
board1 = np.where(board1 == '', ' ', board1)
# ask player1 about input
player1choice = input('please enter (x , o):').lower()
if player1choice == 'x':
    player2choice = 'o'
else:
    player2choice = 'x'
# put yuor mark in the last column
column_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}


def player1turn():
    columnname = input("frist player, please choose a column from A to G : ").upper()
    columnindx = column_dict[columnname]
    totalcells = board1[1:, columnindx]  # take the second of row and columnindx
    empty = (totalcells == ' ').sum()
    if empty == 6:
        totalcells[-1] = player1choice
    else:
        totalcells[empty - 7] = player1choice
    print(board1)


def player2turn():
    columnname = input("second player, please choose a column from A to G: ").upper()
    columnindx = column_dict[columnname]
    totalcells = board1[1:, columnindx]  # take the second of row and columnindx
    empty = (totalcells == ' ').sum()
    if empty == 6:
        totalcells[-1] = player2choice
    else:
        totalcells[empty - 7] = player2choice
    print(board1)


for i in range(21):
    player1turn()
    player2turn()
print("game over")


# calculation score

def score(columnname):
    xscore = 0
    oscore = 0
    for cell in columnname:
        if cell == "x":
            xscore += 1
    else:
        if xscore % 4 != 0:
            xscore = xscore - (xscore % 4)

    for cell in columnname:
        if cell == "o":
            oscore += 1
    else:
        if xscore % 4 != 0:
            oscore = oscore - (oscore % 4)

    if player1choice == 'X':
        player1score = xscore // 4
        player2score = oscore // 4
    else:
        player2score = xscore // 4
        player1score = oscore // 4
    return player1score, player2score


player1score_finally = 0
player2score_finally = 0
for i in range(6):
    columnname = board1[i + 1]
    player1, player2 = score(columnname)
    player1score_finally += player1
    player2score_finally += player2

    if i < 4:  # add diagonal
        columnname = board1[1:].diagonal(i)
        player1, player2 = score(columnname)
        player1score_finally += player1
        player2score_finally += player2

        flipped_board = np.flip(board1[1:], axis=0)
        columnname = flipped_board[1:].diagonal(i)
        player1, player2 = score(columnname)
        player1score_finally += player1
        player2score_finally += player2
    else:
        columnname = board1[1:].diagonal(i - 6)
        player1, player2 = score(columnname)
        player1score_finally += player1
        player2score_finally += player2

        flipped_board = np.flip(board1[1:], axis=0)
        columnname = flipped_board[1:].diagonal(i - 6)
        player1, player2 = score(columnname)
        player1score_finally += player1
        player2score_finally += player2
for i in range(7):
    columnname = board1[1:, i]
    player1, player2 = score(columnname)
    player1score_finally += player1
    player2score_finally += player2

if player1score_finally > player2score_finally:
    print("the winner is player1 which is choose", player1choice)
else:
    if player2score_finally > player1score_finally:
        print("the winner is player2 which is choose", player2choice)
    else:
        print("game is over")


