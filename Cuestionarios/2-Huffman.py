#!/usr/bin/env python
# coding: utf-8

# In[20]:



import time
import random
import itertools
import heapq


# **Definir una función** `LongitudMedia(C,p)` **que dado un código $C$ y una distribución de probabilidades $p$ devuelva la longitud media $\tilde l$ del código**.

# In[2]:

def CodeCanonico(L):
    codigo_binario = []
    maxi = max(L) + 1
    bl_count = [0]*maxi
    for n in L:
        bl_count[n] = bl_count[n] + 1
    code = 0
    bl_count[0] = 0
    next_code = [0]*maxi
    for bits in range(1, maxi): 
        code = code + bl_count[bits - 1] << 1
        next_code[bits] = code
    for n in range(len(L)):
        leng = L[n]
        if leng != 0:
            codigo_binario.append(bin(next_code[leng])[2:])
            next_code[leng] += 1
    i = 0
    for w in codigo_binario:
        corregido = ''
        l = len(w)
        while l < L[i]:
            corregido += '0'
            l += 1
        codigo_binario[i] = corregido + w
        i += 1
    return codigo_binario

def LongitudMedia(C,p):
    l = 0.0
    indice = 0
    for i in C:
        l += len(i) * p[indice]
        indice += 1
    return l 

# **Definir una función** `Huffman(p)` **que dada una distribución de probabilidades $p$ devuelva** ***UN*** **código de Huffman asociado a dicha la distribución de probabilidades**.

def descompose(tree, depth, info):
	if type(tree[0]) == int:
		info[tree[0]] = depth
	else:
		descompose(tree[0], depth + 1, info)
	if type(tree[1]) == int:
		info[tree[1]] = depth
	else:
		descompose(tree[1], depth + 1, info)

# In[80]:

def Huffman(p,debug=False):
    diccionario = {}
    for i in range(len(p)):
    	diccionario[i] = p[i]

    cola = []

    for key in diccionario:
    	heapq.heappush(cola, (diccionario[key], key))

    while len(cola) > 1:
    	min1 = heapq.heappop(cola)
    	min2 = heapq.heappop(cola)
    	heapq.heappush(cola, (min1[0] + min2[0], [min1[1], min2[1]]))

    tree = cola[0][1]
    depth = 1

    info = {}
    print(info)
    descompose(tree, 1, info)

    longitudes_palabras = []

    for key in info:
    	longitudes_palabras.append(info[key])

    return CodeCanonico(longitudes_palabras)

# ### Ejemplos

# In[17]:

'''
p = [0.0018, 0.7097, 0.0026, 0.005, 0.0336, 0.0166, 0.0362, 0.0282, 0.0126, 0.0139, 0.0267, 0.0317, 0.0256, 0.0332, 0.0226]
codigo = Huffman(p)
#codigo = ['011', '1000', '101001', '001', '010011', '1101', '010010', '10100011', '11001', '01000', '10100010', '11000', '10101', '1011', '1111', '1110', '000', '1010000', '0101', '1001']
print(p)
print([[p[i],codigo[i]] for i in range(len(p))], '\n Longitud Media:',LongitudMedia(codigo,p))

codigo_ejercicio = ['100011', '1100', '1010', '001', '011', '1001', '1110', '1111', '10000', '1011', '000', '100010', '0101', '1101', '0100']
#codigo = ['011', '1000', '101001', '001', '010011', '1101', '010010', '10100011', '11001', '01000', '10100010', '11000', '10101', '1011', '1111', '1110', '000', '1010000', '0101', '1001']
print('longitud ejercicio')
print(LongitudMedia(codigo_ejercicio,p))
'''


# In[43]:

'''
p=[0.8,0.1,0.05,0.05]
codigo=Huffman(p)
print(p)
print([[p[i],codigo[i]] for i in range(len(p))], '\n Longitud Media:',LongitudMedia(codigo,p))


# In[44]:


p=[0.5,0.25,0.1,0.05,0.05,0.05]
codigo=Huffman(p)
print(p)
print([[p[i],codigo[i]] for i in range(len(p))], '\n Longitud Media:',LongitudMedia(codigo,p))


# In[45]:


p=[0.102, 0.106, 0.053, 0.114, 0.0081, 0.106, 0.0088, 0.030, 0.056, 0.055, 0.032, 0.094, 0.0075, 0.078, 0.1496]
codigo=Huffman(p)
print(p)
print([[p[i],codigo[i]] for i in range(len(p))], '\n Longitud Media:',LongitudMedia(codigo,p))


# In[52]:


n=2**7
p=[1/n for _ in range(n)]

codigo=Huffman(p)

print(p)

print(codigo, '\n Longitud Media:',LongitudMedia(codigo,p))

'''
# **Definir una función** `tablaFrecuencias(mensaje, numero_de_simbolos=1)` **que dado un mensaje $M$ devuelva una tabla con la frecuencia de cada tupla de** `numero_de_simbolos` **símbolos del mensaje**.

