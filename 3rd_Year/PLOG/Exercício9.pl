aluno(joao, paradigmas).
aluno(maria, paradigmas).
aluno(joel, lab2).
aluno(joel, estruturas).

frequenta(joao, feup).
frequenta(maria, feup).
frequenta(joel, ist).
professor(carlos, paradigmas).
professor(ana_paula, estruturas).
professor(pedro, lab2).

funcionario(pedro, ist).
funcionario(ana_paula, feup).
funcionario(carlos, feup). 

/* a) Quem são os alunos do professor X?

professor(X,_Y) , aluno(Z,_Y).
X = carlos, Z = joao
X = carlos, z = maria
x = ana_paula, z = joel
x = pedro z, = joel

*/

/* b) Quem são as pessoas da universidade X? (alunos ou docentes) 
frequenta(Y,X)
*/


/* c) Quem são as pessoas da universidade X? (alunos ou docentes) 
frequenta(Y,X)

colega(A,B) :- aluno(A,C) , aluno(B,C), A @< B.
 ; (frequenta(A,C) , frequenta(B,C)).


amigo(A,B) :- aluno(A,B)
*/

