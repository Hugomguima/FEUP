A, B, C, D, E, F

A -> B,E
B -> C,D

Chave: A,F

1º Passo -> Simplificar as DF, eliminando as redundantes

A -> B
A -> E

B -> C
B -> D

2º Passo -> Construir novas relações baseadas nas DF anteriores

R1(A,B,E);
R2(B,C,D);

3º Passo -> Adicionar uma relação contendo a chave, caso não exista

R3(A,F);


Deste modo, dividimos a Relação existente nas 3 formadas, as quais estão na 3NF.

R1(A,B,E);
R2(B,C,D);
R3(A,F);
