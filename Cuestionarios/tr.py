from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage
from scipy.cluster.vq import vq, kmeans
import imageio
import pickle

A = np.array(

[[1, 1, 1, 1, 1, 1, 1, 1],
[1, -1, 1, -1, 1, -1, 1, -1],
[1, 1, -1, -1, 1, 1, -1, -1],
[1, -1, -1, 1, 1, -1, -1, 1],
[1, 1, 1, 1, -1, -1, -1, -1],
[1, -1, 1, -1, -1, 1, -1, 1],
[1, 1, -1, -1, -1, -1, 1, 1],
[1, -1, -1, 1, -1, 1, 1, -1]]
)

B = np.transpose(A)


def reconstruir(bs, C, bloques):
	bloque = []
	index = 0
	for i in range(bs):
		fila = []
		for j in range(bs):
			if i + j < C:
				fila.append(bloques[index])
				index += 1
			else:
				fila.append(0.0)

		bloque.append(fila)

	return np.array(bloque, dtype = float)

def reconstruir_mensaje(bloques):
	imagen = [] 
	indexBloque = 1
	n_filas = imagenCodigo[0][0]
	n_columnas = imagenCodigo[0][1]
	bs = imagenCodigo[0][2]
	C = imagenCodigo[0][3]

	for i in range(n_filas//bs):
		fila_bloques = reconstruir(bs, C, bloques[indexBloque])
		indexBloque += 1
		for j in range(1, n_columnas//bs):
			bloque = reconstruir(bs, C, bloques[indexBloque])
			indexBloque += 1
			bloque2 = np.dot(B, bloque)
			bloque2 = np.dot(bloque2, A)
			fila_bloques = np.append(fila_bloques, bloque2, axis = 1)
		if i == 0:
			imagen = fila_bloques
		else:
			imagen = np.append(imagen, fila_bloques, axis = 0)

	return imagen

with  open('./descarga.csv', 'rb') as file:
    imagenCodigo=pickle.load(file)

bloques = imagenCodigo

imagen = reconstruir_mensaje(imagenCodigo)


plt.imshow(imagen, cmap=plt.cm.gray)
plt.xticks([])
plt.yticks([])
plt.show()
