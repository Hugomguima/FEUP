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

% aviao(X,Y) -> o Aviao X é pilotado por Y
aviao('MX2','Lamb').
aviao('Edge540','Besenyei').
aviao('Edge540','Chambliss').
aviao('Edge540','MacLean').
aviao('Edge540','Mangold').
aviao('Edge540','Jones').
aviao('Edge540','Bonhomme').

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

% ganha(X) -> a equipa(X) ganha 
ganha(X) :- equipa(X,Y), venceu(Y,Z).

/* Exercício a: Quem venceu a corrida no Porto?

venceu(X,'Porto').
X = 'Jones'

*/

/* Exercício b: Qual a equipa que ganhou no Porto? 

equipa(X,Y), venceu(Y,'Porto').
X = 'Matador'
Y = 'Jones'

*/

/* Exercício c:

venceu(X,_Y) , venceu(X,_Z) , _Y @< _Z.
X = 'Mangold'.

*/

/* Exercício d:

gates(X,Y) , Y > 8.
X = 'Instabul'
Y = 9

*/

/* Exercício e:

aviao(X,Y) , X \= 'Edge540'.
X = 'MX2'
Y = 'Lamb'
*/



