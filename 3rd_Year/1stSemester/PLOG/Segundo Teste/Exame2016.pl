:- use_module(library(clpfd)).
:- use_module(library(lists)).
% Exame2016

% Pergunta 1


/*
Este programa recebe 2 lista como argumentos, e verifica se ambas contém os mesmos valores, através do predicado gen.


De seguida, verifica se a segunda lista recebida possui todos os seus valores organizados ou por ordem crescente, ou decrescente.

A nível de eficiência, podemos dizer que o programa não é muito eficiente dado que não usa a library(clpfd),
ou seja, não usa programação de restrições por propragação. A utilização de retrocesso é menos eficiente.

Para além disso, o predicado test utiliza o mecanismo


*/

% Pergunta 1

p1(L1,L2) :-
    gen(L1,L2),
    test(L2).


gen([],[]).
gen(L1,[X|L2]) :-
    select(X,L1,L3),
    gen(L3,L2).


test([_,_]).
test([X1,X2,X3|Xs]) :-
    (X1 < X2, X2 < X3; X1 > X2, X2 > X3),
    test([X2,X3|Xs]).


% Pergunta 3


p2(L1,L2) :-
    length(L1,N),
    length(L2,N),
    %
    pos(L1,L2,Is),
    all_distinct(Is),
    test2(L2),
    %
    labeling([],Is).
    


pos([],_,[]).
pos([X|Xs],L2,[I|Is]) :-
    element(I,L2,X),
    pos(Xs,L2,Is).


