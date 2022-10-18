# player move on the position of the board
def move(player, curr_board, position):
    if position not in curr_board.keys():
        print("Illegal move. Make a different move!")
        return False
    if curr_board[position] == '_':
        curr_board[position] = player.flag
        return True
    else:
        print("That square is already occupied. Make a different move!")
        return False


# Player object
class Player:

    def __init__(self, s, num):
        self.flag = s
        self.num = num


# Convert dictionary to list then call print_grid to print
def printBoard(curr_board):
    L = [[], [], []]
    i = 0
    for e in curr_board.values():
        L[i // 3].append(e)
        i += 1
    print_grid(L)


# check whether the game is over
def check(curr_board):
    l1 = ['a', 'b', 'c']
    l2 = ['1', '2', '3']
    # column check
    for i in l1:
        if curr_board[i + '1'] == curr_board[i + '2'] and curr_board[i + '1'] == curr_board[i + '3']:
            if curr_board[i + '1'] == 'X':
                print("Player 0 wins!")
                return True
            elif curr_board[i + '1'] == '0':
                print("Player 1 wins!")
                return True
            else:

                continue
    # row check
    for i in l2:
        if curr_board['a' + i] == curr_board['b' + i] and curr_board['a' + i] == curr_board['c' + i]:
            if curr_board['a' + i] == 'X':
                print("Player 0 wins!")
                return True
            elif curr_board['a' + i] == '0':
                print("Player 1 wins!")
                return True
            else:

                continue
    # dig check
    if (curr_board['a1'] == curr_board['b2'] and curr_board['a1'] == curr_board['c3']) or (
            curr_board['a3'] == curr_board['b2'] and curr_board['a3'] == curr_board['c1']):
        if curr_board['a1'] == 'X' and curr_board['b2'] == 'X':
            print("Player 0 wins!")
            return True
        elif curr_board['a1'] == '0' and curr_board['b2'] == '0':
            print("Player 1 wins!")
            return True
        else:

            return False
    else:
        return False


def print_grid(L):
    print('\n'.join(['\t'.join([str(c) for c in row]) for row in L]))


if __name__ == '__main__':
    # board is a dictionary to record the position
    board = {'a3': '_', 'b3': '_', 'c3': '_', 'a2': '_', 'b2': '_', 'c2': '_', 'a1': '_', 'b1': '_', 'c1': '_'}
    # player 0 use X to flag the position selected
    player0 = Player('X', 0)
    # player 1 use O to flag the position selected
    player1 = Player('O', 1)
    # indicate which player to move
    move_num = 0
    # if there have empty to select
    while "_" in board.values():
        print("what is your move, player", move_num, "?")
        pos = input()
        if pos == "EXIT":
            break
        if move_num == 0:
            if move(player0, board, pos):
                move_num = 1
                printBoard(board)
        else:
            if move(player1, board, pos):
                move_num = 0
                printBoard(board)
        if check(board):
            break
        else:
            if "_" in board.values():
                pass
            else:
                print("The game is a draw.")
