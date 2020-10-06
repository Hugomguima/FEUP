% male(X) -> X is male

male('Aldo Burrows').
male('Lincoln Burrows').
male('LJ Burrows').
male('Michael Scofield').

% female(X) -> X is male

female('Christina Rose Scofield').
female('Lisa Rix').
female('Sara Tancredi').
female('Ella Scofield').

% parent(X,Y) -> X is Y's parent

parent('Aldo Burrows','Lincoln Burrows').
parent('Christina Rose Scofield','Lincoln Burrows').
parent('Aldo Burrows','Michael Scofield').
parent('Christina Rose Scofield','Michael Scofield').
parent('Lisa Rix','LJ Burrows').
parent('Lincoln Burrows','LJ Burrows').
parent('Sara Tancredi','Ella Scofield').
parent('Michael Scofield','Ella Scofield').

/* Exercício 1.a)
 Quem são os pais de Michael?

 parent(X,'Michael Scofield').
*/

/* Exercício 1.b)
 Quem são os filhos de Aldo?

 parent('Aldo Burrows',X).
*/