test2([_,_],2).
test2([X1,X2,X3|Xs],Length) :-
    ((X1 #< X2 #/\ X2 #< X3) #\/ (X1 #> X2 #/\ X2 #> X3)) #<=> B,
    Length #=  B + Length2,
    test2([X2,X3|Xs],Length2).


% Exercício 4

% Existem N ovos, os restantes recursos são ilimitados

% Receitas -> tempo de preparação, numero de ovos

% Tempo limitado para cozinhar 3 pratos
% gastando o maior número possível de ovos

% sweet_recipes(60,30,[20,50,10,20,15],[6,4,12,20,6],Cookings,Eggs).

sweet_recipes(MaxTime,NEggs,RecipeTimes,RecipeEggs,Cookings,Eggs):-

    % Obter o número de cozinhados, e verificar que as listas têm o mesmo tamanho
    length(RecipeTimes,Length),
    length(RecipeEggs,Length),

    % Declarar os 3 cozinhados que são necessários
    length(Cookings,3),

    % Apenas é possível ter o index do numero de recipes existentes
    domain(Cookings,1,Length),
    domain([Eggs],0,NEggs),

    % Não se pode fazer o mesmo cozinhado 2 vezes
    all_distinct(Cookings),


    % Ir buscar todos os ovos e tempos de 3 dos cozinhados
    get_all(Cookings,RecipeTimes,RecipeEggs,Eggs,TotalTime),

    Eggs #=< NEggs,
    TotalTime #=< MaxTime,


    labeling([maximize(Eggs)],[Eggs,TotalTime|Cookings]).


get_all([],_,_,0,0).
get_all([H|T],RecipeTimes,RecipeEggs,TotalEggs,TotalTime):-
    element(H,RecipeTimes,NTime),
    element(H,RecipeEggs,NEggs),
    TotalEggs #= NextEggs + NEggs,
    TotalTime #= NextTime + NTime,
    get_all(T,RecipeTimes,RecipeEggs,NextEggs,NextTime).



receitas(NOvos, TempoMax, OvosPorReceita, TempoPorReceita, OvosUsados, Receitas):- 
    
    
    length(OvosPorReceita, NumReceitas), 
    length(Receitas, 4), 
    domain(Receitas, 1, NumReceitas), 
    domain([OvosUsados], 0, NOvos), 
    all_distinct(Receitas), 
    
    get_total_ovos(Receitas, OvosPorReceita, OvosUsados), 
    OvosUsados #=< NOvos, 
    
    get_tempo_receita(Receitas, TempoPorReceita, TotalTempo), 
    TotalTempo #=< TempoMax,
    
    append([[OvosUsados], Receitas], Vars), 
    labeling([maximize(OvosUsados)], Vars). 
    
get_total_ovos([], _, 0).
get_total_ovos([X|Receita], OvosPorReceita, TotalOvos):-
    element(X, OvosPorReceita, NumOvos), 
    TotalOvos #= NumOvos + OtherNumOvos, 
    get_total_ovos(Receita, OvosPorReceita, OtherNumOvos).
    
get_tempo_receita([], _, 0).
get_tempo_receita([X|Receita], TempoPorReceita, TotalReceita):-
    element(X, TempoPorReceita, Tempo), 
    TotalReceita #= Tempo + OtherTempo, 
    get_tempo_receita(Receita, TempoPorReceita, OtherTempo).




sweet_recipes2(MaxTime, NEggs, RecipeTimes, RecipeEggs, Cookings, Eggs) :-
    length(RecipeEggs, N),
    Cookings = [C1, C2, C3],
    domain(Cookings, 1, N),
    domain([Eggs], 0, NEggs),
    all_distinct(Cookings),

    find_recipes(Cookings, RecipeTimes, RecipeEggs, Time, Eggs),
    Eggs #=< NEggs,
    Time #=< MaxTime, 

    labeling([maximize(Eggs)], [Eggs, Time | Cookings]).

find_recipes([], _, _,  0, 0).
find_recipes([IndexRecipe | Cookings], RecipeTimes, RecipeEggs, Time, Eggs) :-
    element(IndexRecipe, RecipeTimes, NewTime),
    element(IndexRecipe, RecipeEggs, NewEggs),
    Time #= NewTime + Time1,
    Eggs #= NewEggs + Eggs1,
    find_recipes(Cookings, RecipeTimes, RecipeEggs, Time1, Eggs1).


% cut([12,50,14,8,10,90,24], [100,45,70], S).
cut(Shelves,Boards,SelectedBoards):-

    % Arranjar o tamanho das boards, para saber o domain dasselected boards
    length(Boards,Length),
    length(Shelves,LengthShelves),
    length(SelectedBoards,LengthShelves),
    domain(SelectedBoards,1,Length),

    % generate tasks and machines for cumulatives,
    create_tasks(Shelves,SelectedBoards,Tasks),
    create_machines(Boards,Machines,1),
    
    cumulatives(Tasks,Machines,[bound(upper)]),

    labeling([],SelectedBoards).

create_tasks([],_,[]).
create_tasks([Shelf|T1],[BoardIndex|T2],[task(0,1,1,Shelf,BoardIndex)|T3]):-
    create_tasks(T1,T2,T3).

create_machines([],[],_).
create_machines([Board|T],[machine(Index,Board)|T2],Index):-
    Index2 #= Index + 1,
    create_machines(T,T2,Index2).


% cut2([12,50,14,8,10,90,24], [100,45,70], S).
cut2(Shelves,Boards,SelectedBoards):-

    % Arranjar o tamanho das boards, para saber o domain dasselected boards
    length(Boards,Length),
    length(Shelves,LengthShelves),
    length(SelectedBoards,LengthShelves),
    domain(SelectedBoards,1,Length),

    % generate tasks for cumulatives,
    create_items(Shelves,SelectedBoards,Items),
    create_bins(Boards,Bins,1),
    bin_packing(Items,Bins),

    labeling([],SelectedBoards).

create_items([],_,[]).
create_items([Shelf|T1],[BoardIndex|T2],[item(Shelf,BoardIndex)|T3]):-
    create_items(T1,T2,T3).

create_bins([],[],_).
create_bins([Board|T],[bin(Index,Board)|T2],Index):-
    Index2 #= Index + 1,
    create_bins(T,T2,Index2).














    