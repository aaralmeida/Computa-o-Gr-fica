import numpy as np
from random import randint, uniform
import matplotlib.pyplot as plt

	# Aplicação do Algoritmo de Bresenham 
	# Autor: Armando Alan Ramalho de Almeida
	# Trabalho de Processamento Digital de Imagens 
	# Professor: Thiago Sylas 



def criamatriz(pontox, pontoy): #Função que criará uma matriz dinamicamente, conforme o ponto máximo e minímo digitado pelo usuário
	matriz = []
	linhamax= max(pontoy) +40
	linhamin= min(pontoy)  #Armazena em variáveis quais os pontos máximos e minimos de x
	colunamax= max(pontox)+40
	colunamin= min(pontox)  #Armazena em variáveis quais os pontos máximos e minimos de y
	for i in range(linhamin, linhamax): #Loop para criar a matriz
		aux = [] #cria as colunas 
		for j in range(colunamin , colunamax): #Linhas da Matriz
			aux.append(0)
		matriz.append(aux)
	return matriz 


def bresenham(x1, y1, x2, y2): #Função que roda o algoritmo de Bresenham
	if (y1 > y2):	#Isso é feito para o caso de retas com angulos menores que 0
		cordenadas = bresenham(x2,y2,x1,y1) #Chamada recursiva mudando as coordenadas, será criado uma reta invertida
	else:	
		x = x1 
		y = y1
		cordenadas = [x, y] #Lista que armazenará os pontos que serão percorridos
		dx = abs(x2 - x1)  #Tamanho da reta em x
		dy = abs(y2 - y1) #Tamanho da reta em y
		d = 2*dy - dx #D inicial
		incBaixo = 2*dy # Fórmula usada somente quando cordenada x é incrementada
		incCima = 2*(dy-dx) #Fórmula usada quando a cordenada x e y é incrementada
		incy = 1 #incremento padrão de y
		while (x != x2):
			incx = 1 #incremento padrão de x
			if(d <= 0):
				if (x1 > x2): #Usado caso a reta tenha um angulo menor que 0
					incx = incx*(-1)
				d = d + incBaixo
				x = x +  incx
			else:
				if (x1 > x2):  #Usado caso a reta tenha um angulo menor que 0
					incx = incx*(-1)
				d = d + incCima
				x = x + incx
				y = y + incy
			cordenadas.append(x) #adicina a cordenada na lista
			cordenadas.append(y)
	return cordenadas

def criareta(pontox, pontoy): #Função que chamará a função bresenham a quantidade de vezes necessária
	percurso = [] 
	for i in range (0, len(pontox)):
		if i == len(pontox) - 1: 
			break
		reta = bresenham(pontox[i],pontoy[i],pontox[i+1],pontoy[i+1])
		for i in range(0,len(reta)):
			percurso.append(reta[i])
	return percurso

# percurso = criareta(pontox, pontoy)

# print(percurso)
# def proporcionarmatriz(cordenadasx,cordenadasy, centrox, centroy):
# 	x = []
# 	y = []
# 	for i in range(0, len(cordenadasx)):
# 		x.append(cordenadasx[i]+centrox)
# 		y.append(cordenadasy[i]+centroy)
# 	return

def marcamatriz(percurso, pontox, pontoy): # Coloca na matriz os "pixels" que foram acionados 
	cordenadasx =percurso[0::2] 
	cordenadasy =percurso[1::2]
	matrizdeplot = criamatriz(pontox, pontoy)
	centrox = int(len(matrizdeplot)/2)
	centroy = int(len(matrizdeplot[1])/2)

	for i in range(0, len(cordenadasx)):
		cordenadasx[i] = centrox - cordenadasx[i]
		cordenadasy[i] = centroy + cordenadasy[i]
	print(cordenadasx)
	print(cordenadasy)
	for i in range(0, len(cordenadasx)):
		print(cordenadasx[i])
		print(cordenadasy[i])
		matrizdeplot[cordenadasx[i]][cordenadasy[i]] = 1

	return matrizdeplot


def main (pontox, pontoy): #Chama todas as outras funcões
	percurso = criareta(pontox, pontoy)
	matrizdeplot = marcamatriz(percurso, pontox, pontoy)
	return matrizdeplot

n_ponto = int(input("Entre com o número de pontos: (minimo 2) \n"))
pontox = []
pontoy = []
for i in range(0, n_ponto):
	y = int(input("Entre com a cordenada x" + str(i + 1) + "\n"))
	pontox.append(y)
	x = int(input("Entre com a cordenada y" + str(i + 1) + "\n"))
	pontoy.append(x)	

main = main(pontox, pontoy)
percurso = criareta(pontox, pontoy)
print(percurso)
plt.figure(1)
plt.imshow(main, interpolation ='nearest' ,cmap=plt.cm.gray)
plt.grid(True)
plt.show()
