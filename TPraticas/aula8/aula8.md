# Aula 8 - 9/4/2018


## Pergunta 1.1.1:
A fórmula que nos vai dar o resultado aproximado do número de bugs é a seguinte:


Número de bugs = ((Nºlinhas de código)/1000) * limite

limite superior = 50

limite inferior = 5


#### Limite Superior:
* Facebook: (61000000 / 1000) * 50 = 61 000 * 50 = 3 050 000 bugs
* Software de Automóveis: (100000000 / 1000) * 50 = 5 000 000 bugs
* Linux 3.1: (15000000 / 1000) * 50 = 750 000 bugs
* Todos os serviços de internet da Google: (2000000000 / 1000) * 50 = 100 000 000 bugs

#### Limite Inferior:
* Facebook: (61000000 / 1000) * 5 = 61 000 * 5 = 305 000 bugs
* Software de Automóveis: (100000000 / 1000) * 5 = 500 000 bugs
* Linux 3.1: (15000000 / 1000) * 5 = 75 000 bugs
* Todos os serviços de internet da Google: (2000000000 / 1000) * 5 = 10 000 000 bugs


## Pergunta 1.1.2:
Alguns desses bugs podem representar vulnerabilidades mas apenas vamos sabendo que um software tem uma determinada vulnerabilidade quando essa é descoberta.
Outros bugs podem não representar nenhuma vulnerabilidade para o software em causa.


## Pergunta 1.2:


#### Vulnerabilidades de Projeto:
Esta vulnerabilidade é introduzida durante a fase de projeto do software(obtenção de requisitos e desenho).
Por exemplo, quando estamos a planear o desenvolvimento de um software específico e se um intruso obter os requisitos e o desenho desse software pode ficar a saber como esse software vai implementado e pode ir tentando encontrar vulnerabilidades.
Outro exemplo desta vulnerabilidade é um utilizador obter os requisitos e o desenho e usa-los para proveito próprio isto pode acontecer se uma empresa concorrente obter estes dados e tentar antecipar-se à outra empresa no lançamento desse produto para o mercado. 


#### Vulnerabilidades de Codificação:
A vulnerabilidade é introduzida durante a programação do software, ou seja, introduzir um bug com implicações de segurança.
Por exemplo, quando introduzimos um bug com o intuito de diminuir a segurança de um determinado software para conseguirmos aceder a informações confidenciais pondo em causa a segurança da outra empresa.
Outro exemplo é quando introduzimos um bug numa determinada funcionalidade de modo a ela não funcionar do modo correto benefeciando quem introduziu esse bug, isso pode ser alicado por exemplo em transações.


#### Vulnerabilidades Operacionais:
A vulnerabilidade é causada pelo ambiente no qual o software é executado ou pela sua execução.  


## Pergunta 1.3:
