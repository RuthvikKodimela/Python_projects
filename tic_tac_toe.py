import random

def display_board(board):
    print('\n'*100)
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def player_input():
    
    choice = 'wrong'
    
    #we want to take input from user about which marker to choose, need to fail and ask again
    # if they enter anything else apart from X or O
    # also send a message if they give a wrong answer
    # if player1 chooses X, then player2 becomes O and vice versa
    
    while choice != 'X' and choice != 'O':
        choice = input("enter a marker X or O: ")
        
        if choice != 'X' and choice != 'O':
            print('\n'*100)
            print("Sorry, only X or O to be choosen")

        if choice == 'X':
            player1_marker = 'X'
            player2_marker = 'O'
        elif choice == 'O':
            player1_marker = 'O'
            player2_marker = 'X'
        
    return player1_marker,player2_marker

def place_marker(board, marker, position):
    # this func should open the board and take a marker which is X or O
    # and then take a index position from user and assign the marker to the position
    
    board[position] = marker
    
    return board

def win_check(board, mark):
    
    # need a func that checks the board and marker(X or O ) to see if the marker has won
    
     return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


def choose_first():
    # this function should let us know which one should go first
    # if the random int prints 0, player 1 should go, else player 2
    if random.randint(0,1) == 0:
        return 'Player1'
    else:
        return 'Player2'
        
def space_check(board, position):
    # this func should checks whether the position on the board is free
    return board[position] == ' '

def full_board_check(board):
    # need to check each position or index is full in the board
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    
    # should ask player next index pos b/w 1,9
    # use space check if the position is free
    # if free then assign the marker to free pos
    
    position = 0
    
    while position not in range(1,10) or not space_check(board, position):
        position = int(input("your next move? : "))
    
        if position not in range(1,10):
            print('\n'*100)
            print("your move out of range, try again")
            
    return position

def replay():
    
    return input("Do you wanna have another go? yes or no? ").lower().startswith('y')

while True:
    
    theboard = [' '] * 10
#     display_board(theboard)

    player1_marker,player2_marker = player_input()

    turn = choose_first()
    print(turn + " will go first")

    play_game = input("Lets start, yes or no?")

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'Player 1':
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player1_marker, position)

            if win_check(theboard, player1_marker):
                display_board(theboard)
                print("congrats mate P1!")
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print("Game's a draw bud !")
                    break
                else:
                    turn = 'Player 2'
                    display_board(theboard)

        else:
            #player2 turn
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player2_marker, position)

            if win_check(theboard, player2_marker):
                display_board(theboard)
                print("congrats mate player2 !")
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print("Game's a draw bud !")
                    break
                else:
                    turn = 'Player 1'
            
    if not replay():
        break