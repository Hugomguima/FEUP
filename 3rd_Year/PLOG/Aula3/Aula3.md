# Aula 3
## Exercicio 1

- a) yes
- b) no
- c) H = apple, T=[broccoli,refrigerator]
- d) H = a, T=[b,c,d,e]
- f) H = a, T = [[b,c,d]]
- g) H = apples, T = []
- h) no
- i) One = apple,
 Two = sprouts,
T = [fridge,milk]
- j)  X = a
Y = _01
T = _03 
Z = [_01,_03]
- k) ) H = apple
T = [_01]
Z = _01
- l) yes


## Exercício 2

### a)

membro(X,L) :- member(X,[L]).
membro(X,L) :- append(_,[X|_],L).