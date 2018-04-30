# Aula 10


## Pergunta 1.1:
Verifique o que ocorre no mesmo programa escrito em Java (LOverflow2.java), Python (LOverflow2.py) e C++ (LOverflow2.cpp), executando-os.
Explique o comportamento dos programas.


## Resposta 1.1:

* LOverflow2.java: O programa dá erro quando se pretende guardar um array superior ao tamanho que o mesmo foi inicializado, neste caso de tamanho 10, ou seja dá erro por não ter espaço alocado para guardar todos os valores. 
Erro -> Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: 10

* LOverflow2.py: Semelhante ao programa de Java, dá erro quando se pretende introduzir mais que o número permitido do tamanho do array porque o programa só suporta tamanho 10, e só para de correr quando a variável count é 0. Essa situação pode originar um buffer overflow. 
Erro -> IndexError: list assignment index out of range

* LOverflow2.cpp: Aqui já não acontece o mesmo, pois não existe controlo de acesso, e não dá erro. A partir do índice do tamanho do array definido, o programa vai escrevendo na posição de memória adjacente.



## Pergunta 1.2:
Verifique o que ocorre no mesmo programa escrito em Java (LOverflow3.java), Python (LOverflow3.py) e C++
(LOverflow3.cpp), executando-os.
Explique o comportamento dos programas.

## Resposta 1.2:

* LOverflow3.java: O programa coloca num array até 10 posições os valores ordenados na forma decrescente.
O programa dá erro ao correr com um valor maior que 10 porque não pode guardar mais do que 10 elementos no array, dá o seguinte erro: Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: 10. Também pode acontecer tentar recuperar um valor negativo que aparece o seguinte erro: Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: 10
No entanto, quando se guarda, por exemplo, 4 valores no array e depois se pretende recuperar o oitavo valor não dá erro, devolvendo que o valor guardado nessa posição é 0.


* LOverflow3.py: O programa coloca num array até 10 posições os valores ordenados de forma decrescente. O programa dá erro quando se pretende guardar mais que 10 valores no array, sendo este o tamanho definido do array. O erro é o seguinte: IndexError: list assignment index out of range
No entanto, contrariamente ao Java, quando se pretende recuperar um valor negativo, não dá erro, apenas retorna None.


* LOverflow3.cpp: O programa coloca num array até 10 posições os valores ordenados na forma decrescente.
Se o número de valores a guardar for maior que 10, o programa não pede o valor para recuperar, apenas fica em modo espera porque a memória disponível do array foi ultrapassada. Quando se pretende recuperar valores negativos, este programa retorna 0. E quando se pretende recuperar um valor maior do que o número de valores guardados, o valor é o endereço de memória. Por exemplo:
Quantos valores quer guardar no array? 4
Que valor deseja recuperar? 8
O valor é 45833024



## Pergunta 1.3:
Analise e teste os programs escritos em C RootExploit.c e 0-simple.c .
Indique qual a vulnerabilidade de Buffer Overflow existente e o que tem de fazer (e porquê) para a explorar e (i)
obter a confirmação de que lhe foram atribuídas permissões de root/admin, sem utilizar a password correta, (ii)
obter a mensagem "YOU WIN!!!".

## Resposta 1.3:
No ficheiro RootExploit.c e no 0-simple.c a vulnerabilidade de buffer overflow deve-se pelo facto de a função gets não ter em conta o tamanho do imput.
Mais concretamente no ficheiro RootExploit.c as permissões são dadas quando a password contém pelo menos 5 caracteres, como podemos verificar na imagem seguinte:




![Execução de RootExploit](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula10/img/per1.3.PNG)




Semelhante ao caso anterior, no ficheiro 0-simple.c temos que ter em conta que o tamanho do input tem de ser maior um caracterer que o tamanho do buffer, para podermos verificar a vulnerabilidade e a mensagem pretendida como mostra a imagem seguinte:




![Execução de 0-simple](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula10/img/per1.3.2.PNG)




