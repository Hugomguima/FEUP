## Exercicise 2.2 -> N-Puzzle

* Representação de estados
    - Matriz Quadrada de tamanho N
    - Valores da matriz entre 0 e N*N-1
* Estado Inicial
    - 

* Operators

| Name | PreCond | Effects | Cost |
| - | - | - | - |
|down | ys < n | B[xs,ys] = B[xs,ys+1]; = B[xs,ys+1] = 0; Ys = Ys+1| 1 |


### heuristic

```py
def heuristica(board):
    n = 0
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] != x + y*len(board) and board[x][y] != 0:
                value = board[x][y]
                xObj = value % len(board)
                yObj = value / len(board)
                n += abs(x - xObj) + abs(y - yObj)
    return n
```