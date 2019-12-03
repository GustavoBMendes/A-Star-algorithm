'''
-Representação do no
	-Tabuleiro 
	-Custo g
	-Custo h'
	-Ponteiro para o vertice pai p(v)

-Representacao dos conjuntos A e F
	-Lista, arvore...

-Funcao GeraSucessor (nó pai)
-Algoritmo A*

-----
caso 1
5 1 2 3 9  6 7 4  13 10 11   8 0 14 15 12
caso 2
2 3 0 8 1 5 4 7 9  6 10 12 13 14 11  15
caso 3
9 5 1 0 13 6 7 2 14 10 11 3 15 12 8  4
caso 5
0 1 3 4 5 2 6 8 9 10 7 11 13 14 15 12
-----
'''
import copy

class no:

	def __init__(self):
		self.matriz = []
		self.g = 0
		self.h = 0
		self.f = 0
		self.pai = None

def print_matriz(matriz):
	for i in range(0,4):
		for j in range(0,4):
			print('{}\t'.format(matriz[i][j]), end = '')
		print('')

def tira_espaco(splitEle, matriz):
	n = 4
	k = 0
	val_remove = ''

	while val_remove in splitEle:
		splitEle.remove(val_remove)

	for i in range(n):
		tmp = []
		for j in range(n):
			tmp.append(int(splitEle[k]))
			k += 1
		matriz.append(tmp[:])
	#print(matriz)
	return matriz

def h1(matriz):
	i = 1
	cont = 0
	for ele in matriz:
		for j in ele:
			if j != i:
				cont += 1
			i += 1
	return cont

def h2(matriz):
	lista = []
	cont = 0

	for i in range(0,4):
		for j in range(0,4):
			lista.append(matriz[i][j])

	for i in range(1,len(lista)):
		if lista[i] != lista[i-1] + 1 and lista[i-1] != 0:
			cont += 1

	return cont

def calcular_dist(matriz, peca):
	for i in range(0,4):
		for j in range(0,4):
			if peca == matriz[i][j]:
				return i,j

def h3(matriz):
	aux = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
	dist = 0

	for i in range(0,4):
		for j in range(0,4):
			if matriz[i][j] != aux[i][j]:
				i2, j2 = calcular_dist(aux, matriz[i][j])
				dist += abs(i-i2) + abs(j - j2)
	return dist

def h4(matriz):
	p1 = 0.1
	p2 = 0.3
	p3 = 0.6
	return (p1 * h1(matriz)) + (p2 * h2(matriz)) + (p3 * h3(matriz))

def h5(matriz):
	return max(h1(matriz), h2(matriz), h3(matriz))

def gera_matriz(m, i, j, novo1, novo2):
	mat_aux = no()
	mat_aux.matriz = copy.deepcopy(m.matriz)

	v_aux = mat_aux.matriz[i][j]
	mat_aux.matriz[i][j] = mat_aux.matriz[novo1][novo2] 
	mat_aux.matriz[novo1][novo2] = v_aux

	mat_aux.g = m.g + 1
	mat_aux.h = h3(mat_aux.matriz)
	mat_aux.f = mat_aux.g + mat_aux.h

	return mat_aux

