## TP Aula 3

### Pergunta P1.1

Pretende-se que altere o código fornecido para a experiência 1.2, de forma a simplificar o input e output.

### Resposta P1.1

Os componentes necessários para a realização da assinatura cega foram guardados nas pastas **Signer** e **Req**, assinante e requerente respetivamente. As pastas são criadas automáticamente na execução.

## Assinante

- `init-app.py`: Inicialmente é necessário executar o código `python init-app.py -init` para criar as componentes iniciais _pRDashComponents_ e _initComponents_ como também a pasta **Signer** onde se irá guardar todos os ficheiros relativos ao assinante. Poderá ainda executar o ficheiro sem a flag **-init** para imprimir o **R'**, ou seja, o **pRDashComponents**. De realçar que é necessário inicializar as componentes antes de poder imprimir o **R'**.

```python
(...)

def parseArgs():
    if (len(sys.argv) == 1):
        main()
    elif (len(sys.argv) == 2 and sys.argv[1] == "-init"):
        init()
    else:
        printUsage()

def main():
    # Verifica se a pasta existe
    if not os.path.exists("Signer/pRDashComponents"):
        print("Components not initialized yet. Use: python init-app.py -init")
    else:
        # Abre o ficheiro com o pRDashComponents
        with open("Signer/pRDashComponents", "r") as pR:
            print("Output")
            print("pRDashComponents: %s" % pR.read())

def init():
    initComponents, pRDashComponents = eccblind.initSigner()
    # Verifica se a pasta existe
    if not os.path.exists("Signer"):
        os.makedirs("Signer")
    # Guardar em ficheiro os components
    with open("Signer/initComponents", "w") as comp:
        comp.write(initComponents)
    with open("Signer/pRDashComponents", "w") as pR:
        pR.write(pRDashComponents)

(...)
```

- `blindSignature-app.py`: Neste ficheiro o assinante assina a _BlindMessage_ com a sua _privateKey_ devolvendo e guardando na sua pasta a _BlindSignature_ correspondente. Leva como parâmetros a _PrivateKey_ e a _BlindMessage_.

```python
(...)

def parseArgs():
    if (len(sys.argv) == 5 and sys.argv[1] == "-key" and sys.argv[3] == "-bmsg"):
        eccPrivateKeyPath = sys.argv[2]
        with open(sys.argv[4], "r") as bm:
            blindM = bm.read()
        main(eccPrivateKeyPath, blindM)
    else:
        printUsage()

def showResults(errorCode, blindSignature):
    print("Output")
    if (errorCode is None):
        with open("Signer/BlindSignature", "w") as blindS:
            blindS.write(blindSignature)
        print("Blind signature: %s" % blindSignature)
    elif (errorCode == 1):
        print("Error: it was not possible to retrieve the private key")
    elif (errorCode == 2):
        print("Error: init components are invalid")
    elif (errorCode == 3):
        print("Error: invalid blind message format")

def main(eccPrivateKeyPath, blindM):
    pemKey = utils.readFile(eccPrivateKeyPath)
    print("Input")
    passphrase = raw_input("Passphrase: ")
    with open("Signer/initComponents", "r") as initcomp:
        initComponents = initcomp.read()
    errorCode, blindSignature = eccblind.generateBlindSignature(pemKey, passphrase, blindM, initComponents)
    showResults(errorCode, blindSignature)

(...)
```

## Remetente

- `ofusca-app.py`: O objetivo deste ficheiro é de "ofuscar", ou seja, ocultar uma mensagem para depois ser enviada para o assinante sem esse saber o seu conteúdo. Aqui é também criada a pasta **Req** onde se irá guardar os ficheiros relativos ao requerente. Devolve a _BlindMessage_ e leva como parâmetros a mensagem a assinar e o _pRDashComponents_ anteriormente gerados pelo assinante.

```python
(...)

def parseArgs():
    if (len(sys.argv) == 5 and sys.argv[1] == "-msg" and sys.argv[3] == "-RDash"):
        with open(sys.argv[2], "r") as msg:
            data = msg.read()
        with open(sys.argv[4], "r") as pRd:
            pRDashComponents = pRd.read()
        main(data, pRDashComponents)
    else:
        printUsage()

def showResults(errorCode, result):
    print("Output")
    if (errorCode is None):
        blindComponents, pRComponents, blindM = result
        # Verifica se a pasta existe
        if not os.path.exists("Req"):
            os.makedirs("Req")
        # Guarda nos ficheiros
        with open("Req/blindM", "w") as bm:
            bm.write(blindM)
        with open("Req/blindComponents", "w") as blindcomp:
            blindcomp.write(blindComponents)
        with open("Req/pRComponents", "w") as pRcomp:
            pRcomp.write(pRComponents)
        print("Blind Message: %s" % blindM)
    elif (errorCode == 1):
        print("Error: pRDash components are invalid")

def main(data, pRDashComponents):
    errorCode, result = eccblind.blindData(pRDashComponents, data)
    showResults(errorCode, result)
    
(...)
```

