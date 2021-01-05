:-use_module(library(clpfd)).
:-use_module(library(lists)).


% Exercício 1, problema do quadrado mágico

% 1.a

magic3x3(Vars):-
    Vars = [A1,A2,A3,B1,B2,B3,C1,C2,C3],

    domain(Vars,1,9),

    all_distinct(Vars),


    Sum is (Length + 1)*Length//2, 

    % Horizontal
    A1 + A2 + A3 #= Soma,
    B1 + B2 + B3 #= Soma,
    C1 + C2 + C3 #= Soma,

    % Vertical
    A1 + B1 + C1 #= Soma,
    A2 + B2 + C2 #= Soma,
    A3 + B3 + C3 #= Soma,

    % Diagonal 
    A1 + B2 + C3 #= Soma,
    C1 + B2 + A3 #= Soma,

    % Eliminar Simestrias
    A1 #< A2, A1 #< A3,
    A1 #< B1, A1 #< B3,  

    labeling([],Vars).


magic(Length,Table):-

    % Matriz sobre forma de Lista de Listas para aceder às listas
    generateListofLists(Length,ListOfLists),

    % Matriz Transposta sobre forma de Lista de Listas para aceder a colunas
    transpose(ListOfLists,Transpose),

    % Flatten à lista para restringir o dominio
    append(ListOfLists,Table),

    % Restrição dos valores permitidos
    Domain is Length * Length,
    domain(Table,1,Domain),

    % Valores da tabela todos distintos
    all_distinct(Table),

    % Linhas todas iguais
    sum_restriction(ListOfLists,Sum),

    % Colunas todas iguais
    sum_restriction(Transpose,Sum),

    % Diagonais iguais
    diag_restriction(ListOfLists,Transpose,Sum),


    labeling([],Table).


% generateListofLists(+Length,-ListOfLists)
% gera uma Lista de Listas de dimensão Length.
generateListofLists(Length,ListOfLists):-
    length(ListOfLists,Length),
    generator(ListOfLists,Length).

% generator(-Row,+Length)
% gera uma linha de tamanho Length da lista de listas
generator([],_).
generator([H|T],Length):-
    length(H,Length),
    generator(T,Length).



sum_restriction([],_).
sum_restriction([H|T],Value):-
    sum_list(H,Value),
    sum_restriction(T,Value).


sum_list(List,Total):-
    sum_list(List,0,Total).

sum_list([],Total,Total).

sum_list([H|T],Current,Total):-
    Current2 #= Current + H,
    sum_list(T,Current2,Total).


diag_restriction(L1,L2,SumTotal):-
    diagonal_restriction(L1,L2,0,SumTotal,1).

diagonal_restriction([],[],Total,Total,_).
diagonal_restriction([H1|T1],[H2|T2],Current,Total,Index):-

    element(Index,H1,V1),
    element(Index,H2,V2),
    V1 #= V2, 
    Current2 #= Current + V1,
    Index2 #= Index+1,

    diagonal_restriction(T1,T2,Current2,Total,Index2).



nqueens(Cols):-
    Cols=[A1,A2,A3,A4],
    domain(Cols,1,4),
    all_distinct(Cols), % A1#\=A2, A1#\A3, A1#\A4, A2#\A3, A2#\A4, A3#\A4,
    A1#\=A2+1, A1#\=A2-1, A1#\=A3+2, A1#\=A3-2, A1#\=A4+3, A1#\=A4-3,
    A2#\=A3+1, A2#\=A3-1, A2#\=A4+2, A2#\=A4-2,
    A3#\=A4+1, A3#\=A4-1,
    labeling([],Cols).


%  puzzle(1,[D,O,N,A,L,D],[G,E,R,A,L,D],[R,O,B,E,R,T]).
puzzle(2,Vars):-
    Vars = [D,O,N,A,L,G,E,R,B,T],

    domain(Vars,0,9),
    all_distinct(Vars),

    D #\= 0,
    G #\= 0,

    D*100000 + O*10000 + N*1000 + A*100 + L*10 + D + 
    G*100000 + E*10000 + R*1000 + A*100 + L*10 + D #=
    (R*100000 + O*10000 + B*1000 + E*100 + R*10 + T),


    labeling([],Vars).

fort(Rooms):-

    Rooms = [R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12],
    domain(Rooms,0,12),
    sum(Rooms,#=,12),

    R1 + R12 + R11 + R10 #= 5,
    R1 + R2 + R3 + R4 #= 5,
    R4 + R5 + R6 + R7 #= 5,
    R7 + R8 + R9 + R10 #= 5,

    labeling([],Rooms).



% 72 perus -> _67_ escudos
% 
peru(Cost,Single):-

    Cost = [D3,6,7,D0],

    domain(Cost,0,9),

    D3 #\= 0,

    D3 * 1000 + 600 + 70 + D0 #= Total,

    Total mod 72 #= 0,
    Single #= Total / 72, 

    labeling([],Cost).















