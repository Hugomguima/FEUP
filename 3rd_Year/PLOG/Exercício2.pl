% piloto(X) -> X é Piloto
piloto('Lamb').
piloto('Besenyei').
piloto('Chambliss').
piloto('MacLean').
piloto('Mangold').
piloto('Jones').
piloto('Bonhomme').

% equipa(X,Y) -> A equipa X tem o piloto Y
equipa('Breitling','Lamb').
equipa('RedBull','Besenyei').
equipa('RedBull','Chambliss').
equipa('MediterraneanRacingTeam','MacLean').
equipa('Cobra','Mangold').
equipa('Matador','Jones').
equipa('Matador','Bonhomme').

% circuito(X) -> X é um circuito
circuito('Istanbul').
circuito('Budapeste').
circuito('Porto').

% venceu(X,Y) -> X venceu o circuito Y
venceu('Jones','Porto').
venceu('Mangold','Budapeste').
venceu('Mangold','Istanbul').

% gates(X,Y) -> X tem Y gates
gates('Istanbul',9).
gates('Budapeste',6).
gates('Porto',5).

% Exercício 1: Quem venceu a corrida no Porto?

% won(X) :- equipa(X,Y), venceu(Y).
