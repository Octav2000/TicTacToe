# TicTacToe
Tic Tac Toe in Python

Pozitiile pentru X si 0 sunt retinute intr-o matrice de 3x3

1) Metoda drawField()
Se parcurge cu for de la 0 la 5 pentru a se putea desena "tabla". De asemenea, am mai luat un contor pentru liniile matricii care se incrementeaza atunci cand i-ul este par.
Cand i este par atunci se afiseaza elementele matricii de pe linia contor si coloanele 0, 1 si 2. 
Cand i este impar atunci se afiseaza doar mai multe - pentru a delimita liniile

2) Metoda checkWinner(player, matrice)
In aceasta metoda se returneaza 0 daca un jucator a reusit sa castige, 1 daca mai sunt locuri libere unde se poate adauga sau 2 daca totul este ocupat si niciun jucator nu a reusit sa castige
Acele if-uri verifica pentru toate liniile, coloanele si diagonalele matricii daca exista de 3 ori acelasi semn (daca sunt 3 de X sau 3 de 0) caz in care se returneaza 0 pentru castigator

De la linia 59 pana la 61 se initializeaza jucatorul generand aleator intre 1 si 2 si dupa se deseneaza tabla

In bucla infinita (linia 66):
- se citesc de la tastatura linia si coloana unde se doreste introducere urmatorului semn (X pentru jucatorul 1, 0 pentru jucatorul 2)
- Se verifica pentru fiecare jucator in parte daca la pozitia introdusa este loc liber (" "), iar in caz afirmativ se introduce semnul. Daca nu se afiseaza un mesaj ca este deja ceva introdus si se reia citirea
- Se deseneaza noua tabla (drawField()) si dupa se apeleaza metoda checkWinner() care daca returneaza 0 atunci avem un castigator si se da break din bucla infinita. Daca checkWinner() returneaza 2 atunci iar se da break pentru ca toata tabla a fost completata, dar nu e niciun castigator. Daca se returneaza 1 atunci se mai pot face introduceri si se schimba player-ul
