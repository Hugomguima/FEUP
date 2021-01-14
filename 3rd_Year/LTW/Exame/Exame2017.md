# Exame 2017

#### Pergunta 1
###### Alinea a)
R1: (0,0,1,1)
R2: (0,0,0,2)
R3: (0,1,1,2)
R4: (0,1,1,2)
R5: (0,0,1,2)
R6: (0,0,0,3)

###### Alinea b)
R1: (0,0,1,1)
R2: (0,0,0,2)
R3: (0,1,1,2)

Buy Bread: blue
Learn Guitar: red
Pay Bills: red
Wash Car: red

###### Alinea c)

Buy Bread: Blue
Learn Guitar: Red
Pay Bills: Green
Wash Car: Inherit



#### Pergunta 2

Washing the washing machine while watching the washing machine washing washing

###### Alinea a)
/wa.*ing/

Washing the [washing machine while watching the washing machine washing washing]

###### Alinea b)
Wash[ing] the washing machine while watching the washing machine washing washing

###### Alinea c)
Wash[ing the washing] machine while watching the washing machine washing washing

###### Alinea d)
[Was]hing the washing machine while watching the washing machine washing washing

###### Alinea e)
Washing the washing ma[ch]ine while watching the washing machine washing washing

###### Alinea f)
W[ashing the wa]shing ma[ch]ine while watching the washing machine washing washing


#### Pergunta 3

```javascript

let photos = document.getElementById('products');

let listItems = document.querySelectorAll('div#photos ul li a');

let list = document.querySelectorAll('div#photos ul');

let loadable = document.querySelector('div#photos .load');


for(let i=0; i < listItems.length;i++>)
    listItems[i].addEventListener("click",function(){
        let data = document.querySelector('div#photos .large');
        let current = lisItems[i].getAttribute.('src');
        data.setAttribute("src","large/" + src);
    })


loadable.addEventListener("click",function(event){

    event.preventdefault();

    let request = new XMLHttpRequest();

    request.open('get','getrandomimages.php',true);
    request.onload(handleReply);
    request.send();
   
}

function handleReply(){
    let data = JSON.parse(this.responseText);

    for(let i = 0; i < data.length; i++){
        img.setAttribute("src",data[i]);
        list.appendChild()
    }
}


```

#### Pergunta 4

##### Alinea a)
O título de todos os livros.
``
//authors/author/book/text()
``

##### Alinea b)
O título dos livros escritos depois de 1900.
``
//authors/author/book[@year > 1900]/text()
``

##### Alinea c)
Os anos em que foram escritos livros por autores Ingleses.
``
//authors/author[@country='England']/book/@year
``

##### Alinea d)
O nome dos autores que escreveram livros do tipo Novel.
``
//authors/author[book/@type="Novel"][@name]
//authors/author[book[@type="Novel"]][@name]
//authors/author[book[@type="Novel"]]/@name
``