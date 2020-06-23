## Aula 2 <p> Transformações

Na classe MyScene.js, é possível utilizar estas funções:  

```javascript
this.translate(x,y,z);  
this.rotate(ang,x,y,z);  
this.scale(x,y,z);  
```

Para fazer alterações, é necessário utilizar também os comandos:
```javascript
>this.pushMatrix();  
>this.popMatrix();  
```

###### Exemplo:
Alteração de posição e tamanho de um Cubo  

```javascript  
this.pushMatrix();
this.scale(10,12,1);
this.translate(-0.5,0,-1.01);
this.cube.display();
this.popMatrix();
```
###### Importante!
As alterações são feitas na ordem inversa da sua escrita, como em álgebra.  
No caso anterior, primeiro foi feita a translação, e só depois o escalamento!!  

### Tangram
Para desenhar o Tangram na aula, é preciso utilizar os objetos criados na primeira aula e, em seguida, aplicar as transformações necessárias para os recolocar nas posições pretendidas

![Tangram](ex2/Tangram.png)

### Cubo
É simplesmente necessário criar 6 faces do cubo e inicializar os vértices na ordem certa.  
Em seguida, deve-se reposicionar o cubo atrás do Tangram.

![cubo](ex2/cube.png)
