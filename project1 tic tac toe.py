#Tic Tac Toe using python
   #user have to see the pattern
   #have to be 2 player game
   #patterns have to change each game
   #show result after one game end
   #show play again after a code ends

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_winner(board,player):
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]==player:
            return True
    for i in range(3):
        if board[0][i]==board[1][i]==board[0][2]==player:
            return True
    if board[0][0]==board[1][1]==board[2][2]==player or board[0][2]==board[1][1]==board[2][0]==player:
        return True
    return False
def board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True
def play_again():
    choice=input("Do you want to play again? (yes/no): ")
    return choice=='yes'
def main():
    while True:
        board=[[" " for _ in range(3)] for _ in range(3)]
        current_player='X'
        while True:
            print_board(board)
            row=int(input(f"player {current_player} ,enter row(0-2): "))
            col=int(input(f"player {current_player} ,enter column (0-2): " ))
            if board[row][col]==" ":
                board[row][col]=current_player
                if check_winner(board,current_player):
                    print_board(board)
                    print(f"player {current_player} wins!")
                    break
                elif board_full(board):
                    print_board(board)
                    print("Draw!")
                    break
                else:
                    current_player='0' if current_player=='X' else 'X'
            else:
                print("It is already taken.Try again.")
        if not play_again():
            print("Thanks for playing!")
            break
main()


        
        