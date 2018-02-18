#### Pergunta P1.1

Teste os seguintes comandos, que vão obter 1024 bytes pseudoaleatórios do sistema e os apresentam em base64:

- `head -c 1024 /dev/random | openssl enc -base64`
- `head -c 1024 /dev/urandom | openssl enc -base64`

Que conclusões pode tirar? Em que se baseia para essas conclusões ?

#### Resposta P1.1

Depois de se ter executado várias vezes ambos os comandos, verifica-se que por vezes o `/dev/random` não retorna nada. Depois de alguma pesquisa, averiguámos que isto se verifica devido ao facto que esse comando bloqueia quando esgota a entropia disponível, isto é, pode não haver informação aleatória disponível para ser fornecida ao utilizador, ficando bloqueado até recolher o ruído atmosférico necessário. Já o comando `/dev/urandom` não bloqueia. No entanto, pode ser vulnerável a um ataque criptográfico se não houver entropia suficiente. Em forma de conclusão se precisarmos de informação aleatório no momento de forma rápida usa-se o `/dev/urandom`. Se precisarmos de informação realmente segura mas não nos importámos de porventura esperar, usa-se o `/dev/random`.

#### Pergunta P1.2

O haveged - <http://www.issihosts.com/haveged/index.html> - é um daemon de entropia adaptado do algoritmo HAVEGE (_HArdware Volatile Entropy Gathering and Expansion_) - <http://www.irisa.fr/caps/projects/hipsor/> -.

Instale a package haveged na máquina virtual com o seguinte comando: `sudo apt-get install haveged`.

Teste novamente os seguintes comandos, que vão obter 1024 bytes pseudoaleatórios do sistema e os apresentam em base64:

- `head -c 1024 /dev/random | openssl enc -base64`
- `head -c 1024 /dev/urandom | openssl enc -base64`

Que conclusões pode tirar? Em que se baseia para essas conclusões?

#### Resposta P1.2

Depois de instalar o package indicado, verifica-se que de facto não encontrámos agora nenhum problema quando ao comando `/dev/random`, já que o propósito do package é mesmo esse, corrigir as condições em que a entropia não está disponível que acontece em algumas situações.

#### Pergunta P1.3

