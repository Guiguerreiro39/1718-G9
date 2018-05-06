# Aula 11

## Pergunta 1.1
Analise o programa overflow.c.
  1. Qual a vulnerabilidade que existe na função vulneravel() e quais os efeitos da mesma?
  2. Complete o main() de modo	a demonstrar essa vulnerabilidade.
  3. Ao executar dá algum erro? Qual?

## Resposta 1.1
  1. A vulnerabilidade presente na função vulneravel() diz respeito aos argumentos passados, mais especificamente `x e y`, que dizem respeito ao tamanho usado na alocação de memória da matriz. Neste caso, ao atribuir valores absurdamente altos a estes dois inteiros, poderá-se exceder o limite superior do tipo *size_t* pelo que o número iria ser convertido para um menor. Devido a este risco, possivelmente se começaria a escrever e corromper os dados de locais da memória não pré-destinados para esta função.

```c
int main() {
	char *matriz;
	vulneravel(matriz, 253473829, 13482018273, 39);
}
```

  3. Ao se executar o programa ocorre um *segmentation fault* pois não é possível a alocação de memória pretendida pelo simples facto de o número convertido ser inferior ao que se realmente se pretende como tamanho, o que irá fazer com que se tente alterar pedaços de memórias não alocada.

## Pergunta 1.2
Analise o programa underflow.c.
  1. Qual a vulnerabilidade que existe na função vulneravel() e quais os efeitos da mesma?
  2. Complete o main() de modo a demonstrar essa vulnerabilidade.
  3. Ao executar dá algum erro? Qual?
  
## Respota 1.2
  1. Existem também vulnerabilidades devido à atribuição de valores demasiado baixos nos argumentos passados ao alocar a memória. Apesar de haver a verificação para valores acima de `MAX_SIZE`, não existe essa mesma confirmação para um limite inferior. Ao passar o valor 0 ao argumento `tamanho`, a variável `tamanho_real` será -1 pelo que, como não é possível um inteiro *size_t* ser negativo, esse valor irá ser convertido para um valor extremamente alto que irá ultrapassar o limite estabelecido em `MAX_SIZE`.
  
```c
int main() {
	char *origem;
	vulneravel(origem, 0);
}
```

  3. Ao executar o programa irá ocorrer um *segmentation fault* devido à mesma situação incorrida na pergunta 1.1.
  
## Pergunta 1.3
Analise o programa erro_sinal.c.
  1. Qual a vulnerabilidade que existe na função vulneravel() e quais os efeitos da mesma?
  2. Complete o main() de modo a demonstrar essa vulnerabilidade.
  3. Ao executar dá algum erro? Qual?
  
## Resposta 1.3
  1. Ao analisar detalhadamente o código, é possível reparar que neste caso, apesar de se ter estabelecido um limite inferior, o tipo da variável `tamanho_real` foi alterado de *size_t* para *int*. Enquanto que os inteiros de tipo *size_t* não podem ser números negativos, os de tipo *int* podem. Por causa deste factor, o limite superior abrangido por inteiros do tipo *size_t* é maior do que os de tipo *int* (2x). Por esse motivo, ao atribuirmos um número suficientemente grande para ultrapassar esse valor limite e o tentarmos atribuir ao inteiro de tipo *int*, este vai converter esse valor para um valor negativo. Seguindo por passos no código fornecido, apesar do valor final da variável *tamanho_real* ser negativo, foi possível ultrapassar todas as barreiras de verificações implementadas no código e irá-se usar como tamanho da alocação de memória um valor negativo que posteriormente irá ser convertido num número diferente ao do tamanho pretendido para a memória.

```c
int main() {
	char *origem;
	// limite superior de int é 2147483647
	vulneravel(origem, 2147483649);
}
```

  3. Tal como os programas anteriores, estes também irá dar *segmentation fault* devido ao facto de se pretender aceder a memória que não foi alocada.

   
  

