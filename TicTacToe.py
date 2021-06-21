# / /  0
#----- 1
# / /  2
#----- 3
# / /  4
# 01234

import random as r

def drawField(matrice):
    contor = 0
    for i in range(5):
        if i % 2 == 0:
            print(matrice[contor][0] + "|" + matrice[contor]
                  [1] + "|" + matrice[contor][2])
            contor += 1
        else:
            print("-----")


def checkWinner(player, matrice):
    if (matrice[0][0] == matrice[1][1] and matrice[1][1] == matrice[2][2] and matrice[0][0] != " "):  # diagonala principala
        print("A castigat jucatorul " + str(player))
        return 0
    else:
        if(matrice[0][0] == matrice[0][1] and matrice[0][1] == matrice[0][2] and matrice[0][0] != " "):  # prima linie
            print("A castigat jucatorul " + str(player))
            return 0
        else:
            if(matrice[0][0] == matrice[1][0] and matrice[1][0] == matrice[2][0] and matrice[0][0] != " "):  # prima coloana
                print("A castigat jucatorul " + str(player))
                return 0
            else:
                # coloana secundara
                if(matrice[0][2] == matrice[1][1] and matrice[1][1] == matrice[2][0] and matrice[0][2] != " "):
                    print("A castigat jucatorul " + str(player))
                    return 0
                else:
                    # ultima linie
                    if(matrice[2][0] == matrice[2][1] and matrice[2][1] == matrice[2][2] and matrice[2][0] != " "):
                        print("A castigat jucatorul " + str(player))
                        return 0
                    else:
                        # ultima coloana
                        if(matrice[0][2] == matrice[1][2] and matrice[1][2] == matrice[2][2] and matrice[0][2] != " "):
                            print("A castigat jucatorul " + str(player))
                            return 0
                        else:
                            # daca se returneaza 1 atunci mai sunt locuri libere de cautat
                            ok = 0
                            for r in range(3):
                                for c in range(3):
                                    if matrice[r][c] == " ":
                                        ok = 1
                            if ok == 1:
                                return 1
                            # daca se returneaza 2 inseamna ca totul este ocupat si nu este niciun castigator
                            return 2


player = r.randint(1,2)
matrice = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
drawField(matrice)

while(True):

    print("Este randul jucatorului ", player)
    linie = int(input("Linia unde vrei sa pui: "))
    coloana = int(input("Coloana unde vrei sa pui: "))

    if player == 1:
        if(matrice[linie][coloana] == " "):
            matrice[linie][coloana] = "X"
            drawField(matrice)
            if checkWinner(player, matrice) == 0:
                break
            else:
                if checkWinner(player, matrice) == 2:
                    print("Nu este niciun castigator")
                    break
            player = 2
        else:
            print("Este deja ceva pe pozitia ", linie, coloana)
    else:
        if(matrice[linie][coloana] == " "):
            matrice[linie][coloana] = "O"
            drawField(matrice)
            if checkWinner(player, matrice) == 0:
                break
            else:
                if checkWinner(player, matrice) == 2:
                    print("Nu este niciun castigator")
                    break
            player = 1
        else:
            print("Este deja ceva pe pozitia ", linie, coloana)
