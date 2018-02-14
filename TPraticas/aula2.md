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
