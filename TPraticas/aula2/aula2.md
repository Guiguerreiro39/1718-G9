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

#### Pergunta 4.1

Cada grupo indicado abaixo deve identificar os algoritmos e tamanhos de chave utilizados nos certificados das Entidades de Certificação (EC) que emitem certificados digitais qualificados, e verificar se são os mais adequados (e se não forem, propor os que considerar mais adequados):
Eslovénia, para as ECs "Ministry of Defence of Slovenia", "Republika Slovenija", "HALCOM D.D.";

#### Resposta 4.1

### Ministry of Defence of Slovenia

* Algoritmos: Signature Algorithm: sha256WithRSAEncryption, Public Key Algorithm: rsaEncryption
* Tamanho de Chave: 2048 bits
* Certificado: SIMoD-CA-Restricted
** Nº do certificado: 1203932140
** Validade: 2014-02-07 09:47:31 - 2020-02-07 10:17:31
* Verificação do Certificado: O certificado usado neste algoritmo atualmente é considerado como seguro.
* Base 64-encoded:
> -----BEGIN CERTIFICATE-----
MIIFozCCA4ugAwIBAgIER8KL7DANBgkqhkiG9w0BAQsFADBIMQswCQYDVQQGEwJzaTENMAsGA1UECgwEbW9yczESMBAGA1UECwwJc2ltb2QtcGtpMRYwFAYDVQQDDA1zaW1vZC1jYS1yb290MB4XDTE0MDIwNzA5NDczMVoXDTIwMDIwNzEwMTczMVowTjELMAkGA1UEBhMCc2kxDTALBgNVBAoMBG1vcnMxEjAQBgNVBAsMCXNpbW9kLXBraTEcMBoGA1UEAwwTc2ltb2QtY2EtcmVzdHJpY3RlZDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAL3Gt3hoCzvEMyViv+qewWdXVv5xrN5Jo3NdPmoM/7RHoAp39qN9FfOmK1s60bAXiSp8hzV5H2MVQ8KlpTdQUGCKUqewda31kgREi7n1w96TBPTJhvBoZiTgKXXhkSmLxprjoe8Q0vlT+v5FsKHcW4KI/+rO42X647SX6dczxi/zXn9FOEpyKWoXh95wH9LEVHQk5EcSNNyNA0NCNhMJBnl6xS5rX3sK4DKwCueHchyoY8g9CnVGqGzQIfz0Rq+j8XZV6Yhh9Zxr+U7wqlZljx5QbrFP7mQwL9pvqrVXbYYB9yEVYV6jEuMaHA/tMfgl1zN8/34Cs+UhTx+iq1LKTycCAwEAAaOCAY0wggGJMA8GA1UdEwEB/wQFMAMBAf8wDgYDVR0PAQH/BAQDAgEGMIIBIQYDVR0fBIIBGDCCARQwX6BdoFukWTBXMQswCQYDVQQGEwJzaTENMAsGA1UECgwEbW9yczESMBAGA1UECwwJc2ltb2QtcGtpMRYwFAYDVQQDDA1zaW1vZC1jYS1yb290MQ0wCwYDVQQDDARDUkwxMIGwoIGtoIGqhnNsZGFwOi8vaW1lbmlrLnNpbW9kLXBraS5tb3JzLnNpL2NuPVdpbkNvbWJpbmVkMSxjbj1zaW1vZC1jYS1yb290LG91PXNpbW9kLXBraSxvPW1vcnMsYz1zaT9jZXJ0aWZpY2F0ZVJldm9jYXRpb25MaXN0hjNodHRwOi8vd3d3LnNpbW9kLXBraS5tb3JzLnNpL2NybC9zaW1vZC1jYS1yb290MS5jcmwwEwYDVR0jBAwwCoAIRmxV0DffKvowEQYDVR0OBAoECEx9VQjnv0B+MBkGCSqGSIb2fQdBAAQMMAobBFY3LjEDAgCBMA0GCSqGSIb3DQEBCwUAA4ICAQA25n2eSPIP9KQBUKuW42fnox0ncpdUB/koN9JR8lF2XG1Hb1lAhhwYTll8Jy6kdKUM1lwBBsjbo6DYpXphB8TGaXoDnigQqLX/un26TX8m3aW4nXRXMaKLfKfsoSxtJoOZGQLodDwVgsa6NcR9aW/SqtbFemtuvtuNqqFuqAbvRjt0NY8417a246dgOb4MF+kw6J+eWFVj8QwnH3EYlF0oQawLaYGFsouSEsxQLsGUv8Rto/+ADipbO/wm1RjmyWD+vkvw2dAje8Ic6Glk2wJeE1PdZOV+NDY9ILIw4RKD8JbnKDRq07PAnFfGpCF4xmBzBmTQpfpsTxCSiN2qklvZ+j9NWS8F13+OhB4sOeJ9vjZK5zM2qLm2jmV/aQhts/4i6y/7ZmMYTEyVpjXKG9EVL4BsLsqZZBgDihbF9ScO1sXuTcshjtdYpcYHtMWPuQHKomO2MkoQp6GfAvdVKZdKGn6Xsx+UhbyxHxyz2TOEP2DTotUlH9TIDAFy6Iu2v1Kuc+dRF48m/q5AzEtSJMrfc7GnYhC7K6GLkURVDlGeYr7jHeH90OgfCNfSYTdnCS/hc4+I43y8R9H356IM5DdA0WJUCH7SMxLCZDPOviy3j8ii/nELG6hYJ77kGa07MSO72rKbOfc9MiVNPVrj5anrGblBFg1Rqfvf4tMEVmoE4g==
-----END CERTIFICATE-----




