from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage
from scipy.cluster.vq import vq, kmeans
import imageio
import pickle

def reconstruir (bloques, imagen_x, imagen_y, n_bloque):
	print(len(bloques))
	block_index = 0
	reconstruccion = []

	for i in range(0, imagen_x//n_bloque):
		blocks_row = bloques[block_index]
		block_index += 1
		for j in range(1, imagen_y//n_bloque):
			blocks_row = np.append(blocks_row, bloques[block_index], axis = 1)
			block_index += 1
		if i == 0:
			reconstruccion = blocks_row
		else:
			reconstruccion = np.append(reconstruccion, blocks_row, axis = 0)
	return reconstruccion

def Dibuja_imagen_cuantizada_KMeans(imagenCodigo):
	imagen_x = imagenCodigo[0][0]
	print(imagen_x)
	imagen_y = imagenCodigo[0][1]
	n_bloque = imagenCodigo[0][2]
	diccionario = imagenCodigo[1]
	indices = imagenCodigo[2]

	imagenRecuperada = reconstruir(np.array([diccionario[i] for i in indices]), imagen_x, imagen_y, n_bloque)
	return imagenRecuperada

with  open('./descarga.csv', 'rb') as file:
    imagenCodigo=pickle.load(file)

imagen = Dibuja_imagen_cuantizada_KMeans(imagenCodigo)
plt.imshow(imagen, cmap=plt.cm.gray)
plt.xticks([])
plt.yticks([])
plt.show()
