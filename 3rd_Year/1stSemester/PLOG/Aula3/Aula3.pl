/*Exercício 2 */

/*  ALinea a*/

membro(X,[X|L]).
membro(X,[Y|L]) :- 
    X \= Y,
    member(X,L).

/* Alinea b */

b) membro(X,L):- append(_,[X|_],L). 

/* Alinea c */

nth_membro(1,[M|_],M).
nth_membro(N,[_|T],M):-
    N>1,
    N1 is N-1,
    nth_membro(N1,T,M). 
    
