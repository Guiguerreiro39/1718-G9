# Aula 14

## Injection

### Pergunta 1.1

* O resultado obtido usando o nome Smith foi o seguinte:

![Tópico 1](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula14/img/1.1.1.png)

* A tautologia usada foi a seguinte: 'Smith OR 1=1' . E isso permitiu-nos obter a lista de todos os utilizadores 
como podemos verificar na imagem seguinte.

![Tópico 2](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula14/img/1.1.2.png)

### Pergunta 1.2

Para realizarmos a Injection e obter todos os sítios que tem previsão do tempo disponível tivemos que acrescentar á query SQL a seguinte 
tautoligia 'OR 1 = 1'. o resultado pode ser visualizado na imagem seguinte.

![Tópico 2](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula14/img/1.2.png)

### Pergunta 1.3

Para alterarmos o valor do salário do utilizador 101 tivemos que executar o comando 'ID:101; set employee salary = 19999'.

![Tópico 3](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula14/img/1.3.png)

## XSS

## Pergunta 2.1

Verificou-se que, ao tentar utilizar os campos de quantidade na lista de compras, este alterava os caracteres especiais (< e >) como se vê na fígura.

![Tópico 1](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula14/img/2.png)

Nos campos seguintes, o credit card number e o digit access code, apesar de já não alterar caracteres especiais, não se conseguiu correr o script no campo do credit card number mas conseguiu-se com sucesso no campo do digit access code.

![Tópico 1](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula14/img/1.png)

![Tópico 1](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula14/img/3.png)

## Experiência 2.2

Conseguimos utilizar o script indicado no campo da mensagem para correr um script no browser de quem a for ler. É necessário o título da mensagem para que esta seja gravada.

![Tópico 2](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula14/img/2.1.png)

![Tópico 1](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula14/img/2.2.png)


## Quebra na autenticação
