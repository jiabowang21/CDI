from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
import PIL
import pickle

import scipy.ndimage
from scipy.cluster.vq import vq, kmeans

#%%
"""
imagen = np.array([[57, 79, 48, 77, 88, 44, 43, 57], [56, 70, 46, 79, 79, 54, 41, 60], [70, 60, 48, 81, 66, 57, 40, 55], [71, 72, 49, 82, 56, 65, 47, 45], [61, 82, 51, 76, 52, 74, 45, 41], [54, 83, 50, 65, 46, 72, 45, 41], [48, 78, 50, 53, 45, 58, 51, 42], [46, 80, 59, 52, 50, 46, 60, 44]])
(n,m)=imagen.shape # filas y columnas de la imagen
plt.imshow(imagen, cmap=plt.cm.gray)
plt.xticks([])
plt.yticks([])
plt.show()
"""
def nivelar(k, minN, maxN):
    i = minN
    niveles = []
    partes = (maxN + 1 - minN) / k
    while i <= maxN:
    	niveles.append(i)
    	i += partes 
    niveles.append(i)
    return niveles


def asignar_nivel(niveles, pixel):
    index = -1
    for i in niveles:
    	if pixel >= i:
    		index += 1
    return index


def cuantizar(im, k, minN, maxN):
    niveles = nivelar(pow(2, k), minN, maxN)
    print(niveles)
    new_im = im.copy()
    for index_row, row in enumerate(new_im):
        for index_pixel, pixel in enumerate(row):
            new_im[index_row][index_pixel] = asignar_nivel(niveles, pixel)
    return new_im
"""
k = 2
minN = 40
maxN = 88
imagenCuantizada = cuantizar(imagen, k, minN, maxN)
print(imagenCuantizada)
"""
def asignar_nivel2(niveles, pixel):
	medio = niveles[pixel] + niveles[pixel + 1]
	medio = medio/2
	return medio

def deshacer(im, k, minN, maxN):
	niveles = nivelar(pow(2, k), minN, maxN)
	new_im = im.copy()
	for index_row, row in enumerate(new_im):
		for index_pixel, pixel in enumerate(row):
			new_im[index_row][index_pixel] = asignar_nivel2(niveles, pixel)
	return new_im
"""
imagenRecuperada = deshacer(imagenCuantizada, k, minN, maxN)
print(imagenRecuperada)

plt.imshow(imagenRecuperada, cmap=plt.cm.gray)
plt.xticks([])
plt.yticks([])
plt.show()
"""

with  open('./descarga.csv', 'rb') as file:
    imagenCodigo=pickle.load(file)

#print(imagenCodigo)

n = imagenCodigo[0][0]
m = imagenCodigo[0][1]
n_bloque = imagenCodigo[0][2]
k = imagenCodigo[0][3]

n_f = int(n / n_bloque)
print(n_f)
m_f = int(m / n_bloque)

l = []

i2 = 0

bloques = []

print(len(imagenCodigo))

for i in range(1, len(imagenCodigo)):
	#print(imagenCodigo[i])
	#print("HH")
	bloque = imagenCodigo[i]
	minN = bloque[0][0]
	maxN = bloque[0][1]
	bloque_recuperado = deshacer(bloque[1], k, minN, maxN)
	#print(bloque)
	#print(minN)
	#print(maxN)
	#print(bloque_recuperado)

	if i2 < n_f:
		bloques.append(bloque_recuperado)
		i2 += 1
	elif i2 == n_f:
		
		l.append(bloques)
		i2 = 0
		bloques = []
		bloques.append(bloque_recuperado)

print(len(l[0]))

arr = np.array(l[0][0])
arr = np.append(arr, l[0][1], axis = 1)
arr = np.append(arr, l[0][2], axis = 1)
arr = np.append(arr, l[0][3], axis = 1)
arr = np.append(arr, l[0][4], axis = 1)
arr = np.append(arr, l[0][5], axis = 1)
arr = np.append(arr, l[0][6], axis = 1)
arr = np.append(arr, l[0][7], axis = 1)
arr = np.append(arr, l[0][8], axis = 1)
arr = np.append(arr, l[0][9], axis = 1)
arr = np.append(arr, l[0][10], axis = 1)
arr = np.append(arr, l[0][11], axis = 1)
arr = np.append(arr, l[0][12], axis = 1)
arr = np.append(arr, l[0][13], axis = 1)
arr = np.append(arr, l[0][14], axis = 1)
arr = np.append(arr, l[0][15], axis = 1)


