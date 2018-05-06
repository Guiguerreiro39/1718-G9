# Aula 11

## Pergunta 1.1
Analise o programa overflow.c.
..1. Qual a vulnerabilidade que existe na função vulneravel() e quais os efeitos da mesma?
..2. Complete o main() de modo	a demonstrar essa vulnerabilidade.
..3. Ao executar dá algum erro? Qual?

## Resposta 1.1
..1. A vulnerabilidade presente na função vulneravel() diz respeito aos argumentos passados, mais especificamente x e y, que dizem respeito ao size_t usado na alocação de memória da matriz. Neste caso, ao atribuir valores absurdamente altos a estes dois inteiros, poderá gerar um overflow em que possivelmente se começaria a escrever e corromper os dados de locais da memória não pré-destinados para esta função.

..2.
```c
int main() {
	char *matriz;
	vulneravel(matriz, 253473829, 13482018273, 39);
}
```
..3. Ao se executar o programa ocorre um *segmentation fault* pois não é possível a alocação de memória pretendida.
