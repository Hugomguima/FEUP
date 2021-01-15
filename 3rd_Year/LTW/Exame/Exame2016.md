# Exame 2016

##### Pergunta 1

###### Alinea a)
R1: (0,1,0,1)
R2: (0,0,1,1)
R3: (0,0,1,3)

R4: (0,0,0,1)
R5: (0,0,0,2)
R6: (0,0,0,1)

###### Alinea b)
Title: Blue
1st Par: Black (Default)
2nd Par: Black (Default)
Footer: Red

###### Alinea c)
Title: Green
1st Par: cyan
2nd Par: yellow
Footer: Red


##### Pergunta 2

When you write copy you have the right to copyright the copy you write


###### Alinea a)
When you write [copy you have the right to copyright] the copy you write

###### Alinea b)
Wh[e]n you write copy you have the right to copyright the copy you write

###### Alinea c)
When you [write copy you have the right to copyright the copy you writ]e

###### Alinea d)
When you write copy you have the right to copyright the copy you [write]

###### Alinea e)
When you write co[py] you have the right to copyright the copy you write

###### Alinea f)
When [you write copy you] have the right to copyright the copy you write

##### Pergunta 3


###### Alinea a) e b)
```javascript
'use strict'

let form = document.querySelector("#register");

let inputs = document.querySelectorAll("#register input");

let submit = document.querySelector("#register input[type = submit]");



for(let i=0; i < inputs.length(); i++){
    inputs[i].addEventListener("focusout",function(){
        let value = inputs[i].getAttribute("value");
        let regex =  new RegExp(/(\W\D)/);
        if(value.length >= 8 && regex.match(value)){
            inputs[i].style.border = "2px solid red";
        }
        
    })
}


submit.addEventListener("click",function(event){
    event.preventDefault();

    let request = new XMLHttpRequest();

    request.open("post","verifyusername.php",true);
    request.onload(responseHandler);
    request.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
    request.send(encodeForAjax())

    
})


function responseHandler(){

    let valid = JSON.parse(this.responseText).valid;

    if(valid){
        form.submit();
    }else{
        submit.style.border = "1px solid red";
    }
}


```






##### Pergunta 4
Nao demos