arr2 = np.array(l[1][0])
arr2 = np.append(arr2, l[1][1], axis = 1)
arr2 = np.append(arr2, l[1][2], axis = 1)
arr2 = np.append(arr2, l[1][3], axis = 1)
arr2 = np.append(arr2, l[1][4], axis = 1)
arr2 = np.append(arr2, l[1][5], axis = 1)
arr2 = np.append(arr2, l[1][6], axis = 1)
arr2 = np.append(arr2, l[1][7], axis = 1)
arr2 = np.append(arr2, l[1][8], axis = 1)
arr2 = np.append(arr2, l[1][9], axis = 1)
arr2 = np.append(arr2, l[1][10], axis = 1)
arr2 = np.append(arr2, l[1][11], axis = 1)
arr2 = np.append(arr2, l[1][12], axis = 1)
arr2 = np.append(arr2, l[1][13], axis = 1)
arr2 = np.append(arr2, l[1][14], axis = 1)
arr2 = np.append(arr2, l[1][15], axis = 1)

arr3 = np.array(l[2][0])
arr3 = np.append(arr3, l[2][1], axis = 1)
arr3 = np.append(arr3, l[2][2], axis = 1)
arr3 = np.append(arr3, l[2][3], axis = 1)
arr3 = np.append(arr3, l[2][4], axis = 1)
arr3 = np.append(arr3, l[2][5], axis = 1)
arr3 = np.append(arr3, l[2][6], axis = 1)
arr3 = np.append(arr3, l[2][7], axis = 1)
arr3 = np.append(arr3, l[2][8], axis = 1)
arr3 = np.append(arr3, l[2][9], axis = 1)
arr3 = np.append(arr3, l[2][10], axis = 1)
arr3 = np.append(arr3, l[2][11], axis = 1)
arr3 = np.append(arr3, l[2][12], axis = 1)
arr3 = np.append(arr3, l[2][13], axis = 1)
arr3 = np.append(arr3, l[2][14], axis = 1)
arr3 = np.append(arr3, l[2][15], axis = 1)

arr4 = np.array(l[3][0])
arr4 = np.append(arr4, l[3][1], axis = 1)
arr4 = np.append(arr4, l[3][2], axis = 1)
arr4 = np.append(arr4, l[3][3], axis = 1)
arr4 = np.append(arr4, l[3][4], axis = 1)
arr4 = np.append(arr4, l[3][5], axis = 1)
arr4 = np.append(arr4, l[3][6], axis = 1)
arr4 = np.append(arr4, l[3][7], axis = 1)
arr4 = np.append(arr4, l[3][8], axis = 1)
arr4 = np.append(arr4, l[3][9], axis = 1)
arr4 = np.append(arr4, l[3][10], axis = 1)
arr4 = np.append(arr4, l[3][11], axis = 1)
arr4 = np.append(arr4, l[3][12], axis = 1)
arr4 = np.append(arr4, l[3][13], axis = 1)
arr4 = np.append(arr4, l[3][14], axis = 1)
arr4 = np.append(arr4, l[3][15], axis = 1)

arr5 = np.array(l[4][0])
arr5 = np.append(arr5, l[4][1], axis = 1)
arr5 = np.append(arr5, l[4][2], axis = 1)
arr5 = np.append(arr5, l[4][3], axis = 1)
arr5 = np.append(arr5, l[4][4], axis = 1)
arr5 = np.append(arr5, l[4][5], axis = 1)
arr5 = np.append(arr5, l[4][6], axis = 1)
arr5 = np.append(arr5, l[4][7], axis = 1)
arr5 = np.append(arr5, l[4][8], axis = 1)
arr5 = np.append(arr5, l[4][9], axis = 1)
arr5 = np.append(arr5, l[4][10], axis = 1)
arr5 = np.append(arr5, l[4][11], axis = 1)
arr5 = np.append(arr5, l[4][12], axis = 1)
arr5 = np.append(arr5, l[4][13], axis = 1)
arr5 = np.append(arr5, l[4][14], axis = 1)
arr5 = np.append(arr5, l[4][15], axis = 1)