### Republika Slovenija

* Algortimo: Signature Algorithm: sha256WithRSAEncryption , Public Key Algorithm: rsaEncryption
* Tamanho de Chave: 3072 bits
* Certificado: SIGOV-CA
** Nº do certificado: 49792534925696038464206524649
** Validade: 2016-05-24 13:03:18 - 2035-12-22 23:00:00
* Verificação do Certificado: O certificado usado neste algoritmo atualmente é considerado como seguro.
* Base 64-encoded:
> -----BEGIN CERTIFICATE-----
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
-----END CERTIFICATE-----




### HALCOM D.D

* Algortimo: Signature Algorithm: sha256WithRSAEncryption, Public Key Algorithm: rsaEncryption
* Tamanho de Chave: 2048 bits
* Certificado: Halcom CA web 1
** Nº do certificado: 921298
** Validade: 22017-04-22 09:00:00 - 2027-04-22 09:00:00
* Verificação do Certificado: O certificado usado neste algoritmo atualmente é considerado como seguro.
* Base 64-encoded:
> -----BEGIN CERTIFICATE-----
MIIEqjCCA5KgAwIBAgIDDg7SMA0GCSqGSIb3DQEBCwUAMGgxCzAJBgNVBAYTAlNJMRQwEgYDVQQKEwtIYWxjb20gZC5kLjEXMBUGA1UEYRMOVkFUU0ktNDMzNTMxMjYxKjAoBgNVBAMTIUhhbGNvbSBSb290IENlcnRpZmljYXRlIEF1dGhvcml0eTAeFw0xNzA0MjIwODAwMDBaFw0yNzA0MjIwODAwMDBaMFYxCzAJBgNVBAYTAlNJMRQwEgYDVQQKEwtIYWxjb20gZC5kLjEXMBUGA1UEYRMOVkFUU0ktNDMzNTMxMjYxGDAWBgNVBAMTD0hhbGNvbSBDQSB3ZWIgMTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAKO7rRFpGNkqYjND9aJn2dNB6eCcjhmjWL9lHXXijLdGdeJpNgc5DYLBwRi8PEfqq6Jt75efp5P5TPEciYrawPOmnwg05xhoMQUZsEJYD0sNaGTQjUaGn1d8aptn5m/oqFXtiaed4X/xDVXp7YBq4jkaDwuuQlRw/2RpILiaOHwh5hw2xQXF91zRNsIkdM/+O7evj5d/Qr02xYCl38GFjKNEyvNA6jD/040v0pucSj9lOyzrmAo4FsWFupyKkA///lC4HkfSn8KNRtaJX3gJ3PeNRsReuvcVl5HM1EE02oqLk5SnTJT3hB8sN9Y6gWfFKNe03oJbceJlm7iiosmQC2ECAwEAAaOCAW0wggFpMA8GA1UdEwEB/wQFMAMBAf8wEQYDVR0OBAoECEhCCxftrp5wMBMGA1UdIwQMMAqACEKupkPHmCiwMAsGA1UdDwQEAwIBBjCByQYDVR0fBIHBMIG+MIG7oIG4oIG1hm9sZGFwOi8vbGRhcC5oYWxjb20uc2kvY249SGFsY29tJTIwUm9vdCUyMENlcnRpZmljYXRlJTIwQXV0aG9yaXR5LG89SGFsY29tLGM9U0k/Y2VydGlmaWNhdGVyZXZvY2F0aW9ubGlzdDtiaW5hcnmGQmh0dHA6Ly9kb21pbmEuaGFsY29tLnNpL2NybHMvaGFsY29tX3Jvb3RfY2VydGlmaWNhdGVfYXV0aG9yaXR5LmNybDBVBgNVHSAETjBMMEoGBFUdIAAwQjBABggrBgEFBQcCARY0aHR0cDovL3d3dy5oYWxjb20uc2kvdXBsb2Fkcy9maWxlcy9DUFNfaGFsY29tX2NhLnBkZjANBgkqhkiG9w0BAQsFAAOCAQEAwXfgRyAaNZwQMP0FboHiiwiWIQfNWkNZieW+OPymM19X6LE7NAExx1KL3fSHhlJsv+NIl0NfkAGSkJzGDH8G0RK7yHhKl4GvkzqijZP2J/V5kbkFffBM+67LHvFnyCwUKEzi8h34YLReOomMs0EAHzchyvRFcT3p30lswQdveUvmYPptGFIhSQEnVbIUOurdMazWTVCImSWbx7jrwN2dl6IFmt9SLLSv/mqKUW0X4fe3tSvVznMlWifcfYS96lWe5xIoT6V+YTFtxJHOMVQqSqwYUGTY4ZFvv6yP5Glgw9v2w8w+XA8F59Fo0R/XMaaKhmrYX/HMrgPXVwgpcMYNRQ==
-----END CERTIFICATE-----
