import netz0
from requests import get
ipy=''
ipz=''
def main():
    ipa=input('Provea la dirección ip del anfitrión (deje en blanco para ser el anfitrión): ')
    if ipa=='':
        ipy=get('https://api.ipify.org').text
        move = 0
    else:
        ipz=ipa
        move=1
    board = []
    for i in range(9):
        board.append(-1)
    win = False
    while not win:
        print_board(board)
        print("turno: " + str(move + 1))
        if move % 2 == 0:
            turn = 'X'
        else:
            turn = 'O'
        netz0.connect(ipy,ipz)
        user = get_input(turn)
        while board[user] != -1:
            print("Invalid move! Cell already taken. Please try again.\n")
            user = get_input(turn)
        board[user] = 1 if turn == 'X' else 0
        # advance move and check for end game
        move += 1
        if move > 4:
            winner = check_win(board)
            if winner != -1:
                out = "The winner is "
                out += "X" if winner == 1 else "O"
                out += " :)"
                quit_game(board, out)
            elif move == 9:
                quit_game(board, "No winner :(")
def get_input(turn):
    valid = False
    while not valid:
        if turn=='X':
            try:
                user = input("Where would you like to place X (1-9)? ")
                user = int(user)
                if user >= 1 and user <= 9:
                    print('test')
                    q=netz0.connect(z=ipz,y=ipy).lend(g=user)
                    return user - 1
                else:
                    print("No puede usar esa posición.")
            except Exception as e:
                print("No puede usar esa posición, está ocupada o el otro jugador no está conectado.")
        elif turn=='O':
            try:
                w=netz0.connect.wait4player()
                if w >= 1 and w <= 9:
                    return w-1
            except Exception as e:
                print("No responde el jugador...")


def print_board(board):
    print("The board look like this:")
    for i in reversed(range(9)):
        if board[i]==1:
            print('X ',end=''),
        elif board[i]==0:
            print('O ',end=''),
        elif board[i]==-1:
            print('- ',end=''),
        if i==3 or i==6 or i==9:
            print('')
    print('')

def check_win(board):
    win_cond = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
    for each in win_cond:
        try:
            if board[each[0]-1]==board[each[1]-1] and board[each[1]-1]==board[each[2]-1]:
                return board[each[0]-1]
        except:
            pass
    return -1
def quit_game(board, msg):
    print_board(board)
    print(msg)
    quit()

if __name__ == "__main__":
    main()