arr6 = np.array(l[5][0])
arr6 = np.append(arr6, l[5][1], axis = 1)
arr6 = np.append(arr6, l[5][2], axis = 1)
arr6 = np.append(arr6, l[5][3], axis = 1)
arr6 = np.append(arr6, l[5][4], axis = 1)
arr6 = np.append(arr6, l[5][5], axis = 1)
arr6 = np.append(arr6, l[5][6], axis = 1)
arr6 = np.append(arr6, l[5][7], axis = 1)
arr6 = np.append(arr6, l[5][8], axis = 1)
arr6 = np.append(arr6, l[5][9], axis = 1)
arr6 = np.append(arr6, l[5][10], axis = 1)
arr6 = np.append(arr6, l[5][11], axis = 1)
arr6 = np.append(arr6, l[5][12], axis = 1)
arr6 = np.append(arr6, l[5][13], axis = 1)
arr6 = np.append(arr6, l[5][14], axis = 1)
arr6 = np.append(arr6, l[5][15], axis = 1)

arr7 = np.array(l[1][0])
arr7 = np.append(arr7, l[6][1], axis = 1)
arr7 = np.append(arr7, l[6][2], axis = 1)
arr7 = np.append(arr7, l[6][3], axis = 1)
arr7 = np.append(arr7, l[6][4], axis = 1)
arr7 = np.append(arr7, l[6][5], axis = 1)
arr7 = np.append(arr7, l[6][6], axis = 1)
arr7 = np.append(arr7, l[6][7], axis = 1)
arr7 = np.append(arr7, l[6][8], axis = 1)
arr7 = np.append(arr7, l[6][9], axis = 1)
arr7 = np.append(arr7, l[6][10], axis = 1)
arr7 = np.append(arr7, l[6][11], axis = 1)
arr7 = np.append(arr7, l[6][12], axis = 1)
arr7 = np.append(arr7, l[6][13], axis = 1)
arr7 = np.append(arr7, l[6][14], axis = 1)
arr7 = np.append(arr7, l[6][15], axis = 1)

arr8 = np.array(l[7][0])
arr8 = np.append(arr8, l[7][1], axis = 1)
arr8 = np.append(arr8, l[7][2], axis = 1)
arr8 = np.append(arr8, l[7][3], axis = 1)
arr8 = np.append(arr8, l[7][4], axis = 1)
arr8 = np.append(arr8, l[7][5], axis = 1)
arr8 = np.append(arr8, l[7][6], axis = 1)
arr8 = np.append(arr8, l[7][7], axis = 1)
arr8 = np.append(arr8, l[7][8], axis = 1)
arr8 = np.append(arr8, l[7][9], axis = 1)
arr8 = np.append(arr8, l[7][10], axis = 1)
arr8 = np.append(arr8, l[7][11], axis = 1)
arr8 = np.append(arr8, l[7][12], axis = 1)
arr8 = np.append(arr8, l[7][13], axis = 1)
arr8 = np.append(arr8, l[7][14], axis = 1)
arr8 = np.append(arr8, l[7][15], axis = 1)

arr9 = np.array(l[8][0])
arr9 = np.append(arr9, l[8][1], axis = 1)
arr9 = np.append(arr9, l[8][2], axis = 1)
arr9 = np.append(arr9, l[8][3], axis = 1)
arr9 = np.append(arr9, l[8][4], axis = 1)
arr9 = np.append(arr9, l[8][5], axis = 1)
arr9 = np.append(arr9, l[8][6], axis = 1)
arr9 = np.append(arr9, l[8][7], axis = 1)
arr9 = np.append(arr9, l[8][8], axis = 1)
arr9 = np.append(arr9, l[8][9], axis = 1)
arr9 = np.append(arr9, l[8][10], axis = 1)
arr9 = np.append(arr9, l[8][11], axis = 1)
arr9 = np.append(arr9, l[8][12], axis = 1)
arr9 = np.append(arr9, l[8][13], axis = 1)
arr9 = np.append(arr9, l[8][14], axis = 1)
arr9 = np.append(arr9, l[8][15], axis = 1)

