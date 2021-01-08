:- use_module(library(clpfd)).

% Exercício 3, dar fix ao prolog com restrições

prog2(N,M,L1,L2) :-
	length(L1,N),
	N1 is N-1, length(L2,N1),
	domain(L1,1,M),
	domain(L2,1,M),
	
	append(L1,L2,Vars),
	
	all_distinct(Vars),
	
	
	check(L1,L2),
	labeling([],L1).
	
	
check([_],[]).
check([A,B|R],[X|Xs]) :-
	X #= A+B,
	check([B|R],Xs).
	
	
% Exercício 4

% Diferenças das alturas entre homens e mulheres seja inferior a um delta
% Homem nunca poderá sr mais baixo do que a mulher


% gym_pairs([95,78,67,84],[65,83,75,86],10,Pairs).
% Pairs = [1-4,2-3,3-1,4-2] ? ;
% no
% gym_pairs(+MenHeights,+WomenHeights,+Delta,-Pairs)
gym_pairs(MenHeights,WomenHeights,Delta,Pairs):-

	length(MenHeights,ListLength),
	length(WomenHeights,ListLength),
	length(Pairs,ListLength),
	
	append(MenIndex,WomenIndex,Vars),
	
	% Seperate indexes may be needed
	length(MenIndex,ListLength),
	length(WomenIndex,ListLength),
	
	all_distinct(MenIndex),
	all_distinct(WomenIndex),
	
	add_restrictions(MenHeights,WomenHeights,MenIndex,WomenIndex),
	
	labeling([],Vars),
	
	createPairs(MenIndex,WomenIndex,Pairs).
	
	

add_restrictions(_,_,[],[]).
add_restrictions(MenHeights,WomenHeights,[ManIndex|MenIndex],[WomanIndex|WomenIndex]):-
	element(ManIndex,MenHeights,ValueMan),
	element(WomanIndex,WomenHeights,ValueWoman),
	ValueMan + ValueWoman #=< Delta,
	ValueMan #> ValueWoman,
	add_restrictions(MenHeights,WomenHeights,MenIndex,WomenIndex).
	
createPairs([],[],[]).
createPairs([M|T1],[W|T2],[M-W|T3]):-
	createPairs(T1,T2,T3).
	
% Exercício 5

make_pairs2(_, _, _, [], [], []).
make_pairs2(MenHeights, WomenHeights, Delta, [Refe | RefeList], [IndexM | MVars], [IndexW | Vars]) :-
    element(IndexM, MenHeights, HeightM),
    element(IndexW, WomenHeights, HeightW),
    ((HeightM - HeightW #< Delta) #/\ (HeightM #> HeightW)) #<=> Refe,
    make_pairs2(MenHeights, WomenHeights, Delta, RefeList, MVars, Vars).

parse_values([], [], [], []).
parse_values([0 | Refe], [M | Mvars], [W | WVars], Pairs) :-
    parse_values(Refe, Mvars, WVars, Pairs).
parse_values([1 | Refe], [M | Mvars], [W | WVars], [ M-W | Pairs]) :-
    parse_values(Refe, Mvars, WVars, Pairs).

optimal_skating_pairs(MenHeights, WomenHeights, Delta, Pairs) :-
    length(MenHeights, PairsLength),
    length(MVars, PairsLength),
    domain(MVars, 1, PairsLength),

    length(WVars, PairsLength),
    domain(WVars, 1, PairsLength),

    all_distinct(MVars),
    all_distinct(WVars),
    make_pairs2(MenHeights, WomenHeights, Delta, Refe, MVars, WVars),
    append(Refe, MVars, Vars1),
    append(Vars1, WVars, Vars2),
    sum(Refe, #=, Max),
    % Isto para ter todos os resultados com 3 (primeiro caso, segunda opção é a do stor)
    % Max #= 3,
    % labeling([], [Max | Vars2]),
    labeling([maximize(Max)], [Max | Vars2]),
    parse_values(Refe, MVars, WVars, Pairs).
	




	
	

	
	

	
	
	
	