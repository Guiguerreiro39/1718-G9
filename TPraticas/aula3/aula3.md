#### Pergunta P2.1

Cada grupo indicado abaixo deve efetuar o teste _SSL Server test_ aos sites indicados (que têm de obrigatoriamente funcionar sobre HTTPS) e responder às respetivas perguntas:

 Grupo 9 - Escolha quatro sites de Bancos a operar na Europa (i.e., sites com domínios europeus, desde que não .pt).

  1. Anexe os resultados do _SSL Server test_ à sua resposta.
  2. Analise o resultado do _SSL Server test_ relativo ao site escolhido com pior rating. Que comentários pode fazer sobre a sua segurança. Porquê?
  3. É natural que tenha reparado na seguinte informação: "_Heartbleed (vulnerability)_" na secção de detalhe do protocolo. O que significa, para efeitos práticos?

#### Resposta P2.1
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