arr10 = np.array(l[9][0])
arr10 = np.append(arr10, l[9][1], axis = 1)
arr10 = np.append(arr10, l[9][2], axis = 1)
arr10 = np.append(arr10, l[9][3], axis = 1)
arr10 = np.append(arr10, l[9][4], axis = 1)
arr10 = np.append(arr10, l[9][5], axis = 1)
arr10 = np.append(arr10, l[9][6], axis = 1)
arr10 = np.append(arr10, l[9][7], axis = 1)
arr10 = np.append(arr10, l[9][8], axis = 1)
arr10 = np.append(arr10, l[9][9], axis = 1)
arr10 = np.append(arr10, l[9][10], axis = 1)
arr10 = np.append(arr10, l[9][11], axis = 1)
arr10 = np.append(arr10, l[9][12], axis = 1)
arr10 = np.append(arr10, l[9][13], axis = 1)
arr10 = np.append(arr10, l[9][14], axis = 1)
arr10 = np.append(arr10, l[9][15], axis = 1)

arr11 = np.array(l[10][0])
arr11 = np.append(arr11, l[10][1], axis = 1)
arr11 = np.append(arr11, l[10][2], axis = 1)
arr11 = np.append(arr11, l[10][3], axis = 1)
arr11 = np.append(arr11, l[10][4], axis = 1)
arr11 = np.append(arr11, l[10][5], axis = 1)
arr11 = np.append(arr11, l[10][6], axis = 1)
arr11 = np.append(arr11, l[10][7], axis = 1)
arr11 = np.append(arr11, l[10][8], axis = 1)
arr11 = np.append(arr11, l[10][9], axis = 1)
arr11 = np.append(arr11, l[10][10], axis = 1)
arr11 = np.append(arr11, l[10][11], axis = 1)
arr11 = np.append(arr11, l[10][12], axis = 1)
arr11 = np.append(arr11, l[10][13], axis = 1)
arr11 = np.append(arr11, l[10][14], axis = 1)
arr11 = np.append(arr11, l[10][15], axis = 1)

arr12 = np.array(l[11][0])
arr12 = np.append(arr12, l[11][1], axis = 1)
arr12 = np.append(arr12, l[11][2], axis = 1)
arr12 = np.append(arr12, l[11][3], axis = 1)
arr12 = np.append(arr12, l[11][4], axis = 1)
arr12 = np.append(arr12, l[11][5], axis = 1)
arr12 = np.append(arr12, l[11][6], axis = 1)
arr12 = np.append(arr12, l[11][7], axis = 1)
arr12 = np.append(arr12, l[11][8], axis = 1)
arr12 = np.append(arr12, l[11][9], axis = 1)
arr12 = np.append(arr12, l[11][10], axis = 1)
arr12 = np.append(arr12, l[11][11], axis = 1)
arr12 = np.append(arr12, l[11][12], axis = 1)
arr12 = np.append(arr12, l[11][13], axis = 1)
arr12 = np.append(arr12, l[11][14], axis = 1)
arr12 = np.append(arr12, l[11][15], axis = 1)

arr13 = np.array(l[12][0])
arr13 = np.append(arr13, l[12][1], axis = 1)
arr13 = np.append(arr13, l[12][2], axis = 1)
arr13 = np.append(arr13, l[12][3], axis = 1)
arr13 = np.append(arr13, l[12][4], axis = 1)
arr13 = np.append(arr13, l[12][5], axis = 1)
arr13 = np.append(arr13, l[12][6], axis = 1)
arr13 = np.append(arr13, l[12][7], axis = 1)
arr13 = np.append(arr13, l[12][8], axis = 1)
arr13 = np.append(arr13, l[12][9], axis = 1)
arr13 = np.append(arr13, l[12][10], axis = 1)
arr13 = np.append(arr13, l[12][11], axis = 1)
arr13 = np.append(arr13, l[12][12], axis = 1)
arr13 = np.append(arr13, l[12][13], axis = 1)
arr13 = np.append(arr13, l[12][14], axis = 1)
arr13 = np.append(arr13, l[12][15], axis = 1)

