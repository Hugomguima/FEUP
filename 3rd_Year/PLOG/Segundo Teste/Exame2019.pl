:- use_module(library(clpfd)).
:- use_module(library(lists)).

% Exercício 1
/*
a. 2^(NK)

base é 2 porque é o número de opçoes de cada lista, sendo 0 ou 1
Levantado a NK porque é o prodtudo cartesiano entre as 2 listas.

% Exercício 2

a. K^N

Lista de presentes: [P1,P2,P3,PN], N o numero de presentes e K a pessoa

Ou seja, cada valor pode ser uma pessoa, e o tamanho do array é o nuermo de presentes
*/


% Exercício 3

% O programa permite obter soluções em que a paridade do index dos presentes e das pessoas é diferente.

% Exercício 4

% O mod bloqueia a pesquisa e unifica, ignorando o dominio atribuido

% Exercóicio 5

constroi_bins(_,[],[]).
constroi_bins(Index,[H1|T1],[H2|T2]):-
    (I #= H) #<=> H2,
    constroi_bins(Index,T1,T2).


prat(+Prateleiras,+Objetos,-Vars):-

    % ir buscar o tamanho da lista de objetos
    length(Objetos,NObjetos),
    % Criar uma lista de Indices com o tamamho dos objetos
    length(Prateleiras,NLinhas),
    element(1,Prateleiras,Pcols),
    length(Pcols,NColunas),

    Size is NLinhas * NColunas,
    % Restringir os valores da lista de incdices para ter o tamanho da lista de objetos
    length(Vars,NObjetos),
    % Restringir os valores da lista de indices para ter os valors possíveis do tamanho da lista de listas Rows*Cols
    domain(Vars,1,Size),
    % Nâo pode haver índices repetidos na Lista Final.
    all_distinct(Vars),

    labeling([],Vars).



furniture(+Duracoes,+Homens,+MaxMen,+MaxTime,-StartTimes,-EndTimes,-FinalTime):-

    length(Duracoes,NObjetos),
    length(Homens,NObjetos),
    length(StartTimes,NObjetos),
    length(EndTimes,NObjetos),

    domain(StartTimes,0,MaxTime),
    domain(EndTimes,0,MaxTime),

    get_tasks(StartTimes,EndTimes,Homens,Duracoes,1,Tasks),

    maximum(FinalTime,EndTimes),
    cumulative(Tasks,[limit(MaxMen)]),
    labeling([minimize(FinalTime)],EndTimes).

get_tasks([],[],[],[],_,[]).
get_tasks([StartTime|T1],[EndTime|T2],[Homem|T3],[Duracao|T4],Index,[task(StartTime,Duracao,EndTime,Homem,Index)|T5]):-
    Index2 #= Index + 1,
    get_tasks(T1,T2,T3,T4,Index2,T5).


tt(FinalTime,Start,End):-
    Duracoes = [30,10,15,15],
    Homens =   [3,1,3,2],
    furniture(Duracoes,Homens,4,120,Start,End,FinalTime).






homens(4).
tempo_max(60).

create_tasks2(_, [], [], [], []).
create_tasks2(Index, [Homens-Tempo | Next], [task(S, Tempo, E, Homens, Index) | Tasks], [S | SList], [E | Elist]) :-
    NextIndex #= Index + 1,
    create_tasks2(NextIndex, Next, Tasks, SList, EList).

furniture2 :- 
    findall(X-Y, objeto(Objeto, X, Y), Objetos),

    
    length(Ss, 4),
    length(Es, 4),

    domain(Ss,0,60),
    domain(Es,0,60),
    
    create_tasks2(1, Objetos, Tasks, Ss, Es),

   

    maximum(End, Es),   
    cumulative(Tasks, [limit(4)]),
    labeling([minimize(End)],Es),
    write(Objetos), nl,
    write(End), nl,
    write(Ss), nl,
    write(Es).

objeto(piano, 3, 30).
objeto(cadeira, 1, 10).
objeto(cama, 3, 15).
objeto(mesa, 2, 15).
homens(4).
tempo_max(60).

furniture3(StartTimes,EndTimes,FinalTime):-

    findall(Duracao,objeto(X,Homem,Duracao),Duracoes),
    findall(Homem,objeto(X,Homem,Duracao),Homens),
    tempo_max(MaxTime),
    homens(MaxMen),

    length(Duracoes,NObjetos),
    length(Homens,NObjetos),
    length(StartTimes,NObjetos),
    length(EndTimes,NObjetos),

    domain(StartTimes,0,MaxTime),
    domain(EndTimes,0,MaxTime), 

    get_tasks(StartTimes,EndTimes,Homens,Duracoes,1,Tasks),
    maximum(FinalTime,EndTimes),

    cumulative(Tasks,[limit(MaxMen)]),
    labeling([minimize(FinalTime)],EndTimes).


ff(FinalTime,Start,End):-
    furniture3(Start,End,FinalTime).

test:-
    _List = [[1,5], [6,5], [4,3], [7,9], [4,5], [7,8], [3,3]],
    length(_List, _Len), length(Sorted, _Len), maplist(ln2, Sorted),
    length(P, _Len), keysorting(_List, Sorted, [permutation(P)] ).

ln2(X):-
    length(X,2).



place(Starts) :-
    Starts = [A, B, C],
    domain(Starts, 1, 11),
    Lines = [
        line(A, 4, r),
        line(B, 2, r),
        line(C, 3, r)
    ],
    A #< B,
    disjoint1(Lines, [margin(r, r, 2)]),
    labeling([], Starts).

