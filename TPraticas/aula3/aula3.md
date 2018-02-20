## TP Aula 3

### Pergunta P2.1

Cada grupo indicado abaixo deve efetuar o teste _SSL Server test_ aos sites indicados (que têm de obrigatoriamente funcionar sobre HTTPS) e responder às respetivas perguntas:

 Grupo 9 - Escolha quatro sites de Bancos a operar na Europa (i.e., sites com domínios europeus, desde que não .pt).

  1. Anexe os resultados do _SSL Server test_ à sua resposta.
  2. Analise o resultado do _SSL Server test_ relativo ao site escolhido com pior rating. Que comentários pode fazer sobre a sua segurança. Porquê?
  3. É natural que tenha reparado na seguinte informação: "_Heartbleed (vulnerability)_" na secção de detalhe do protocolo. O que significa, para efeitos práticos?

### Resposta P2.1
 1.
 Os 4 bancos escolhidos foram:
- Credit Suisse (www.credit-suisse.com)
- ING (www.ing.com)
- HSBC (www.hsbc.co.uk)
- Rabobank (www.rabobank.com)
Na diretoria desta aula, estão anexados os pdfs respetivos resultantes do _SSL Server test_.

 2.
Analisando os resultados, podemos concluir que à exceção do banco HSBC, que teve nota A, todos os outros resultados tiveram nota máxima (A+).
Depois de uma análise mais profunda, e notando que apesar da cotação dos campos de Certificado, Suporte Protocolar, Troca de chaves e Força da cifra terem a mesma pontuação, reparámos que a pontuação relativamente mais fraca se deve a 2 factores. Um deles é o `cipher suite`, pois o servidor não suporta `AEAD`, isto é, encriptação autenticada com informação associada, que de momento é a unica abordagem criptográfica que não apresenta nenhuma fraqueza. Este tipo de encriptação oferece autenticação forte, troca de chaves, forward secrecy e encriptação de pelo menos 128 bits. Se isto se mantiver até Março de 2018 a avaliação do _SSL Server test_ descerá para a nota B. O outro factor é o Certificado que tem no campo Issuer: `Symantec Class 3 EV SSL CA - G3`. Ora isto é problema pois este tipo de certificados vão deixar de ser confiáveis pela Google e pela Mozilla a partir de Setembro de 2018.

 3.
Na campo "_Heartbleed (vulnerability)_" todos os resultados apresentados apresentam um _No_ como resposta. Significa isto que não existe nenhum site que esteja vulnerável ao _Heartbleed_. Se assim não fosse o site correspondente não seria de confiança. O _Heartbleed_ é uma famosa e crítica vulnerabilidade presente na biblioteca de software _OpenSSL_, um bug que afetou várias máquinas há alguns anos atrás, que permite ler a memória de um servidor ou cliente, podendo dessa forma aceder a chaves SSL privadas, roubando dessa forma informação que devia estar protegida.





### Pergunta 3.1:

Cada grupo indicado abaixo deve utilizar o ssh-audit para efetuar teste aos sites indicados, que têm de obrigatoriamente ter o ssh (usualmente, na porta 22) ativo.

**Nota 1:** Para simplificar a resposta a esta pergunta deverá configurar uma conta em <https://www.shodan.io/>, já que após login pode fazer pesquisas fáceis sobre serviços disponíveis na Web. Por exemplo, para pesquisar por servidores ssh em Braga, poderá pesquisar por `port:22 country:pt city:braga`. Se quiser saber os servidores ssh da Universidade do Minho, pode pesquisar por `port:22 org:"Universidade do Minho"`.

**Nota 2:** Para pesquisar as vulnerabilidades de um produto software pode utilizar a pesquisa no site [CVE details](https://www.cvedetails.com/version-search.php), inserindo o nome do produto e a versão a pesquisar.

- Grupo 9 - Escolha dois servidores ssh de empresas comerciais em Londres.


### Resposta 3.1:

Para procurarmos os servidores de empresas comerciais pesquisamos o seguinte `port:22 country:UK city:london` no site <https://www.shodan.io/>

#### Servidor 1: 

* Servidor: ec2-35-177-213-122.eu-west-2.compute.amazonaws.com

* Comando:
> python ssh-audit.py ec2-35-177-213-122.eu-west-2.compute.amazonaws.com

* Resultados ssh-audit:
1. [Resultados Parte 1](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula3/img/serv1_1.png)
2. [Resultados Parte 2](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula3/img/serv1_2.png)
3. [Resultados Parte 3](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula3/img/serv1_3.png)

* Software Servidor SSH: OpenSSH 7.2p2

* Versão do Software do Servidor SSH: 7.2p2

* Vulnerabilidade mais alta: 7.8

* Número de vulnerabilidades: 9


![img1](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula3/img/nvul1.png)


#### Servidor 2:

* Servidor: ec2-35-176-57-157.eu-west-2.compute.amazonaws.com

* Comando:
> python ssh-audit.py ec2-35-176-57-157.eu-west-2.compute.amazonaws.com

* Resultados ssh-audit:
1. [Resultados Parte 1](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula3/img/ser2_1.png)
2. [Resultados Parte 2](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula3/img/ser2_2.png)
3. [Resultados Parte 3](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula3/img/ser2_3.png)
4. [Resultados Parte 4](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula3/img/ser2_4.png)

* Software Servidor SSH: OpenSSH 7.4

* Versão do Software do Servidor SSH: 7.4

* Vulnerabilidade mais alta: 5.0

* Número de vulnerabilidades: 2


![img2](https://github.com/uminho-miei-engseg/1718-G9/blob/master/TPraticas/aula3/img/nvul2.png)


#### Qual é a versão de software com mais vulnerabilidades?
A versão do software que possui um maior número de vulnerabilidades é a versão 7.2 pois esta possui 9 enquanto que a versão 7.4 possui 2 vulnerabilidades.


#### Qual dessas versões tem a vulnerabilidade mais grave?
A versão que possui a vulnerabilidade mais grave é a versão 7.2, tendo um rating de 7.8.

#### A vulnerabilidade indicada no ponto anterior é grave? Porque?
Sim, porque a função auth_password em auth-passord.c no SSHD no OpenSSH antes de 7.3 não limita os comprimentos da senha para a autenticação de senha, o que permite aos invasores remotos causarem uma negação de serviço(crypt CPU consumption) usando para isso uma string longa.



