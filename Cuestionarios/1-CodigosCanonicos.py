#!/usr/bin/env python
# coding: utf-8

# # Códigos

# 
# **Dada una codificación $R$, construimos un diccionario para codificar $m2c$ y otro para decodificar $c2m$.**
# 

# In[5]:


R = [('a','0'), ('b','11'), ('c','100'), ('d','1010'), ('e','1011')]

#R = [('ab','0'), ('cb','11'), ('cc','100'), ('da','1010'), ('ae','1011')]


# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in m2c.items()])

print(m2c)

print(c2m)


# 
# **Definir una función** `Encode(M, m2c)` **que, dado un mensaje $M$ y un diccionario 
# de codificación $m2c$, devuelva el mensaje codificado $C$.**
# 

# In[ ]:


def Encode(M, m2c):
    C = ''
    key = ''
    for l in M:
        key = key + l
        if key in m2c:
            C = C + m2c[key]
            key = ''
    return C


# **Definir una función** `Decode(C, m2c)` **que, dado un mensaje codificado $C$ y un diccionario 
# de decodificación $c2m$, devuelva el mensaje original.**

# In[ ]:


def Decode(C,c2m):
    M = ''
    key = ''
    for l in C:
        key = key + l
        if key in c2m:
            M = M + c2m[key]
            key = ''
    return M


# In[5]:


R = [('a','0'), ('b','11'), ('c','100'), ('d','1010'), ('e','1011')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])

M='aabacddeae'
C=Encode(M,m2c)
print(M)
print(m2c)
print(C)
print(c2m)
print(Decode(C,c2m)==M)
print(Encode(M,m2c)=='0011010010101010101101011')


# In[6]:


R = [('a','0'), ('b','10'), ('c','110'), ('d','1110'), ('e','1111')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])

M='aabacddeaeabc'
C=Encode(M,m2c)
print(M)
print(m2c)
print(C)
print(c2m)
print(Decode(C,c2m)==M)
print(Encode(M,m2c)=='0010011011101110111101111010110')


# In[7]:


R = [('ab','0'), ('cb','11'), ('cc','100'), ('da','1010'), ('ae','1011')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in m2c.items()])
M='ababcbccdaae'
C=Encode(M,m2c)
print(M)
print(m2c)
print(C)
print(c2m)

print(Decode(C,c2m)==M)

print(Encode(M,m2c)=='001110010101011')


# In[8]:


#------------------------------------------------------------------------
# Ejemplo 3 (no prefijo)
#------------------------------------------------------------------------
R = [('a','0'), ('b','01'), ('c','011'), ('d','0111'), ('e','1111')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])

''' 
6. Codificar y decodificar los mensajes  'ae' y 'be'. 
Comprobar si los mensajes decodificados coinciden con los originales.
'''



M='ae'
C=Encode(M,m2c)
Mr=Decode(C,c2m)
print(M,Mr,M==Mr)

M='be'
C=Encode(M,m2c)
Mr=Decode(C,c2m)
print(M,Mr,M==Mr)


# # Códigos canónicos
# 
# 
# RFC 1951, sección 3.2.2: https://tools.ietf.org/html/rfc1951#page-7
# 
# 

# 
# **Definir una función** `CodeCanonico(L)` **que, dada una lista de longitudes $L$ y devuelva un código canónico binario cuyas palabras tengan las longitudes de la lista $L$.**

# In[12]:

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
    
# In[27]:


L=[ 3, 3, 3, 3, 2, 4, 7,7,7,5,5,5,4]
#L = [ 3, 3, 3, 3, 3, 2, 4, 4 ]
print(L)
print(CodeCanonico(L))


# In[14]:



L=[7,2,3,3,3,3,26,4,4,4,600]

print(L)
print(CodeCanonico(L))


# # Ejercicio final

# In[20]:

