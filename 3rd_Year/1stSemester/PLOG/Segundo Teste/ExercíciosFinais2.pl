:- use_module(library(clpfd)).
:- use_module(library(lists)).
:- use_module(library(between)).


% Exercício 13

% A distância contempla a ida e volta
% concelho(Nome,Distancia,NEleitoresIndecisos)
concelho(x,120,410).
concelho(y,10,800).
concelho(z,543,2387).
concelho(w,3,38).
concelho(k,234,376).



% concelhos(+NDias,+MaxDist,-ConcelhosVisitados,-DistTotal,-TotalEleitores)
concelhos(NDias,MaxDist,ConcelhosVisitados,DistTotal,TotalEleitores):-

	findall(Nome,concelho(Nome,Dist,Eleitores),Nomes),
	findall(Dist,concelho(Nome,Dist,Eleitores),Distancias),
	findall(Eleitores,concelho(Nome,Dist,Eleitores),NEleitores),
	
	
	length(Distancia,N),
	MaxDiasN is NDias - 1,
	MaxDias in 0..MaxDiasN,
	DiasMaxFirst #= NDias - MaxDias,
	length(IndexConcelhosVisitados,DiasMaxFirst),
	domain(IndexConcelhosVisitados,1,N),
	
	
	length(IndexConcelhosVisitados,NDias),
	
	all_distinct(IndexConcelhosVisitados),
	
	check_distances(Nomes,Distancias,NEleitores,IndexConcelhosVisitados,NDias,DistTotal,TotalEleitores),
	
	DistTotal #=< MaxDist,

	labeling([maximize(TotalEleitores)],[DistTotal,TotalEleitores|IndexConcelhosVisitados]),
	switch_indexes(IndexConcelhosVisitados,Nomes,ConcelhosVisitados).
	

check_distances(_,_,_,[],_,0,0).
check_distances(Nomes,Distancias,Eleitores,[ConcelhoVisitado|IndexConcelhosVisitados],NDias,DistTotal,TotalEleitores):-
	element(ConcelhoVisitado,Distancias,Dist),
	element(ConcelhoVisitado,Eleitores,NEleitores),
	DistTotal #= Dist + NextDist,
	Ndias2 #= NDias - 1,
	TotalEleitores #= NEleitores + NextEleitores,
	check_distances(Concelhos,Distancias,Eleitores,IndexConcelhosVisitados,NDias2,NextDist,NextEleitores).
	
	
	
% concelhos(+NDias,+MaxDist,-ConcelhosVisitados,-DistTotal,-TotalEleitores)
concelhos2(NDias,MaxDist,ConcelhosVisitados,DistTotal,TotalEleitores):-

	findall(Nome,concelho(Nome,Dist,Eleitores),Nomes),
	findall(Dist,concelho(Nome,Dist,Eleitores),Distancias),
	findall(Eleitores,concelho(Nome,Dist,Eleitores),NEleitores),
	
	length(Distancias,Length),
	length(ListBooleans,Length),
	domain(ListBooleans,0,1),
	
	scalar_product(Distancias,ListBooleans,#=,DistTotal),
	scalar_product(NEleitores,ListBooleans,#=,TotalEleitores),
		
	%sum(ListBooleans,#=<,NDias),
	domain([Val],0,NDias),
	global_cardinality(ListBooleans,[0-X,1-Val]),
	
	DistTotal #=< MaxDist,
	
	labeling([maximize(TotalEleitores)],[DistTotal,TotalEleitores|ListBooleans]),
	
	findall(I,nth1(I,ListBooleans,1),IndexList),
	switch_indexes(IndexList,Nomes,ConcelhosVisitados).
	
	switch_indexes([],_,[]).
switch_indexes([Index|IndexConcelhosVisitados],Nomes,[ConcelhoVisitado|ConcelhosVisitados]):-
	nth1(Index,Nomes,ConcelhoVisitado),
	switch_indexes(IndexConcelhosVisitados,Nomes,ConcelhosVisitados).
	
	
% Exercício 12

put_values([_]).
put_values([A, B]) :-
  ((A #> B) #\/ (B #< A)).
put_values([E1, E2, E3 | Rest]) :-
  (((E2 #< E3) #/\ (E2 #< E1)) #\/ ((E2 #> E3) #/\ (E2 #> E1))),
  put_values([E3 | Rest]).

ups_and_downs(Min, Max, N, L) :-
	length(L, N),
    domain(L, Min, Max),
    put_values(L),
    labeling([], L).
	
	
	
place(Starts) :-
	Starts = [A, B, C, D],
	domain(Starts, 1, 15),
	Lines = [
	line(A, 4, r),
	line(B, 2, r),
	line(C, 2, r),
	line(D, 3, r)
	],
	disjoint1(Lines, [margin(r, r, 2)]),
	labeling([], Starts).
	
	


	



