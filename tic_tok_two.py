
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def display_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


def player_move(board, player):
    while True:
       
        position = int(input(f"Player {player},  position (1-9): ")) -1 
        if board[position] == ' ':  
            board[position] = player
            break  
        else:
            print("That spot is taken.")


def check_winner(board, player):
    
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == player and board[combo[1]] == player and board[combo[2]] == player:
            return True
    return False


def check_draw(board):
    return ' ' not in board  


def play_game():
    
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  
    current_player = 'X' 

    
    while True:
        display_board(board)  
        player_move(board, current_player)  

        
        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break


        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break

    
        current_player = 'O' if current_player == 'X' else 'X'


play_game()
