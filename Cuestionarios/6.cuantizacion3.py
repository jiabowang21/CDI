#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scipy
import scipy.ndimage
from scipy.cluster.vq import vq, kmeans, whiten
from scipy import misc

import numpy as np
import time
import matplotlib.pyplot as plt
import imageio
import PIL
import pickle
import math

# EJERCICIO 1
'''
x = np.array([1.5933011778800474, 1.3923011778800474, 1.5383011778800473, 1.1303011778800474, 1.5193011778800474, 1.0233011778800474, 1.2973011778800474, 1.4593011778800473])

suma = 0
for i in range(len(x)):
	suma += x[i]*x[i]

IIxII = suma
print(IIxII)


y = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

A = np.array([[0.35355339059327373, 0.35355339059327373, 0.35355339059327373, 0.35355339059327373, 0.35355339059327373, 0.35355339059327373, 0.35355339059327373, 0.35355339059327373],
[0.35355339059327373, 0.35355339059327373, 0.35355339059327373, 0.35355339059327373, -0.35355339059327373, -0.35355339059327373, -0.35355339059327373, -0.35355339059327373],
[0.35355339059327373, 0.35355339059327373, -0.35355339059327373, -0.35355339059327373, -0.35355339059327373, -0.35355339059327373, 0.35355339059327373, 0.35355339059327373],
[0.35355339059327373, 0.35355339059327373, -0.35355339059327373, -0.35355339059327373, 0.35355339059327373, 0.35355339059327373, -0.35355339059327373, -0.35355339059327373],
[0.35355339059327373, -0.35355339059327373, -0.35355339059327373, 0.35355339059327373, 0.35355339059327373, -0.35355339059327373, -0.35355339059327373, 0.35355339059327373],
[0.35355339059327373, -0.35355339059327373, -0.35355339059327373, 0.35355339059327373, -0.35355339059327373, 0.35355339059327373, 0.35355339059327373, -0.35355339059327373],
[0.35355339059327373, -0.35355339059327373, 0.35355339059327373, -0.35355339059327373, -0.35355339059327373, 0.35355339059327373, -0.35355339059327373, 0.35355339059327373],
[0.35355339059327373, -0.35355339059327373, 0.35355339059327373, -0.35355339059327373, 0.35355339059327373, -0.35355339059327373, 0.35355339059327373, -0.35355339059327373]])

for i in range(len(A)):
	for j in range(len(A[0])):
		y[i] += A[i][j]*x[j]

y[2:] = 0.0

print(y)

x2 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
B = np.linalg.inv(A)

for i in range(len(A)):
	for j in range(len(A[0])):
		x2[i] += B[i][j]*y[j]

print(x2)

suma = 0
for i in range(len(x2)):
	suma += x2[i]*x2[i]

IIx2II = suma
print(IIx2II)

print(IIx2II/IIxII)

'''
"""
# EJERCICIO 2
def reconstruir_bloque(bs, C, bloque):
	bloqueReconstruido = []
	index = 0
	for i in range(bs):
		fila = []
		for j in range(bs):
			if i+j < C:
				fila.append(bloque[index])
				index += 1
			else:
				fila.append(0.0)
		bloqueReconstruido.append(fila)
	return np.array(bloqueReconstruido, dtype = float)

def reconstruir_imagen(imagenCodigo):

	A = np.array([[1, 1, 1, 1, 1, 1, 1, 1],
	[1, -1, 1, -1, 1, -1, 1, -1],
	[1, 1, -1, -1, 1, 1, -1, -1],
	[1, -1, -1, 1, 1, -1, -1, 1],
	[1, 1, 1, 1, -1, -1, -1, -1],
	[1, -1, 1, -1, -1, 1, -1, 1],
	[1, 1, -1, -1, -1, -1, 1, 1],
	[1, -1, -1, 1, -1, 1, 1, -1]])
	AT = np.transpose(A)

	n_filas = imagenCodigo[0][0]
	n_columnas = imagenCodigo[0][1]
	bs = imagenCodigo[0][2]
	C = imagenCodigo[0][3]

	imagen = []
	indexBloque = 1
	
	#print('\n', len(imagenCodigo[1:]), '\n')
	for i in range(n_filas//bs):
		bloque1 = reconstruir_bloque(bs, C, imagenCodigo[indexBloque])
		bloque2 = np.dot(AT, bloque1)
		bloque3 = np.dot(bloque2, A)
		fila_bloques = bloque3
		indexBloque += 1
		for j in range(1, n_columnas//bs):
			bloque4 = reconstruir_bloque(bs, C, imagenCodigo[indexBloque])
			bloque5 = np.dot(AT, bloque4)
			bloque6 = np.dot(bloque5, A)
			indexBloque += 1
			fila_bloques = np.append(fila_bloques, bloque6, axis = 1)
		if i == 0:
			imagen = fila_bloques
		else:
			imagen = np.append(imagen, fila_bloques, axis = 0)
	return imagen
			

with  open('EdKvIuDy.csv', 'rb') as file:
	imagenCodigo=pickle.load(file)

imagen = reconstruir_imagen(imagenCodigo)
plt.imshow(imagen, cmap=plt.cm.gray,vmin=0, vmax=255)
plt.show()

"""

# EJERCICIO 3

I = np.array([[1, 1, 1, 1, 1, 1, 1, 1]])

A = np.array([[0.0, -0.60302, 0.55048, 0.20943, 0.24678, 0.21622, 0.12309, -0.40825]])
AT = np.transpose(A)

X = AT*I*A

plt.figure()
plt.imshow(X, cmap=plt.cm.gray)
plt.show()


# EJERCICIO 4
"""
A = np.array(
[[-0.1780024, 0.0281919, -0.7144872, -0.0318181],
[-0.5564824, -0.2588556, -0.034254, -0.1878905],
[-0.0987746, -0.0227031, -0.1727404, -0.6140228],
[0.0329318, -0.2631657, -0.5614113, -0.2379304]])
AI = np.linalg.inv(A)
AT = np.transpose(A)
print(AI)
print(AT)
print(np.array_equal(AI, AT))
"""

