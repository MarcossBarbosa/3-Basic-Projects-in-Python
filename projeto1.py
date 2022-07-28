# Fatorial de um numero
'''
Crie um programa que recebe um
número e imprime seu fatorial.

#Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e
peça mais informações/investigue mais até você
compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
- numero
2. O que devo fazer com estes dados?
- calcular o fatorial do numero que o usario escolher
3. Quais são as restrições deste problema?
- o Numero nao pode ser negativo e tem que ser um numero inteiro
4. Qual é o resultado esperado?
- calcular o fatorial do numero 
5. Qual é sequência de passos a ser feitas para
chegar ao resultado esperado?

int numero
input numero
if numero < 0
print “digite apenas números positivos”
fatorial = 1
loop de 1 a numero
fatorial = fatorial * numero
print fatorial
'''
numero = int(input('digite um numero'))
if numero < 0:
  print('digite um numero positivo')
fatorial = 1
for i in range(1, numero + 1):
  fatorial = fatorial * i
  print(fatorial)
  