arr14 = np.array(l[13][0])
arr14 = np.append(arr14, l[13][1], axis = 1)
arr14 = np.append(arr14, l[13][2], axis = 1)
arr14 = np.append(arr14, l[13][3], axis = 1)
arr14 = np.append(arr14, l[13][4], axis = 1)
arr14 = np.append(arr14, l[13][5], axis = 1)
arr14 = np.append(arr14, l[13][6], axis = 1)
arr14 = np.append(arr14, l[13][7], axis = 1)
arr14 = np.append(arr14, l[13][8], axis = 1)
arr14 = np.append(arr14, l[13][9], axis = 1)
arr14 = np.append(arr14, l[13][10], axis = 1)
arr14 = np.append(arr14, l[13][11], axis = 1)
arr14 = np.append(arr14, l[13][12], axis = 1)
arr14 = np.append(arr14, l[13][13], axis = 1)
arr14 = np.append(arr14, l[13][14], axis = 1)
arr14 = np.append(arr14, l[13][15], axis = 1)

arr15 = np.array(l[14][0])
arr15 = np.append(arr15, l[14][1], axis = 1)
arr15 = np.append(arr15, l[14][2], axis = 1)
arr15 = np.append(arr15, l[14][3], axis = 1)
arr15 = np.append(arr15, l[14][4], axis = 1)
arr15 = np.append(arr15, l[14][5], axis = 1)
arr15 = np.append(arr15, l[14][6], axis = 1)
arr15 = np.append(arr15, l[14][7], axis = 1)
arr15 = np.append(arr15, l[14][8], axis = 1)
arr15 = np.append(arr15, l[14][9], axis = 1)
arr15 = np.append(arr15, l[14][10], axis = 1)
arr15 = np.append(arr15, l[14][11], axis = 1)
arr15 = np.append(arr15, l[14][12], axis = 1)
arr15 = np.append(arr15, l[14][13], axis = 1)
arr15 = np.append(arr15, l[14][14], axis = 1)
arr15 = np.append(arr15, l[14][15], axis = 1)
"""
arr16 = np.array(l[15][0])
arr16 = np.append(arr16, l[15][1], axis = 1)
arr16 = np.append(arr16, l[15][2], axis = 1)
arr16 = np.append(arr16, l[15][3], axis = 1)
arr16 = np.append(arr16, l[15][4], axis = 1)
arr16 = np.append(arr16, l[15][5], axis = 1)
arr16 = np.append(arr16, l[15][6], axis = 1)
arr16 = np.append(arr16, l[15][7], axis = 1)
arr16 = np.append(arr16, l[15][8], axis = 1)
arr16 = np.append(arr16, l[15][9], axis = 1)
arr16 = np.append(arr16, l[15][10], axis = 1)
arr16 = np.append(arr16, l[15][11], axis = 1)
arr16 = np.append(arr16, l[15][12], axis = 1)
arr16 = np.append(arr16, l[15][13], axis = 1)
arr16 = np.append(arr16, l[15][14], axis = 1)
arr16 = np.append(arr16, l[15][15], axis = 1)
"""
final = np.concatenate((arr, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9, arr10, arr11, arr12, arr13, arr14, arr15))

print(final)

plt.imshow(final, cmap=plt.cm.gray)
plt.xticks([])
plt.yticks([])
plt.show()

"""
def reconstruir(bloques):
    a, b, c = bloques.shape
    n_bloques = b*c
    new_im = np.concatenate(bloques[0:n_bloques])
    i = n_bloques
    while i < len(bloques):
        new_im = np.concatenate((new_im, np.concatenate(bloques[i:i+n_bloques])), axis=1)
        i += n_bloques
    return np.transpose(new_im)

imagenRecuperada = reconstruir(l)
print(imagenRecuperada)
	
plt.imshow(l, cmap=plt.cm.gray)
plt.xticks([])
plt.yticks([])
plt.show()
"""
"""
print(n)
print(m)
print(n_bloque)
print(k)
"""
