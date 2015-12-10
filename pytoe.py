__author__ = 'hectormgerardo'
# imprime el gato
def schauspiel(spiel):
    #reversed para que la matriz se muestre en
    # la misma posición que'l teclado númérico
    for i in reversed(range(3)):
        print()
        for j in range(3):
            if spiel[i*3+j]==1:
                print('X ',end=' ')
            elif spiel[i*3+j]==0:
                print('O ',end=' ')
            elif spiel[i*3+j]==-1:
                print('- '
                    #spiel[i*3+j]-1
                     ,end=' ')
        #if i==2 or i==5 or i==8:
    print('\n')
# recibe la cruz o círculo por input()
def get_input(turn):
    valid = False
    while not valid:
        try:
            user = input("¿Dónde colocar " + turn + " (1-9)? ")
            user = int(user)
            if user >= 1 and user <= 9:
                return user-1
            else:
                print("Nope, ahí no. Sigue participando.\n")
        except Exception as e:
            print(user + " no se puede ahí, intenta otra vez.\n")
#era check, pero scheck suena más alemán
def scheck(spiel):
    win_cond = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
    for each in win_cond:
        try:
            if spiel[each[0]-1] == spiel[each[1]-1] and spiel[each[1]-1] == spiel[each[2]-1]:
                return spiel[each[0]-1]
        except:
            pass
    return -1
def aus_spiel(spiel,msg):
    schauspiel(spiel)
    print(msg)
    quit()
def main():
    #arreglo dónde estarán las X y O
    spiel = []
    #-1 para vacío, 1 para X y 0 para O
    for i in range(9):
        spiel.append(-1)

    win = False
    q = 0
    while not win:
        schauspiel(spiel)
        print("Turn number " + str(q+1))
        if q % 2 == 0:
            turn = 'X'
        else:
            turn = 'O'
        user = get_input(turn)
        while spiel[user] != -1:
            print("Nope, ahí no, intenta otra vez.\n")
            user = get_input(turn)
        spiel[user] = 1 if turn == 'X' else 0
        q += 1
        if q > 4:
            ganador = scheck(spiel)
            if ganador != -1:
                out = "Ganó: "
                out += "X" if ganador == 1 else "O"
                out += " c:"
                aus_spiel(spiel,out)
            elif q == 9:
                aus_spiel(spiel,msg="DRAW GAEM")
if __name__ == "__main__": main()
