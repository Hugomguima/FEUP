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
	
	length(IndexConcelhosVisitados,NDias),
	
	all_distinct(IndexConcelhosVisitados),
	
	check_distances(Nomes,Distancias,NEleitores,IndexConcelhosVisitados,NDias,DistTotal,TotalEleitores),
	
	DistTotal #=< MaxDist,

	labeling([maximize(TotalEleitores)],[DistTotal,TotalEleitores|IndexConcelhosVisitados]).
	
	maplist(switch_indexes,IndexConcelhosVisitados,Nomes,ConcelhosVisitados).
	

check_distances(_,_,_,[],0,0,0).
check_distances(Nomes,Distancias,Eleitores,[ConcelhoVisitado|IndexConcelhosVisitados],NDias,DistTotal,TotalEleitores):-
	element(ConcelhoVisitado,Distancias,Dist),
	element(ConcelhoVisitado,Eleitores,NEleitores),
	DistTotal #= Dist + NextDist,
	Ndias2 #= NDias - 1,
	TotalEleitores #= NEleitores + NextEleitores,
	check_distances(Concelhos,Distancias,Eleitores,IndexConcelhosVisitados,NDias2,NextDist,NextEleitores).
	
	
%concelhos(3,700,CVs,Dist,Te).

switch_indexes([Index|IndexConcelhosVisitados],Nomes,[ConcelhoVisitado|ConcelhosVisitados]):-
	element(Index,Nomes,ConcelhoVisitado).
	