- `desofusca-app.py`: Depois da assinatura da _BlindMessage_ ser realizada pelo assinante, este ficheiro irá "desofuscar", ou seja, decifrar a _BlindSignature_ de forma a obter a _Signature_ da mensagem original. Devolve a _Signature_ e necessita como parâmetros a _BlindSignature_ e o _pRDashComponents.

```python
(...)

def parseArgs():
    if (len(sys.argv) == 5 and sys.argv[1] == "-s" and sys.argv[3] == "-RDash"):
        with open(sys.argv[2], "r") as blindS:
            blindSignature = blindS.read()
        with open(sys.argv[4], "r") as pRd:
            pRDashComponents = pRd.read()
        main(blindSignature, pRDashComponents)
    else:
        printUsage()


def showResults(errorCode, signature):
    print("Output")
    if (errorCode is None):
        with open("Req/Signature", "w") as sig:
            sig.write(signature)
        print("Signature: %s" % signature)
    elif (errorCode == 1):
        print("Error: pRDash components are invalid")
    elif (errorCode == 2):
        print("Error: blind components are invalid")
    elif (errorCode == 3):
        print("Error: invalid blind signature format")

def main(blindSignature, pRDashComponents):
    with open("Req/blindComponents", "r") as blindC:
        blindComponents = blindC.read()
    errorCode, signature = eccblind.unblindSignature(blindSignature, pRDashComponents, blindComponents)
    showResults(errorCode, signature)
    
(...)
```

## Assinante

- `verify-app.py`: Depois da obtenção da _Signature_, este ficheiro permite verificar essa mesma com o certificado gerado juntamente com a _PrivateKey_ do assinante bem como o resto dos componentes do requerente. Devolve uma mensagem de aprovação ou negação (dependendo do resultado da verificação) e leva como parâmetros o _Certificate_, a mensagem original (um ficheiro com uma mensagem escrita), a _Signature_ e a pasta criada para o requerente (a pasta é criada na pasta em que executar o código `python ofusca-app.py -msg <mensagem a assinar> -RDash <pRDashComponents>` com o nome **Req**).

```python
(...)

def parseArgs():
    if (len(sys.argv) == 9 and sys.argv[1] == "-cert" and sys.argv[3] == "-msg"):
        # Para a linha de cima não ficar demasiado grande
        if(sys.argv[5] == "-sDash" and sys.argv[7] == "-f"):
            eccPublicKeyPath = sys.argv[2]
            with open(sys.argv[4], "r") as msg:
                data = msg.read()
            with open(sys.argv[6], "r") as sig:
                signature = sig.read()
            for filename in os.listdir(sys.argv[8]):
                if (filename == "pRComponents"):
                    with open(sys.argv[8] + "/" + filename, "r") as pRc:
                        pRComponents = pRc.read()
                elif (filename == "blindComponents"):
                    with open(sys.argv[8] + "/" + filename, "r") as blindC:
                        blindComponents = blindC.read()
            main(eccPublicKeyPath, data, signature, blindComponents, pRComponents)
    else:
        printUsage()

def showResults(errorCode, validSignature):
    print("Output")
    if (errorCode is None):
        if (validSignature):
            print("Valid signature")
        else:
            print("Invalid signature")
    elif (errorCode == 1):
        print("Error: it was not possible to retrieve the public key")
    elif (errorCode == 2):
        print("Error: pR components are invalid")
    elif (errorCode == 3):
        print("Error: blind components are invalid")
    elif (errorCode == 4):
        print("Error: invalid signature format")

def main(eccPublicKeyPath, data, signature, blindComponents, pRComponents):
    pemPublicKey = utils.readFile(eccPublicKeyPath)
    errorCode, validSignature = eccblind.verifySignature(pemPublicKey, signature, blindComponents, pRComponents, data)
    showResults(errorCode, validSignature)

(...)
```

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
No campo "_Heartbleed (vulnerability)_" todos os resultados apresentados apresentam um _No_ como resposta. Significa isto que não existe nenhum site que esteja vulnerável ao _Heartbleed_. Se assim não fosse o site correspondente não seria de confiança. O _Heartbleed_ é uma famosa e crítica vulnerabilidade presente na biblioteca de software _OpenSSL_, um bug que afetou várias máquinas há alguns anos atrás, que permite ler a memória de um servidor ou cliente, podendo dessa forma aceder a chaves SSL privadas, roubando dessa forma informação que devia estar protegida.





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



