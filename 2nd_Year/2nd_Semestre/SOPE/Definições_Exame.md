# Definitions

### Race condition
Uma "Race condition" ocorre quando pelo menos 2 threads podem aceder/modificar dados partilhados e tentar fazê-lo ao mesmo tempo. Como o algoritmo de escalonamento permite a troca entre threads a qualquer momento, não é possível saber a ordem pela qual as threads irão tentar aceder aos dados partilhados. Deste modo, o resultado da alteração dos dados depende do algorirtmo de escalonamento, onde as threads em causa estão a "competir" (ou concorrer) para aceder/modificar os dados partilhados.

### Trap
Uma "trap" no contexto de computação e Sistemas Operativos, é também conhecida como uma exceção ou uma falha.

Os microprocessadores possuem "traps" para várias situações de erro, permitindo a execução de código enquanto está a ocorrer algum problema no processador. São geralmente utilizadas pelo SO para recuperação de erros, e correspondem a subrotinas forçadas pelo processador quando deteta um problema, tratando do mesmo.

Nesta cadeira, o trap é abordado dado que podem ocorrer erros na paginação, nomeadamente, a falta de páginas, que origina um "trap", quando a referência na tabela de páginas é inválida, sendo necessário suporte de hardware para permitir o recomeço de uma instrução que falhou por falta de página.

Par além disso, pode ocorrer um "trap" num fork, caso haja um erro na criação de um processo filho e o processador necessite de tratar de esse problema.

### Semaphore

Um semáforo corresponde a uma varíavel utilizada para controlar o acesso a um recurso que é comum a vários processos concorrentes. É uma variável utilizada para resolver problemas de seções críticas, alcançando a sincronização em situações de multiprocessamento.

Um semáforo está associado a uma variável inteira que utiliza duas operações atómicas, wait() e signal() para sincronizar processos. A operação wait() decrementa o valor inteiro, e, se esse valor não for positivo, nenhuma operação é executada. A operação signal incrementa esse mesmo valor. Deste modo, sendo o inteiro o número de recursos disponíveis, o incremento corresponde ao aumento de recursos disponíveis, enquanto o decremento corresponde á remoção de recursos.


### Mutex

Um mutex corresponde a uma flag de exclusão. Funciona como um "guarda" de uma seção crítica do código, permitindo que um processo bloqueie o acesso a uma váriavel partilhada por outros processos concorrentes. Os mutexes são utilizados, portanto, para exclusão mútua do acesso a um recurso partilhado, garantindo a sincronização em ambientes de multiprocessamento.


### Distinction between mutex and semaphore

Embora quer mutexes quer semáforos sejam utilizados como primitivas de sincronização de processos concorrentes, há uma grande diferença entre eles. No caso de um mutex, apenas o processo que bloqueia ou adquire o mutex o pode desbloquear, enquanto um processo á espera de um semáforo pode ser sinalizado por um diferente processo, para que possa aceder á seção crítica.

Outra distinção está associada ao facto de u mutex ter apenas os estados de bloqueado/desbloqueado, enquanto um semáforo utiliza um valor inteiro, permitindo o acesso de multiplos processos a uma variável partilhada.

Em geral, considera-se que um mutex corresponde a um semáforo inicializado a 1.

### Virtual memory and physical memory

Memória virtual corresponde a uma abstração que dá ao programador a ilusão de ter um memória infinita disponível no seu sistema.

O Mapeamento de memória virtual corresponde ao endereço físico existente. O sistema operativo cria tabelas de páginas para lidar com este mapeamento

Um SO necessita de um certa quantidade de RAM(memória) para funcionar. A memória virtual é armazenada no disco rígido, quando a memória não tem capacidade de armazenar todos os dados, permitindo uma rápida troca de dados entre o disco e a memória.

### Deadlock

Um "deadlock" corresponde a uma situação de encravamento em que um programa não consegue aceder a um recurso que necessita para continuar. Quando um processo se encontra em "deadlock", pode ficar preso â espera durante um tempo indefninido.

### Starvation
"Starvation" ocorre quando um processo não consegue aceder aos recursos que necessita para continuar porque os recursos estão a ser alocados para outros processos concorrentes.