Na diretoria das aulas (Aula2/PseudoAleatorio) encontra o ficheiro *generateSecret-app.py* baseado no módulo eVotUM.Cripto (https://gitlab.com/eVotUM/Cripto-py), já instalado na máquina virtual em /home/user/API/Cripto-py/eVotUM/Cripto.

Analise e execute esse programa de geração de segredo aleatório e indique o motivo do output apenas conter letras e dígitos (não contendo por exemplo caracteres de pontuação ou outros).

#### Resposta P1.3

Depois de analisar o código do programa *generateSecret-app.py*, reparámos que chama a função `generateSecret` do programa *shamirsecret.py*. Analisando então o código da função desse programa, constatámos que dentro do ciclo while aparece o seguinte código:
```python
s = utils.generateRandomData(secretLength - l)
        for c in s:
            if (c in (string.ascii_letters + string.digits) and l < secretLength): # printable character
                l += 1
                secret += c
```
É gerado uma string com um comprimento dado no input da função, e verifica-se se cada carater dessa string faz parte das letras ascii ou é um número. Se assim se tratar, significa que pode ser adicionado à string de retorno, justificando assim o facto do output apenas ser constituído por letras ou números.


#### Pergunta P2.1

Na diretoria das aulas (Aula2/ShamirSharing) encontra os ficheiros *createSharedSecret-app.py*, *recoverSecretFromComponents-app.py* e *recoverSecretFromAllComponents-app.py* baseado no módulo eVotUM.Cripto (https://gitlab.com/eVotUM/Cripto-py), já instalado na máquina virtual em /home/user/API/Cripto-py/eVotUM/Cripto.

A. Analise e execute esses programas, indicando o que teve que efectuar para dividir o segredo "Agora temos um segredo muito confidencial" em 7 partes, com quorom de 3 para reconstruir o segredo.

Note que a utilização deste programa é ``python createSharedSecret-app.py number_of_shares quorum uid private-key.pem`` em que:
+ number_of_shares - partes em que quer dividir o segredo
+ quorum - número de partes necessárias para reconstruir o segredo
+ uid - identificador do segredo (de modo a garantir que quando reconstruir o segredo, está a fornecer as partes do mesmo segredo)
+ private-key.pem - chave privada, já que cada parte do segredo é devolvida num objeto JWT assinado, em base 64

B. Indique também qual a diferença entre recoverSecretFromComponents-app.py e recoverSecretFromAllComponents-app.py, e em que situações poderá ser necessário utilizar recoverSecretFromAllComponents-app.py em vez de recoverSecretFromComponents-app.py.

#### Reposta P2.1 A

Em primeiro lugar foi necessário criar o par de chaves que pode ser efetuado com o comando `openssl genrsa -aes128 -out mykey.pem 1024`. Com isto, foi adicionado o ficheiro *mykey.pem* à diretoria correspondente. De seguida efetua-se o comando ``python createSharedSecret-app.py 7 3 1 mykey.pem``, onde foi introduzido a mesmo passphrase que na geração da chave privada, assim como o segredo "Agora temos um segredo muito confidencial". 
Para verificar se as 3 partes são necessárias para reconstruir o segredo, primeiramente cria-se o certificado associado à chave privada com o comando `openssl req -key mykey.pem -new -x509 -days 365 -out mykey.crt`, completando com toda a informação referente ao certificado que é pedida. Confirma-se que foi criado o ficheiro *mykey.crt*, referente ao certificado.
O próximo passo é obter o segredo a partir das componentes com o comando `python recoverSecretFromComponents-app.py 3 1 mykey.crt`. Depois de introduzir as 3 componentes necessárias, chegamos à recuperação do segredo pretendido.

#### Reposta P2.1 B

A principal diferença encontrada entre os dois programas encontra-se no número de componentes necessários para reconstruir o segredo.
Enquanto que no programa *recoverSecretFromAllComponents-app.py* o número de componentes é igual ao número de partes que foi dividido o segredo inicialmente, não é verdade para o programa *recoverSecretFromComponents-app.py*, onde existem um quorum, um número de partes necessárias para reconstruir o segredo, que pode ser diferente do número de partes da divisão inicial do segredo.
Para o *AllComponents* recomenda-se a sua utilização quando é necessário a validação de todos os envolvidos. Já para o outro, pode haver, por exemplo, horários definidos em que o quorum é o número de pessoas disponíveis no momento da recuperação do segredo.


#### Pergunta P3.1
Baseado no cenário identificado, como sugeriria à sua empresa que cifrasse e decifrasse o(s) segredo(s), de modo a garantir confidencialidade, integridade e autenticidade do segredo e da sua etiqueta? Inclua, na sua resposta, o algoritmo, que utilizando a API, pediria à área de desenvolvimento para implementar, de modo a cifrar e decifrar o segredo.



* Encoding:
```
chave é do tipo = dia.mes.ano
def cifrar(mensagem):
        segredo = encoding(mensagem,chave)
        autenticacao = hmac(HMAC_SHA256_key,segredo)
        cyphertext = segredo + autenticacao
        return cyphertext
```
P.S: temos de ter em consideração que a chave já foi previamente acordada entre as duas entidades.

* Decoding:
O cyphertext tem de ser separado em dois pois precisamos de verificar através do Hmac se a autenticação é válida, se o resultado for positivo aí passamos à decifragem da mensagem enviada pela outra entidade.
```
def decifrar(cypertext):
        autenticacao , segredo = separate(cyphertext) 
        if (hmac(HMAC_SHA_256, segredo) == autenticacao)
                decoding(segredo,chave)
        else
                print("Erro no processo de decifragem/cifragem da msg")
```