def gera_sucessor(matriz, sucessores):
	i, j = calcular_dist(matriz.matriz, 0)


	if i == 0:
		if j == 0:
			mat_aux1 = gera_matriz(matriz, i, j, i, j+1)
			sucessores.append(mat_aux1)

			mat_aux2 = gera_matriz(matriz, i, j, i+1, j)
			sucessores.append(mat_aux2)

		elif j == 3:
			mat_aux1 = gera_matriz(matriz, i, j, i, j-1)
			sucessores.append(mat_aux1)

			mat_aux2 = gera_matriz(matriz, i, j, i+1, j)
			sucessores.append(mat_aux2)
		else:
			mat_aux1 = gera_matriz(matriz, i, j, i+1, j)
			sucessores.append(mat_aux1)

			mat_aux2 = gera_matriz(matriz, i, j, i, j-1)
			sucessores.append(mat_aux2)

			mat_aux3 = gera_matriz(matriz, i, j, i, j+1)
			sucessores.append(mat_aux3)

	elif i == 3:
		if j == 0:
			mat_aux1 = gera_matriz(matriz, i, j, i-1, j)
			sucessores.append(mat_aux1)

			mat_aux2 = gera_matriz(matriz, i, j, i, j+1)
			sucessores.append(mat_aux2)
		elif j == 3:
			mat_aux1 = gera_matriz(matriz, i, j, i, j-1)
			sucessores.append(mat_aux1)

			mat_aux2 = gera_matriz(matriz, i, j, i-1, j)
			sucessores.append(mat_aux2)
		else:
			mat_aux1 = gera_matriz(matriz, i, j, i-1, j)
			sucessores.append(mat_aux1)

			mat_aux2 = gera_matriz(matriz, i, j, i, j-1)
			sucessores.append(mat_aux2)

			mat_aux3 = gera_matriz(matriz, i, j, i, j+1)
			sucessores.append(mat_aux3)

	else:
		if j == 0:
			mat_aux1 = gera_matriz(matriz, i, j, i+1, j)
			sucessores.append(mat_aux1)

			mat_aux2 = gera_matriz(matriz, i, j, i-1, j)
			sucessores.append(mat_aux2)

			mat_aux3 = gera_matriz(matriz, i, j, i, j+1)
			sucessores.append(mat_aux3)
		elif j == 3:
			mat_aux1 = gera_matriz(matriz, i, j, i+1, j)
			sucessores.append(mat_aux1)

			mat_aux2 = gera_matriz(matriz, i, j, i-1, j)
			sucessores.append(mat_aux2)

			mat_aux3 = gera_matriz(matriz, i, j, i, j-1)
			sucessores.append(mat_aux3)
		else:
			mat_aux1 = gera_matriz(matriz, i, j, i+1, j)
			sucessores.append(mat_aux1)

			mat_aux2 = gera_matriz(matriz, i, j, i-1, j)
			sucessores.append(mat_aux2)

			mat_aux3 = gera_matriz(matriz, i, j, i, j-1)
			sucessores.append(mat_aux3)

			mat_aux4 = gera_matriz(matriz, i, j, i, j+1)
			sucessores.append(mat_aux4)

	return sucessores

#procura em um dado conjunto o nó com o menor custo f
def min_f(conjunto):
	menor = no()
	menor.f = 9999
	for n in conjunto:
		if n.f <= menor.f:
			menor = n
	return menor

def a_estrela(S):
	A = []
	A.append(S)
	F = []
	T = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
	sucessores = []

	for s in A:
		s.h = h3(s.matriz)
		s.g = 0
		s.pai = 0
		s.f = s.g + s.h
	
	v = min_f(A)
	while len(A) > 0 and v.matriz != T:
		F.append(v)

		#excluir v em A
		A.remove(v)
		#print(v.f)
		#para cada matriz m sucessor da matriz v
		sucessores = gera_sucessor(v, sucessores)	
		for m in sucessores:
			#print(m.matriz)
			for mlinha in A:
				#print(mlinha.matriz)
				if mlinha.matriz == m.matriz and m.g < mlinha.g:
					A.remove(mlinha)

			if (m not in A) and (m not in F):
				A.append(m)
				m.pai = v

		v = min_f(A)
	
	#Se existe v pertence a A tal que v é o f(n) min ou v == T então sucesso, senão fracasso
	#print(v.g)
	print(v.matriz)
	if v.matriz == T:
		print(v.g)
	else:
		print('False')
				
		


def main():
	no1 = no()
	matriz = no1.matriz

	elemento = input()
	splitEle = elemento.split(" ")
	matriz = tira_espaco(splitEle, matriz)
	#h1(matriz)
	#h2(matriz)
	#h3(matriz)
	#print_matriz(matriz)
	no1.matriz = matriz
	'''
	S = []
	S.append(no1)
	
	sucessores = []
	sucessores = gera_sucessor(matriz, sucessores)
	for s in sucessores:
		no_x = no()
		no_x.matriz = s.matriz
		S.append(no_x)
	'''
	a_estrela(no1)

if __name__ == '__main__':
	main()