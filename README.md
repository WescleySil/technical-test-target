# technical-test-target
```bash
1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
 (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
 escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e
 retorne uma mensagem avisando se o número informado pertence ou não a sequência.
````
Codigo: [question1.py](https://github.com/WescleySil/technical-test-target/blob/main/question1.py)

---

```bash
2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’,
seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
```
Codigo: [question2.py](https://github.com/WescleySil/technical-test-target/blob/main/question2.py)

---

```bash
3) Observe o trecho de código abaixo:
int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA?

Vamos acompanhar o que acontece em cada iteração:

Iteração 1: K = 2, SOMA = 0 + 2 = 2
Iteração 2: K = 3, SOMA = 2 + 3 = 5
Iteração 3: K = 4, SOMA = 5 + 4 = 9
Iteração 4: K = 5, SOMA = 9 + 5 = 14
Iteração 5: K = 6, SOMA = 14 + 6 = 20
Iteração 6: K = 7, SOMA = 20 + 7 = 27
Iteração 7: K = 8, SOMA = 27 + 8 = 35
Iteração 8: K = 9, SOMA = 35 + 9 = 44
Iteração 9: K = 10, SOMA = 44 + 10 = 54
Iteração 10: K = 11, SOMA = 54 + 11 = 65

Após essa última iteração, K se torna 12
, e o laço termina porque a condição K < INDICE (ou seja, 12 < 12) não é mais verdadeira.

Valor final de SOMA:
Portanto, ao final do processamento, o valor da variável SOMA será 65.
```

---

```bash
4) Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, ___
b) 2, 4, 8, 16, 32, 64, ____
c) 0, 1, 4, 9, 16, 25, 36, ____
d) 4, 16, 36, 64, ____
e) 1, 1, 2, 3, 5, 8, ____
f) 2,10, 12, 16, 17, 18, 19, ____

a) 1, 3, 5, 7, ___
Lógica: A sequência está aumentando de 2 em 2.
Próximo número: 7 + 2 = 9
Resposta: 9

b) 2, 4, 8, 16, 32, 64, ____
Lógica: Cada número é o dobro do anterior (multiplicação por 2).
Próximo número: 64 * 2 = 128
Resposta: 128

c) 0, 1, 4, 9, 16, 25, 36, ____
Lógica: Os números são quadrados perfeitos
Resposta: 49

d) 4, 16, 36, 64, ____
Lógica: A sequência é formada por quadrados perfeitos de números pares 
Resposta: 100

e) 1, 1, 2, 3, 5, 8, ____
Lógica: Esta é a sequência de Fibonacci, onde cada número é a soma dos dois anteriores.
Resposta: 13

f) 2, 10, 12, 16, 17, 18, 19, ____

Lógica: Todos os números começam com a letra "D". O próximo número que segue essa lógica é DUZENTOS.

Resposta: 200
```

---

```bash
5) Você está em uma sala com três interruptores,
cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está,
mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.
Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

Dado que há 3 salas, cada uma com uma lâmpada:

Na primeira ida:

Ligue o interruptor 1 por 5 minutos e depois desligue-o.
Em seguida, ligue o interruptor 2 e vá imediatamente para uma das 3 salas.
Se a lâmpada estiver acesa, ela é controlada pelo interruptor 2.
Se a lâmpada estiver apagada, mas quente, ela é controlada pelo interruptor 1.
Se a lâmpada estiver apagada e fria, ela é controlada pelo interruptor 3.
Na segunda ida:

Com base na identificação do interruptor 1 e do interruptor 2,
 deixe um dos interruptores ligado e o outro desligado entre os dois restantes.
Vá para a outra sala e identifique os dois interruptores restantes.
```
