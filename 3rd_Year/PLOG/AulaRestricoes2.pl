:-use_module(library(clpfd)).
:-use_module(library(lists)).

% Problema dos 12 carros no slide 3 da jamboard do professor

car_colors(Cars):-

    % Existem 12 carros
    Cars = [C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12],

    % Cada carro tem uma das 4 cores---- 1->Amarelo 2->Verde 3->Vermelho 4->Azul
    domain(Cars,1,4),

    %Numero de carros de cada cor
    global_cardinality(Cars, [1-4,2-2,3-3,4-3]),
    
    %Primeiro e o ultimo têm a mesma cor
    C1 #= C12,
    %Segundo e o penultimo têm a mesma cor
    C2 #= C11,
    %O quinto é azul
    C5 #= 4,

    %Garantir as subsequencias seguidas
    sub_sequencies(Cars),

    %Garantir que a subsequencia apenas existe 1 vez
    distinct_sequence(Cars,1),

    labeling([],Cars),
    write(Cars).
    
    


sub_sequencies([]).
sub_sequencies([_]).
sub_sequencies([_,_]).
sub_sequencies([X,Y,Z|Tail]):-
    all_distinct([X,Y,Z]),
    sub_sequencies([Y,Z|Tail]).


distinct_sequence([_,_,_],0).
distinct_sequence([X,Y,Z,W|Tail],Counter):-
   (X#=1 #/\Y#=2 #/\Z#=3 #/\W#=4)#<=>B,
   Counter #= Counter1 + B,
   distinct_sequence([Y,Z,W|Tail],Counter1).


% Exercício 5 da ficha 2 -- Não está 100% bem
fila_de_carros:-

    length(Colors, 4),
    length(Size, 4),

    % Cada carro tem uma das 4 cores---- 1->Amarelo 2->Verde 3->Azul 4->Preta
    % Cada carro tem um tamanho diferente, por ordem.
    domain(Colors,1,4),
    domain(Size,1,4),

    % Os valores são todos distintos
    all_distinct(Colors),
    all_distinct(Size),

    % e o carro que está imediatamente antes do carro azul é menor do que o que está imediatamente depois do carro azul
    Index2 #= IndexBlue - 1,

    element(IndexBlue,Colors,3),
    element(IndexBlue,Size,SizeBlue),
    element(Index2,Size,PreviousCarSize),

    PreviousCarSize #< SizeBlue,

    % Verde é o menor de todos
    element(IndexGreen,Colors,2),
    element(IndexGreen,Size,1),

    % O carro verde está depois do carro azul
    IndexGreen #> IndexBlue,

    % e que o carro amarelo está depois do preto

    element(IndexYellow,Colors,1),
    element(IndexBlack,Colors,4),

    IndexYellow #> IndexBlack,

    labeling([],Colors),
    labeling([],Size),

    write(Colors),nl,   
    write(Size).




   

    