"Starvation" distingue-se de "deadlock", pois em vez de o processo ficar preso num estado de espera indefinido, o processo encontra-se indefinidamente num estado indeterminado, não conseguindo alcançar o estado que pretende, dado que um recurso que necessita para continuar está a  ser utilizado por outro processo. "Starvation" está geralmente associado a loops infinitos em que o processo não está á espera, mas está continuamente a fazer uma tarefa que "não chega a lado nenhum".

### Busy waiting

Busy waiting corresponde a uma técnica/situação em que o processo está repetidamente a verificar se uma condição é verdadeira. Deve ser evitado porque está a ocupar o processador, o qual poderia estar a ser utilizado por outros processos concorrentes.

Busy waiting pode, em certas situações, ser corrigido com o uso de semáforos e mutexes, de modo a bloquear o processo, sinalizando-o de volta quando necessário, cedendo o uso do CPU a outros processos.


### Ficheiro
- programa ou conjunto de dados gravados em memória secundária e identificado por um nome
- conjunto de dados persistentes, geralmente relacionados entre si e identificados por um nome

Um ficheiro possui atributos e operação que os manipulam. Também possuem um tipo, para se saber quais operações são permitidas

Corresponde a uma coleção de blocos(unidade de transferência física entre o disco e a memória)

### Diretório

Um diretório é um ficheiro especial, que permite o acesso a outros ficheiros. Pode ser estruturado de diversas formas, tais como:
- único nível
- em árvore
- grafo acíclico
- grafo genérico
Um diretório permite a localização rápida de ficheiros, agrupamento lógico dos ficheiros de acordo com as suas propriedades, e ainda a possibilidade de haver 2 ficheiros co o mesmo nome em diferentes diretórios

### I-node

Dada a necessidade de armazenar ficheiros no disco, existem vários métodos de alocação de ficheiros. No caso da alocação indexada, em UNIX, são utilizados i-nodes.

- Cada ficheiro, diretório ou dispositivo de I/O tem um i-node associado
- Cada entrada do diretório aponta p/ o I-node respetivo
- Cada i-node contém os vários dados associados ao ficheiro, tais como:
    - Tipo de ficheiro
    - Permissões de acesso
    - IDs do ficheiro
    - localização de blocos, entre outros...


### Multiprogramação
Multiprogramação corresponde á execução intercalada de processos. São mantidas várias tarefas em memória simultaneamente, e a CPU é partilhada entre eles.

São utilizadas políticas de escalonamento, gestão de memória, proteção, e gestão do CPU.
- Escalonamento do CPU - o sistema deve escolher, entre os vários processos a executar, aquele que vai ser escolhido
- Gestão de Memória - alocar a memória aos diferentes processos
- Gestão de I/O - controlar o acesso aos dispositivos de I/O
- Proteção - não deve haver possibilidade de os processos se afectarem mutuamente
em todos os níveis

A multiprogramação permite:
- 1 processo em execução
- Múltiplos processos algures entre entre o início e o fim de execução

### Multiprocessamento

Multiprocessamento corresponde á execução concorrente de processos por múltiplos CPUs. Tal como na multiprogramação, é necessário alocar memória para os diferentes processos, utilizar políticas de escalonamento de processos, controlar o acesso aos dispositivos I/O, e proteger os dados de situações conflituosas.

O Multiprocessamento permite:
- Múltiplos processos em execução
- Múltiplos processos algures entre entre o início e o fim de execução

### Seção critica

Quando um processo executa código que manipula dados / recursos partilhados, diz-se que o processo está na sua seção crítica (mais info está nos slides de sincronização)

### Trashing

Acontece quando um processo passa mais tempo em atividades de paginação do que a executar.
Causas e sintomas de thrashing : ( Slides Memória virtual, página 22)

### DMA
O acesso direto à memória necessita do uso de um controlador ligado ao barramento do sistema, e permite, como o nome indica, o acesso direto á Memória, sem a intervenção do CPU. Deste modo é possível executar operações I/O sem o uso do CPU, cedendo-o a outros processos, contribuindo para a multiprogramação.

Quando o DMA termina, é gerada uma interrupção que indica que é necessário o uso do CPU novamente