## Pergunta 1.4:
Analise e teste o programa escrito em C ReadOverflow.c
O que pode concluir?

## Resposta 1.4: 
O programa ReadOverflow é responsável por fazer echo de um determinado número de caracteres previamente definidos pelo utilizador. Esse programa tem uma vulnerabilidade, a de fazer echo do número de caracteres que o utilizador escolheu, deixa-o intruduzir uma string do tamanho que quiser, mesmo que esse tamanho seja menor, sendo possível ler mais informação do que era suposto. Essa vulnerabilidade pode ser visualizada com a ajuda da imagem seguinte.




![Execução ReadOverflow](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula10/img/perg1.4.PNG)




## Pergunta 1.5:

Agora que já tem experiência em efetuar o _overflow_ a um _buffer_ (cf. pergunta P1.3), consegue fazer o mesmo se for necessário um valor exato?

Compile e execute o programa 1-match.c, e obtenha a mensagem de "Congratulations" no ecrã. Notas:
  + já ouviu falar de _little-endian_ e _big-endian_?

Indique os passos que efetuou para explorar esta vulnerabilidade.

## Resposta 1.5:

Para explorarmos vulnerabilidade efetuamos o passo seguinte:
* Para conseguirmos obter a resposta, "you win" temos de alterar o valor da variável control para 0x61626364 de forma a entrar na condição verdadeira do ciclo.
Ora em sistemas operativos UNIX a arquitetura é _little-endian_. Primeiramente constata-se quanto espaço é necessário preencher até ser possível alterar a variável pretendida. Depois transforma-se o valor do endereço de acordo com a tabela ASCII é abcd. Logo insere-se "lixo" como primeiros bytes seguido de "dcba", pois o formato é _little-endian_. Desta forma, consegue-se obter a mensagem pretendida no ecrã.




![Execução do programa](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula10/img/per1.5.PNG)




#### Little Endian e Big endian:
São duas formas distintas de representação de um determinado tipo de dados. O little endian começa por representar primeiro o valor menos significativo até ao mais significativo, enquanto o big endian começa por representar o valor mais significativo até ao valor menos significativo.

## Pergunta 1.6:


Compile e execute o programa 2-functions.c, e obtenha a mensagem de "Congratulations" no ecrã. Notas:
  + relembre que o nome de uma função em C equivale ao endereço onde esta é escrita em memória;
  + poderá fp ser win?

Indique os passos que efetuou para explorar a vulnerabilidade.



## Resposta 1.6: 

Depois de se ter compilado o programa, iniciou-se o programa com o gdb para se ter acesso ao endereço das variáveis e funções. Ao executar o comando *p win* acedeu-se ao endereço da função, que neste caso foi 0x555555554740. Convertendo isto para ASCII, e tendo em conta a arquitetura _little-endian_, fica UUUUG@. Preenchendo ainda os primeiros 72 bytes com informação aleatória, completa-se o resto com a string respetiva do endereço 72 bytes + UUUUG@ .
Assim sendo, fica como input e respetivo input como mostra na seguinte figura, acedendo à função win:

![WIN](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula10/img/per1.6.png)

## Pergunta 1.7:

Compile e execute o programa 3-return.c, e obtenha a mensagem de "Congratulations" no ecrã. Notas:

Indique os passos que efetuou para explorar a vulnerabilidade.


## Resposta 1.7:

Para explorar esta vulnerabilidade começou-se por analisar o código, que é muito parecido ao programa anterior. Ora, neste programa não existe a variável *fp*, logo temos de chamar a função *win* de outra forma. 
Primeiramente, usando o gdb, encontrámos o endereço pretendido. Cria-se um pipe e injeta-se um código Perl para imprimir 72 bytes de informação mais esse mesmo endereço em formato hexadecimal no pipe criado.
![Criação do pipe](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula10/img/pipe.png)

Depois, usamos o pipe para correr o código Perl no gdb para assim aceder à função pretendida, obtendo a mensagem de "Congratulations" no ecrã.

![Acesso à função com êxito](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula10/img/gdb.png)