# In[55]:

def tablaFrecuencias(mensaje,numero_de_simbolos = 1):
	print(numero_de_simbolos)
	n = numero_de_simbolos
	w = ''
	dictionary = {}
	for c in mensaje:
		w += c
		n -= 1
		if n == 0:
			if w in dictionary:
				dictionary[w] += 1
			else:
				dictionary[w] = 1
			w = ''
			n = numero_de_simbolos

	frecuencias = []

	for key in dictionary:
		frecuencias.append([key, dictionary[key]])

	frecuencias.sort()
	
	return frecuencias


# ### Ejemplos de como cambian las frecuencias según la _fuente_ $S$

# In[58]:


mensaje= "The Island of Doctor Moreau, by H. G. Wells. [...] I got up and sat down before the food. I had a heavy feeling in my head, and only the vaguest memory at first of the things that had happened over night. The morning breeze blew very pleasantly through the unglazed window, and that and the food contributed to the sense of animal comfort which I experienced. Presently the door behind me--the door inward towards the yard of the enclosure--opened. I turned and saw Montgomery's face. All right, said he. I'm frightfully busy. And he shut the door. Afterwards I discovered that he forgot to re-lock it. Then I recalled the expression of his face the previous night, and with that the memory of all I had experienced reconstructed itself before me. Even as that fear came back to me came a cry from within; but this time it was not the cry of a puma."

nnn=1
print(tablaFrecuencias(mensaje,numero_de_simbolos=nnn))
tabla = tablaFrecuencias(mensaje,numero_de_simbolos=nnn)
p = []
total = len(mensaje) - 0.0
for i in range (len(tabla)):
	p.append(tabla[i][1]/total)
codigo = Huffman(p)
#codigo = ['011', '1000', '101001', '001', '010011', '1101', '010010', '10100011', '11001', '01000', '10100010', '11000', '10101', '1011', '1111', '1110', '000', '1010000', '0101', '1001']
print([[codigo[i]] for i in range(len(p))], '\n Longitud Media:',LongitudMedia(codigo,p))

codigo_ejercicio = ['000', '11110100', '111111000', '1110110', '110010', '111111001', '11110101', '111111010', '11110110', '111111011', '111111100', '1110111', '111111101', '11110111', '11111000', '11111001', '111111110', '1111000', '0100', '110011', '110100', '10100', '001', '10101', '110101', '0101', '10110', '111111111', '10111', '110110', '0110', '0111', '110111', '1000', '11000', '1001', '111000', '1111001', '111001', '11111010', '111010', '11111011']
print('pp')
print(LongitudMedia(codigo_ejercicio, p))
# In[62]:

