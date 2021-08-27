#Tic Tac Toe game for two players 
"""
Approach to take:
1. 2 players should be able to play the game(both sitting at the same computer)
2. The board should be printed out everytime a player makes a move
3. You should be able to accept input of the player position and then place a symbol on the board
"""

"""
We will use the NUMPAD to match numbers to the grid on a tic tac toe board:
    7   8   9   
    4   5   6
    1   2   3
"""

#Function to display the board
def display_board(board):
    print('\n'*100)
    print(' '+board[7]+' '+'|'+' '+board[8]+' '+'|'+' '+board[9])
    print("---|---|---")
    print(' '+board[4]+' '+'|'+' '+board[5]+' '+'|'+' '+board[6])
    print("---|---|---")
    print(' '+board[1]+' '+'|'+' '+board[2]+' '+'|'+' '+board[3])


#Function to take in player input and assign their marker as 'X' or 'O'
def player_input():
    ''' 
    Output = (player 1 marker, Player 2 marker)
    '''
    choice = 'WRONG'
    while choice not in ['X','O']:
        choice = input("Player 1, would you like to be X or O ?: ")

    if choice == 'X':
        return ('X','O')
    else:
        return ('O','X')


#function to take in the board, marker (X or O), desired position (1-9) and assign it to the board
def place_marker(board,marker,position):
    board[position] = marker
    return board


#Function to take in a board and a marker (X or O) and then check to see if that mark has won
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or #TOP ROW
            (board[4] == mark and board[5] == mark and board[6] == mark) or #MIDDLE ROW
            (board[1] == mark and board[2] == mark and board[3] == mark) or #BOTTOM ROW
            (board[7] == mark and board[4] == mark and board[1] == mark) or #LEFT COLUMN
            (board[8] == mark and board[5] == mark and board[2] == mark) or #MIDDLE COLUMN
            (board[9] == mark and board[6] == mark and board[3] == mark) or #RIGHT COLUMN
            (board[7] == mark and board[5] == mark and board[3] == mark) or #DIAGONAL1
            (board[1] == mark and board[5] == mark and board[9] == mark))   #DIAGONAL2


#Function that uses random module to randomly decide which player goes first.
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


#Function that returns a boolean indicating whether a space on the board is free
def space_check(board, position):
    return board[position] == ' '


#Function to check if the board is full
def full_board_check(board):
    count = 0
    for i in range(1,10):
        if board[i] == 'X' or board[i] == 'O':
            count = count + 1
        else: 
            pass
    if count == 9:
        return True
    else:
        return False


#Function to ask a player's next position (1-9) and then use space_check() to check if it's free. If free, return the position for later use
def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board, position):
        position = int(input("Enter the position (1-9): "))
    return position


#Function to ask the player if they want to play again and return boolean True if they do want to play again
def replay():
    choice = 'abc'
    while choice not in ('Y','N'):
        choice = input('Do you want to continue playing? (Y/N): ')
    if choice == 'Y':
        return True
    else:
        return False


#
#GAME LOGIC!!!!
#

print('Welcome to Tic Tac Toe!')

while True:
    
    #SETTING UP THE GAME:
    TheBoard = [' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    
    game = input("Are you ready? (Y/N)")
    if game == 'Y':
        game_on = True
    else:
        game_on = False
        game1 = input("DO you want to play this game?(Y/N): ")
        if game1 == 'Y':
            print("Let's Play!!!")
            game_on = True
        else:
            break
    #GAME PLAY
    while game_on:
        #player1 Turn:
        if turn == 'Player 1':
            display_board(TheBoard)
            position = player_choice(TheBoard)
            place_marker(TheBoard,player1_marker,position)

            if win_check(TheBoard,player1_marker):
                display_board(TheBoard)
                print("Congratulations! Player 1 won the game!!!")
                game_on = False
            elif full_board_check(TheBoard):
                display_board(TheBoard)
                print("The game is draw!")
                break
            else: 
                turn = 'Player 2'

        #player2 turn:
        else:
            display_board(TheBoard)
            position = player_choice(TheBoard)
            place_marker(TheBoard,player2_marker,position)

            if win_check(TheBoard,player2_marker):
                display_board(TheBoard)
                print("Congratulations! Player 2 won the game!!!")
                game_on = False
            elif  full_board_check(TheBoard):
                display_board(TheBoard)
                print("The game is draw!")
                break
            else:
                turn = 'Player 1'

    if replay() == False:
        break



    

