# Exame 2015

##### Pergunta 1

###### Alinea a)
R1: (0,0,1,0)
R2: (0,0,0,2)
R3: (0,1,1,1)

R4: (0,0,1,1)
R5: (0,1,0,1)
R6: (0,1,1,1)

###### Alinea b)
Two Lists: blue (default hyperling value)
1st First: blue
2nd Second: green
Third: yellow


###### Alinea c)

Two Lists: blue (default hyperling value cannot be changed like this)
1st First: cyan
2nd Second: green
Third: cyan


##### Pergunta 2

The thirty-three thieves thought that they thrilled the throne
throughout Thursday.

###### Alinea a)
``/led.+ro/``

The thirty-three thieves thought that they thril[led the thro]ne
throughout Thursday.

###### Alinea b)
``/[thir]+[^e]/``
The [thirty]-three thieves thought that they thrilled the throne
throughout Thursday.

###### Alinea c)
``/(\w{3}.+\1)/``
The thirty-three thieves thought that they thrilled the throne
throughout Thursday.

Trick question, there is no match

###### Alinea d)
``/ll.*e\b/``
The thirty-three thieves thought that they thrilled the throne
throughout Thursday.

###### Alinea e)
``/(h|r|t){3}/``
The thirty-three thieves thought that they thrilled the throne
throughout Thursday.

###### Alinea f)
``/(?<!h)o(?=u)/``
The thirty-three thieves thought that they thrilled the throne
throughout Thursday.

##### Pergunta 3


###### Alinea a) e b)
```javascript
'use strict'

let guessSubmit = document.querySelector("#id");

let guessButton = document.querySelector("imput[name='guess']");

let guessValue = guessButton.value;




guessSubmit.addEventListener("click",function(event){

    event.preventDefault();
    //secret e tries estão declaradas como var, logo tem scope global e podem ser utilizadas
    tries++;
    if(guessValue < secret){
        window.alert("Go Up!");
    } else if(guessValue > secret){
        window.alert("Go Down!");
    } else if(guessValue == secret){
        correct();
    }


})


function correct(){

    window.alert("Correct!!");

    let request = new XMLHttpRequest();

    let username = document.querySelector("imput[name='username']").value;

    request.open("get","save_score.php",true);
    request.onsuccess(function(){
       window.alert("Script was successsfully called!!");
    })
    // Não pede encode mas fiz na mesma
    request.send(encodeForAjax({"username":username,"tries":tries}));

}


```


##### Pergunta 4
Nao demos