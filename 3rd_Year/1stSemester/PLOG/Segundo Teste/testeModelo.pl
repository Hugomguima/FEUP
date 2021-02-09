:- use_module(library(clpfd)).
:- use_module(library(lists)).
:- use_module(library(between)).


% Teste Modelo para o segundo teste

% Exercícios 1, 2 e 3 já foram feitos

% Exercício 4

% Eercício de Cumulative 
% EmbPorObjeto é o tempo
% CustoPorbjeto é o custo


% constroi(30,100,[6,4,12,20,6],[20,50,10,20,15],EmbUsadas,Objetos).
% EmbUsadas = 28,
% Objetos = [1,2,3,5]
constroi(NEmb,Orcamento,EmbPorObjeto,CustoPorObjeto,EmbUsadas,Objetos):-
	
	length(EmbPorObjeto,ListLength),
	length(CustoPorObjeto,ListLength),
	Objetos = [O1,O2,O3,O4],
	
	domain(Objetos,1,ListLength),
	domain([EmbUsadas],0,NEmb),
	domain([SumCost],0,Orcamento),
	
	all_distinct(Objetos),
	
	element(O1,EmbPorObjeto,Emb1),
	element(O2,EmbPorObjeto,Emb2),
	element(O3,EmbPorObjeto,Emb3),
	element(O4,EmbPorObjeto,Emb4),
	
	EmbUsadas #= Emb1 + Emb2 + Emb3 + Emb4,
	EmbUsadas #=< NEmb,
	
	element(O1,CustoPorObjeto,Cost1),
	element(O2,CustoPorObjeto,Cost2),
	element(O3,CustoPorObjeto,Cost3),
	element(O4,CustoPorObjeto,Cost4),
	
	SumCost #= Cost1 + Cost2 + Cost3 + Cost4,
	SumCost #=< Orcamento,
	
	labeling([maximize(EmbUsadas)],[EmbUsadas|Objetos]).
	
% corta([100,45,70], [12,50,14,8,10,90,24], S).
% S = [2,3,3,2,1,1,2] ? ;
% S = [3,3,2,3,1,1,2] ? ;
% no

corta(Pranchas,Prateleiras,PranchasSelecionadas):-
	
	% Ir buscar tamanhos para definir domínios e tamanhos da prancha Selecionada
	length(Pranchas,NPranchas),
	length(Prateleiras,NPrateleiras),
	% Criar A lista das pranchas com o tamanho e dominio definidos
	length(PranchasSelecionadas,NPrateleiras),
	domain(PranchasSelecionadas,1,NPranchas),
	
	length(Tasks,NPrateleiras),
	length(Machines,NPranchas),
	
	findall(Index,between(1,NPranchas,Index),Indexes),
	
	% Criar Tasks
	maplist(create_task,Prateleiras,PranchasSelecionadas,Tasks),
	%get_tasks(Prateleiras,PranchasSelecionadas,Tasks),
	
	% Criar Machines
	maplist(create_machine,Pranchas,Indexes,Machines),
	%get_machines(Pranchas,Machines,1),
	
	cumulatives(Tasks,Machines,[bound(upper)]),
	labeling([],PranchasSelecionadas).
		
	
create_task(Prateleira,Machine,task(0,1,1,Prateleira,Machine)).
create_machine(Prancha,Index,machine(Index,Prancha)).



get_tasks([],[],[]).
get_tasks([Prateleira|Prateleiras],[SelectedBoard|SelectedBoards],[task(0,1,1,Prateleira,SelectedBoard)|Tasks]):-
	get_tasks(Prateleiras,SelectedBoards,Tasks).
	
get_machines([],[],_).
get_machines([Prancha|Pranchas],[machine(Index,Prancha)|Machines],Index):-
	Index2 #= Index + 1,
	get_machines(Pranchas,Machines,Index2).
	
	
	
p2(L1,L2) :-
    length(L1,N),
    length(L2,N),
    %
    pos(L1,L2,Is),
    all_distinct(Is),
    %
	write(Is),nl,
    labeling([],Is).
    %test(L2).

pos([],_,[]).
pos([X|Xs],L2,[I|Is]) :-
    element(I,L2,X),
    pos(Xs,L2,Is).
	
	
	


	
	
	


