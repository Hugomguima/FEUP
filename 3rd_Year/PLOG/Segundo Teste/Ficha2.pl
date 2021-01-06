:-use_module(library(clpfd)).
:-use_module(library(lists)).

% Exercício Fila de carros - Exercício 5

% 4 carros
% Cores = [Amarelo,Azul,Verde,Preto]

% Carro Antes do azul menor do que o depois do azul
% Carro Verde Menor de todos
% Carro Verde depois do Azul
% Carro amarelo está depois do preto

% Amarelo - 1
% Azul - 2
% Verde - 3
% Preto - 4


carros(Colors,Size):-

    length(Colors,4),
    length(Size,4),

    domain(Colors,1,4),
    domain(Size,1,4),

    % 1 tamanho e 1 cor para cada carro
    all_distinct(Colors),
    all_distinct(Size),

    % Carro antes do azul menor do que o seguinte
    element(BlueIndex,Colors,2),
    BeforeBlueIndex #= BlueIndex - 1,
    AfterBlueIndex #= BlueIndex + 1,
    element(BeforeBlueIndex,Size,BeforeBlueSize),
    element(AfterBlueIndex,Size,AfterBlueSize),
    BeforeBlueSize #< AfterBlueSize,

    % Carro Verde Menor de todos
    element(GreenIndex,Colors,3),
    element(GreenIndex,Size,1),

    % Carro Verde depois do Azul
    BlueIndex #< GreenIndex,

    % Carro amarelo está depois do preto

    element(YellowIndex,Colors,1),
    element(BlackIndex,Colors,4),
    BlackIndex #< YellowIndex,

    labeling([],Colors),
    labeling([],Size).


% Exercício outra fila de carros - Exercício 5

% 12 Carros
% 4 amarelos - 1
% 2 verdes - 2
% 3 vermelhos - 3
% 3 azuis - 4
carros2(Cars):-

    length(Cars,12),

    domain(Cars,1,4),
    % Quantidade de cores de cada
    global_cardinality(Cars,[1-4,2-2,3-3,4-3]),

    % O ultimo tem a mesma cor que o primeiro
    element(1,Cars,A),
    element(12,Cars,A),

    % O penultimo tem a mesma cor que o segundo
    element(2,Cars,B),
    element(11,Cars,B),

    % 5º é azul
    element(5,Cars,4),

    % Sequencias de 3 são de cores diferentes
    sequence(Cars),

    % É possível encontrar a sequência 1-2-3-4
    colors_once(Cars,0),

    labeling([],Cars),

    write(Cars),nl.



sequence([_,_]).
sequence([H1,H2,H3|T]):-
    all_distinct([H1,H2,H3]),
    sequence([H2,H3|T]).

colors_once([_,_,_],1).
colors_once([H1,H2,H3,H4|T],Count):-
    (H1 #= 1 #/\ H2 #= 2 #/\ H3 #=3 #/\ H4 #= 4) #<=> B,
    Count1 #= Count + B,
    colors_once([H2,H3,H4|T],Count1).


% Exercício 16 - Líquido ou Pó

% Um terço das pessoas interrogadas não utilizam o pó;
% Dois sétimos das pessoas interrogadas não utiliza o líquido
% 427 pessoas utilizam o líquido e o pó
% Um quinto das pessoas interrogadas não utilizam o produto

liquid(Vars):-

    Vars = [Total,NaoUsa,SoPo,SoLiquido,Ambos],

    domain(Vars,0,10000),

    % People é o valor máximo possível
    maximum(Total,Vars),

    % Soma de todas as partes tem que dar 1

    % Um terço das pessoas interrogadas não utilizam o pó;
    Total #= (Total - (SoPo + Ambos)) *3,

    % Dois sétimos das pessoas interrogadas não utiliza o líquido
    Total * 2 #= (Total - (SoLiquido + Ambos)) *7,

    % 427 pessoas utilizam o líquido e o pó
    Ambos #= 427,
    
    % Um quinto das pessoas interrogadas não utilizam o produto
    Total #= NaoUsa*5,

    % Relação entre o total e os valores
    Total #= NaoUsa + SoPo + SoLiquido + Ambos,

    labeling([],Vars). 
     
% Exercício 12- Biblioteca do joão

% 52 livros de história, dos quais 27 estão em inglês;
% 34 livros encadernados com capa dura dos quais 3 são de história e em francês;
% 46 livros em inglês, a metade deles encadernados com capa comum;
% 20 livros de literatura em francês;
% 31 livros de literatura encadernados com capa comum

library([Vars,Total]):-

    Vars = [A,B,C,D,E,F,G,H],

    domain(Vars,0,10000000),

    % 52 livros de história, dos quais 27 estão em inglês;
    A + B + C + D #= 52,
    A + C #= 27,

    % 34 livros encadernados com capa dura dos quais 3 são de história e em francês;
    C + D + G + H #= 34,
    D #= 3,

    % 46 livros em inglês, a metade deles encadernados com capa comum;
    A + C + E + G #= 46,
    A + E #= 23,

    % 20 livros de literatura em francês;
    F + H #= 20,

    % 31 livros de literatura encadernados com capa comum
    E + F #= 31,

    labeling([],Vars),

    sum_list(Vars,Total).


% Exercício 1 - Sequêcnias mágicas

magic_hexagon(Length):-



    



    


















