### Pergunta P1.1

Para aceder a alguns sites nos EUA tem que estar localizado nos EUA.

1. Efetuando o comando `sudo anonsurf start` consegue garantir que está localizado nos EUA?
2. Porquê? Utilize características do protocolo TOR para justificar.

### Resposta P1.1


#### 1 
Não, devido ao processo de aleatorização na seleção dos OR's que o TOR fornece. Pois, nada nos garante que o último OR esteja localizado nos EUA.

Mas podemos obter um IP nos EUA se executarmos o comando ` sudo anonsurf change`  várias vezes e formos verificar ao site `  http://myiplocator.net/ `. Como não sabemos qual a sequência dos OR's nem o OR final da futura execução não podemos garantir que na próxima execução estamos localizados nos EUA.




#### 2
Não conseguimos garantir que estamos localizados nos EUA, pois o TOR garante-nos anonimato ponto a ponto, ou seja não sabemos qual é a sequência dos OR nem qual é o OR final. Essas sequências de três OR's são realizadas pelos OP, que é um servidor local para cada utilizador. Devido ao facto que os OR's escolhidos são alterados periodicamente podemos ter a probabilidade de estarmos localizados nos EUA, mas é um processo em que não conseguimos garantir que em uma dada execução vamos estar nos EUA.



### Pergunta P1.2
No seguimento da experiência anterior, aceda a <http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page> ou <https://www.facebookcorewwwi.onion/>.

1. Clique no símbolo do Onion (cebola) do lado esquerdo da barra de URL e verifique qual é o circuito para esse site.

2. Porque existem 6 "saltos" até ao site Onion, sendo que 3 deles são "_relay_"? Utilize características do protocolo TOR para justificar.



### Resposta P1.2


#### 1

[Circuito para http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page ](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula4/onion)
[Circuito para https://www.facebookcorewwwi.onion/ ](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula4/fb)

#### 2

Para acedermos ao circuito, o utilizador começa por aceder ao DS (Directory Server) para obter informação sobre os IP (Introduction Points). Depois de os IP's estarem escolhidos vai ser criado um circuito TOR até um RP (Reduz Point) para ser conectado com o serviço anónimo. Cada ligação entre um servidor e um IP compreende 3 ORs intermédios (ex. no caso de zqktlwi4fecvo6ri.onion temos Germany: 144.76.253.229 -> United States: 192.81.132.46 -> Netherlands: 195.169.125.226). No caso de um utilizador querer aceder a um domínio .onion, antes vai aceder ao DS (Diretory Server) obtendo assim as informações sobre os IP's na qual o servidor se vai conectar. 


