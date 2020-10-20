# Function to display the board
def display_board(board):
    
    print(f'     |     |     ')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}  ')
    print(f'_____|_____|_____')
    print(f'     |     |     ')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}  ')
    print(f'_____|_____|_____')
    print(f'     |     |     ')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}  ')
    print(f'     |     |     ')

# Taking input from player
def player_input(player):
    check=True
    while(check):
        position=int(input(f'Choose your position between 1- 9 for {player} : '))
        if(position in range(1,10)):
            check=False
        else:
            print('Wrong input.')
    return position
# Mark the selected place by the makker selected by the player
def place_marker(board, marker, position):
    
    board[position]=marker
# Checking the board, if any one is win or not
def win_check(board, mark):
    check=False
    def w_check(p1,p2,p3):
        return board[p1]==board[p2]==board[p3]==mark
    if(w_check(1,2,3)):
        check=True
    elif(w_check(4,5,6)):
        check=True
    elif(w_check(7,8,9)):
        check=True
    elif(w_check(1,4,7)):
        check=True
    elif(w_check(2,5,8)):
        check=True
    elif(w_check(3,6,9)):
        check=True
    elif(w_check(1,5,9)):
        check=True
    elif(w_check(3,5,7)):
        check=True
    return check

def space_check(board, position):
    
    return board[position]==' '

def full_board_check(board):
    return ' ' not in board

def replay():
    check=input('Do you want play again yes/no : ')
    if check=='yes':
        return True
    else:
        return False
       
print('Welcome to Tic Tac Toe Game!')

while True:
    # Set the game up here
  
    player1 = input("Please pick a marker 'X' or 'O' for player 1 : ")
    player2 = ''
    if player1=='X':
        player2='O'
    else:
        player2='X'
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(board)
    while True:
        #Player 1 Turn
        
        print('Player 1 turn : ')
        position = player_input(player1)
        if(space_check(board,position)):
            place_marker(board,player1,position)
            display_board(board)
        else:
            print('Position is accupied make another choise : ')
            continue
        if(win_check(board,player1)):
            print('Player 1 win.')
            break
            
        # Player2's turn.
        if(full_board_check(board)):
            board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            display_board(board)
              
        print('Player 2 turn : ')
        position = player_input(player2)
        if(space_check(board,position)):
            place_marker(board,player2,position)
            display_board(board)
        else:
            print('Position is not accupied make another choise : ')
            continue
        if(win_check(board,player2)):
            print('Player 1 win.')
            break   

    if not replay():
        break   

