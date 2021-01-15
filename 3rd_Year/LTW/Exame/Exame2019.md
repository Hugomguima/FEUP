Resolução do exame 2019
##### Pergunta 1
Answer: a) title
##### Pergunta 2
Answer: b) label around
##### Pergunta 3
Answer: a) Ids are unique and each element only has one
##### Pergunta 4
Answer: c)
##### Pergunta 5
Answer: a)
##### Pergunta 6
Answer: b)
##### Pergunta 7
Answer: c)
##### Pergunta 8
Answer: c)
##### Pergunta 9
Answer: c) ? not b) :/
##### Pergunta 10
Answer: a)
##### Pergunta 11
Answer: b)
##### Pergunta 12
Answer: c)
##### Pergunta 13
Answer: R1: (0,0,1,1)
##### Pergunta 14
Answer: R2: (0,0,2,1)
##### Pergunta 15
Answer: R3: (0,1,0,1)
##### Pergunta 16
Answer: R4: (0,1,0,1)
##### Pergunta 17
Answer: R5: (0,0,3,2)
##### Pergunta 18
Answer: R6: (0,1,2,2)
##### Pergunta 19
Answer: c) purple 
A -> Magenta
B -> Blue Mesma prioridade que Purple
Purple poruq eé a ultima, desempatando por terem a mesma prioridade

##### Exercício 20
A [groundhog would hog all the ground he could hog, if a groundhog could hog g]ro

##### Exercício 21
A [groundhog would hog] all the ground he could hog, if a groundhog could hog gro

##### Exercício 22
A groundhog would hog a[ll] the ground he could hog, if a groundhog could hog gro

##### Exercício 23
A groundhog would hog all the [ground] he could hog, if a groundhog could hog gro


##### Exercício 24
A groundhog would hog all the ground he could hog, if a groundhog could hog [gro]

##### Exercício 25
A [groundhog would hog all the gro]und he could hog, if a groundhog could hog gro

##### Exercício 26

```php
<?php
include_once 'game.php';

$id = $_POST['id'];
$position = $_POST['position'];

if(isset($position))
    play($id,$position);

echo json_encode(state($id));

?>
```
 
##### Exercício 27 e 28

```javascript

let section = document.getElementById('tic-tac-toe');
let allSquares =  document.getElementByClass('square');

document.addEventListener("load",sendEvent);

let dataId = section.getAttribute('data-id');
    
for(let i = 1; i < 9; i++ ){
    allSquares[i].addEventListener("click",function() {
        let request = new XMLHttpRequest();
        request.addEventListener('load', requestListener3);
        request.open("post",'play.php',true);
        request.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
        request.send(encodeForAjax({id:dataId,position:i}));


    });
}

function sendEvent(event){

    let dataId = section.getAttribute('data-id');

    let request =new XMLHttpRequest();
    request.onload = requestListener;
    request.open("post","play.php",true);
    request.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
    request.send(encodeForAjax({id:dataId}))

}

function requestListener(){

    let response = JSON.parse(this.reponseText);

    let state = document.getElementById('state');
    state.innerHTML = response.state;

    for(let i = 0; i < squares.length ; i++){
        squares[i].innerHTML = response.squares[i]
    }
}

function requestListener2(){

    let squares = JSON.parse(this.reponseText).squares;
    let child = section.firstElementChild; 

    for(let i = 0; i < 9;i++ ){
        child.innerHtml = square[i];
        child.nextElementSibling;
    }
}


```


##### Pergunta 29
``
//recipes/recipe/ingredients/ingredient/text()
``
##### Pergunta 30
``
//recipes/recipe[name='Mixed Toast']/ingredients/count(ingredient)
``
##### Pergunta 31
``
//recipes/count(recipe[@difficulty = 'medium'])
``
##### Pergunta 32
``
//recipes/recipe[ingredients/ingredient/text() = "Apple"]/name/text()
``



