# Chute um numero 
'''

Escreva um programa que, ao iniciar gera um
valor aleatório de 1 a 10 e permite que o usuário
chute um número até que o valor aleatório gerado
no início do programa seja chutado corretamente.

O programa deve informar se o chute foi acima,
abaixo ou igual ao valor aleatório gerado no início
do programa.

1. Quais são os dados de entrada necessários?
- Um valor aleatório de 1 a 10
- Um chute do usuário

2. O que devo fazer com estes dados?
- Devo pegar o valor aleatório de 1 a 10 que foi gerado e
comparar com o valor que foi chutado pelo usuário.
- Se o chute for maior ou menor que valor gerado, alertar o
usuário sobre isso e o deixar jogar novamente até que
acerte o número que foi gerado.

3. Quais são as restrições deste problema?
- tem quer ser uma valor aleatorio de 1 a 10
- o programa nao deve terminar enquanto o usuario nao acertar

4. Qual é o resultado esperado?
- O programa identificar que o valor chutado
pelo usuário é igual ao valor gerado no
início do programa.

5. Qual é sequência de passos a ser feitas para
chegar ao resultado esperado?

input valor_aleatorio entre 1 a 10
input chute
if chute > valor_aleatorio
print "Chute é maior que valor gerado"
if chute < valor_aleatorio
print "Chute é menor que valor gerado"
if chute = valor_aleatorio
print 'Acertou o chute!'
acertou = verdadeiro
else
print 'Você chutou um valor inválido'
'''
import random
valorA = random.randint(1, 10)
acertou = False
while acertou == False: 
  numero = int(input('chute um numero de 1 a 10 '))
  if numero > valorA:
    print('chute maior que valor gerado ')
  elif numero < valorA:
    print('chute é menor que valor gerado ')
  elif numero == valorA:
    acertou = True
    print('acertou o numero '''')
  

  
