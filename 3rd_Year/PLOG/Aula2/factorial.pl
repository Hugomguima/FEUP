factorial(1,1).
/*
factorial(N,V) :-
    N > 1,
    N1 is N-1, factorial(N1,V1),
    V is V1*N.

*/
factorial(N,V) : fact(N,1,V).

fact(N,Acc,V) :-
    N > 1,
    N1 is N-1,
    Acc is Acc*N,
    factorial(N1,V1).
    