'''
mensaje='La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por un instinto de prudencia y armonía que modificaba las vulgares exageraciones de esta arquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequeña, y sobre ésta una cruz de hierro que acababa en pararrayos.'

nnn=2
print(tablaFrecuencias(mensaje,numero_de_simbolos=nnn))


# ---
# **Definir una función** `EncodeHuffman(mensaje,numero_de_simbolos=n_simbolos)` **que codifique un mensaje utilizando un código de Huffman 
# obtenido a partir de las frecuencias de los caracteres del mensaje.**
# 

# Codifico un mensaje de prueba tomando las frecuencias de cada símbolo.  
# 
# Hago una estimación de la ratio de compresión sin contar que he de almacenar el diccionario y contándolo.
# 
# Los tiempos dependerán del entorno de ejecución.

# In[66]:



mensaje='La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por un instinto de prudencia y armonía que modificaba las vulgares exageraciones de esta arquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequeña, y sobre ésta una cruz de hierro que acababa en pararrayos.'

mensaje=mensaje[:]*100
n_simbolos=1

mensaje_codificado, m2c,len_M=EncodeHuffman(mensaje,numero_de_simbolos=n_simbolos)
mensaje_recuperado=DecodeHuffman(mensaje_codificado,m2c,len_M)

print('\n Diccionario ordenado alfabéticamente: ', sorted(m2c.items(), key=lambda x: x[0]))
print('\n Diccionario ordenado longitud código: ', sorted(m2c.items(), key=lambda x: len(x[1])))
ratio_compresion=8*len(mensaje)/len(mensaje_codificado)
ratio_compresion_con_diccionario=8*len(mensaje)/(len(mensaje_codificado)+len(m2c)*8*(n_simbolos+1))
print('\n Ratio de compresión: ', ratio_compresion ,8*len(mensaje),"-->",len(mensaje_codificado))
print('\n Ratio de compresión estimada con diccionario: ', ratio_compresion_con_diccionario,8*len(mensaje),"-->",len(mensaje_codificado)+len(m2c)*16)
if (mensaje!=mensaje_recuperado):
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

print('\n Diccionario a guardar: ',[[x[0],len(x[1])] for x in m2c.items() ])


# ### Codifico _La Regenta_ 
# Uso como fuente los símbolos del texto.

# In[71]:


n_simbolos=1

with open ("../standard_test_text/la_regenta_utf8", "r") as myfile:
    mensaje=myfile.read()
t0=time.time()    
mensaje_codificado, m2c,len_M=EncodeHuffman(mensaje,numero_de_simbolos=n_simbolos)
t_encode=time.time()-t0
print('--------------------------------------------------------------------------------')
print('\n Diccionario ordenado alfabéticamente: ', sorted(m2c.items(), key=lambda x: x[0]))
print('\n Diccionario ordenado longitud código: ', sorted(m2c.items(), key=lambda x: len(x[1])))
ratio_compresion=8*len(mensaje)/len(mensaje_codificado)
ratio_compresion_con_diccionario=8*len(mensaje)/(len(mensaje_codificado)+len(m2c)*8*(n_simbolos+1))
print('\n Ratio de compresión: ', ratio_compresion ,8*len(mensaje),"-->",len(mensaje_codificado),'(bits)')
print('\n Ratio de compresión estimada con diccionario: ', ratio_compresion_con_diccionario,8*len(mensaje),"-->",len(mensaje_codificado)+len(m2c)*8*(n_simbolos+1),'(bits)')

print('\n Tamaño Huffman     :',int((len(mensaje_codificado)+len(m2c)*8*(n_simbolos+1))/8),'bytes')
print('\n Tamaño Fichero .bz2: 518588 bytes')
print('\n Tamaño Fichero .zip: 678394 bytes')
print('\n Tamaño Fichero  .gz: 710464 bytes')


t0=time.time()
mensaje_recuperado=DecodeHuffman(mensaje_codificado,m2c,len_M)
t_decode=time.time()-t0
print("\n Tiempo Encode (Tabla frecuencias+Código Huffman+Codificación):", t_encode)
print("\n Tiempo Decode:", t_decode)
if (mensaje!=mensaje_recuperado):
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


# **Hago distintas pruebas  para ver como varía la ratio de compresión según el número de símbolos de la fuente tomados para calcular las frecuencias**

# In[79]:


with open ("../standard_test_text/la_regenta_utf8", "r") as myfile:
    mensaje=myfile.read()


for n_simbolos in range(1,5):
    
    print('\n\n--------------------------------------------------------------------------------')
    print(' Codifico usando una fuente que toma '+str(n_simbolos)+ ' símbolos consecutivos')
    print('--------------------------------------------------------------------------------')

    t0=time.time()    
    mensaje_codificado, m2c,len_M=EncodeHuffman(mensaje,numero_de_simbolos=n_simbolos)
    t_encode=time.time()-t0
    ratio_compresion=8*len(mensaje)/len(mensaje_codificado)
    ratio_compresion_con_diccionario=8*len(mensaje)/(len(mensaje_codificado)+len(m2c)*8*(n_simbolos+1))
    print('\n Ratio de compresión: ', ratio_compresion ,8*len(mensaje),"-->",len(mensaje_codificado),'(bits)')
    print('\n Ratio de compresión estimada con diccionario: ', ratio_compresion_con_diccionario,8*len(mensaje),"-->",len(mensaje_codificado)+len(m2c)*8*(n_simbolos+1),'(bits)')

    print('\n Tamaño Huffman     :',int((len(mensaje_codificado)+len(m2c)*8*(n_simbolos+1))/8),'bytes')
    print('\n Tamaño Fichero .bz2: 518588 bytes')
    print('\n Tamaño Fichero .zip: 678394 bytes')
    print('\n Tamaño Fichero  .gz: 710464 bytes')

    t0=time.time()
    mensaje_recuperado=DecodeHuffman(mensaje_codificado,m2c,len_M)
    t_decode=time.time()-t0
    print("\n Tiempo Encode (Tabla frecuencias+Código Huffman+Codificación):", t_encode)
    print("\n Tiempo Decode:", t_decode)
    if (mensaje!=mensaje_recuperado):
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

'''
# In[ ]:




