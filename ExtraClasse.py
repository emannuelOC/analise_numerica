# -*- coding: utf-8 -*-

################################
## EXERCÍCIOS EXTRA CLASSE 02 ##
################################

"""
1. Descreva em pseudocódigo um algoritmo
para calcular uma aproximação da função 
f(x) = e^x utilizando a expansão em 
Série de Taylor truncada. Calcule a 
complexidade com a cota superior deste 
algoritmo.

sum recebe 0
para i de 0 até N
	sum recebe sum + (x^i)/fatorial(i)
retorne sum

. Complexidade: A complexidade depende
da implementação da função fatorial(x).
Desconsiderando essa função, a complexidade
do algoritmo é O(N).
Caso a função fatorial tenha sido implementada
de modo que cada fatorial só precise ser 
calculado uma vez, a complexidade do 
algoritmo é O(N * x)
"""

###################################

"""
2. Utilizando o seu algoritmo, calcule 
aproximações para e^3 com N = 5 e N = 10,
utilizando aritmética de arredondamento
com 4 casas decimais. Para qual valor de N
(5 ou 10), a aproximação pareceu ser mais
precisa? Por quê?

"""

def euler(x, N):
	result = 0
	for i in xrange(N):
		result += x**i/factorial(i)
	return result

factorials = {"0": 1, "1": 1}

def factorial(x):
	if str(x) in factorials.keys():
		return factorials[str(x)]
	return x * factorial(x - 1)

print "%.4f" %(euler(1.0,5))
print "%.4f" %(euler(1.0,7))
print "%.4f" %(euler(1.0,10))
print "%.4f" %(euler(1.0,15))

"""
A aproximação com N = 10 parece ser mais
precisa porque depois desse valor o resultado
permanece o mesmo (com precisão de 4 casas).
"""

###################################