"""
mensaje="The Island of Doctor Moreau, by H. G. Wells [...] The Hyena-swine ran beside me, keeping pace with me and glancing furtively at me out of his feline eyes, and the others came pattering and shouting behind us. The Leopard-man went bursting his way through the long canes, which sprang back as he passed, and rattled in M'ling's face. We others in the rear found a trampled path for us when we reached the brake. The chase lay through the brake for perhaps a quarter of a mile, and then plunged into a dense thicket, which retarded our movements exceedingly, though we went through it in a crowd together,--fronds flicking into our faces, ropy creepers catching us under the chin or gripping our ankles, thorny plants hooking into and tearing cloth and flesh together."
print(mensaje) """


# **Ejemplo**: Símbolos y longitudes de las palabras del código asociadas

# In[17]:

Codificacion_para_estudiantes = [(' ', 3), ("'", 8), (',', 7), ('.', 6), (';', 10), ('B', 10), ('D', 10), ('G', 10), ('H', 7), ('I', 9), ('M', 7), ('T', 7), ('W', 9), ('[', 9), (']', 9), ('a', 4), ('b', 8), ('c', 6), ('d', 4), ('e', 3), ('f', 6), ('g', 5), ('h', 4), ('i', 4), ('l', 5), ('m', 6), ('n', 4), ('o', 5), ('p', 7), ('r', 4), ('s', 5), ('t', 4), ('u', 5), ('v', 8), ('w', 6), ('y', 6)]
print(Codificacion_para_estudiantes)


# **Ejemplo**: Hallo el código

# In[18]:


alfabeto=[i[0] for i in Codificacion_para_estudiantes]
longitudes=[i[1] for i in Codificacion_para_estudiantes]

codigoCanonico=CodeCanonico(longitudes)

R=[(i,j) for i,j in zip(alfabeto, codigoCanonico)]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in m2c.items()])

print(m2c)
print(c2m)

mensajeCodificado = "111101101100010001111110101100110111010010000101000110001110000001111111110110001101111010110001001000111101011000100100101001101011110000001111101111101100011110011101100001111111111110110000111111011001101111011111001000111111100110110110110110110111111101000111101101100011000000111101011111010101110111100010110000011001000101000110111110001110010010001010110000000110011111100100011011101001001100111101101111000101100000100000101110111101100110101000001100100101011011101100011010110110000111101011111010101110111100010110000011001000101000110010010011000000100011000101001100111100010110000110001110000001010011000100011111001101011100101000000100111000111000010001111001111111110000001100100010100011111011001001100000011100000110111101110111100010110000111010110001100001011111000000010010000101000011000101001001010100001100111111001000110111010010111101110111100010110110110000111101101100011110110001110100011000101000011000100000011001011011000110101010011110001011000010101100010110001101001100011001110110000111101111101011000000111111110100101001100110100001111010001100000011011101001110010010001101111001110001101011011101100111100010110000010010000101000111110000100110010111100010110000010010100001010011000111100100010100110100111000110101011001100001010011000100011010100001010011001101101001110001110101010011011110000001110100111101001100001011000111001101011010100100111001000010010000101000010000011100011010100110100111111111000010001101110100100110010111010010110001000101001100100101000001001011101001001111001001010100011110101100010001010101101100011100100110011110110001111101111101100010100110001011110010001100110101001010010001011000110000011100111001110110000111100100100001100100011110111001010100010100110001111001111100000001001000010100010100110001111011000111000101110010101000101101101001111011110100111101111110111101100001111001001000110011010110001111100111110000101010001100101101100011010101001111000101100000100111000101000110010001010011001001010111100000001001000010100001001110001010001100100011101001001000010100110010111100010110000110011100011100100100010100111111001001000111000010010011010011000110010000111100000001001000000110101000010100111011101110101001010100011101001001110111111000000010100110100011001111001011110000010101000101011000000111111000111110010111101000010100110001000011011010101011001110110000111100100100011100011000110101000010100010100110001000100101001111110001111000001000010100111001001100110100010101110110"
mensaje=Decode(mensajeCodificado, c2m)
print(mensaje)
#mensajeCodificado=Encode(mensaje,m2c)

print(mensaje)
print(mensajeCodificado)
print()
print(mensaje==Decode(mensajeCodificado,c2m))


# In[ ]:





