# Medidor de velocidade

'''
Levando em considerção a velocidade maxima permitida de 80km em uma determinada rua. Crie um programa que recebe do usuario um valor que representa a velocidade e com base nessa velocidade diga se ele tomou uma multa leve, grave ou gravissima. Levando em consideração que se a pessoa estiver abaixo da velocidade maxima seu progrma deve exibir "não ouve multa", caso esteja ate 10km acima "levou multa leve", caso esteja entre 11 a 20 km "levou multa grave", caso esteja acima de 20 km exiba "levou multa gravissima".

#Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e
peça mais informações/investigue mais até você
compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
-velocidade do usuario
-
2. O que devo fazer com estes dados?
- Levando em consideração que se a pessoa estiver abaixo da velocidade maxima seu progrma deve exibir "não ouve multa", caso esteja ate 10km acima "levou multa leve", caso esteja entre 11 a 20 km "levou multa grave", caso esteja acima de 20 km exiba "levou multa gravissima".
3. Quais são as restrições deste problema?

4. Qual é o resultado esperado?
- exibir o resujltado da multa que a pessoa levou
se a pessoa estiver abaixo da velocidade maxima seu progrma deve exibir "não ouve multa", caso esteja ate 10km acima "levou multa leve", caso esteja entre 11 a 20 km "levou multa grave", caso esteja acima de 20 km exiba "levou multa gravissima".

5. Qual é sequência de passos a ser feitas para
chegar ao resultado esperado?

velocidade maxima = 80
input = velocidade do usuario
if velocidade do usuario <= velocidade maxima:
 print "nao ouve multa"
if velocidade do usuario > velocidade maxima e velocidade do usuario <= velocidade maxima + 10:
print "voce levou multa leve"
if velocidade do usuario > velocidade maxima + 11 e velocidade do usuario <= velocidade maxima +20:
print "voce levou multa media"
if velocidade do usuario > velocidade maxima +20:
print "levou multa gravissima"
'''

velocidadeU = int(input("digite sua velocidade "))
velocidadeM = 80

if velocidadeU <= velocidadeM:
  print("Sem multas")
elif velocidadeU > velocidadeM and velocidadeU <= velocidadeM + 10:
  print("levou multa leve")
elif velocidadeU >= velocidadeM + 11 and velocidadeU <= velocidadeM +20:
  print("levou multa grave")
elif velocidadeU > velocidadeM +20:
  print("levou multa gravissima")
