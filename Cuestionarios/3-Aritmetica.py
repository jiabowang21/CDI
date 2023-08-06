# -*- coding: utf-8 -*-
"""
@author: martinez
Jordi Armengol, Bruno Tamborero.
"""

import math
# ¿Se tenía que usar random? Estaba importado en el enunciado
# import random

from itertools import accumulate



#%%
"""
Dado un mensaje y su alfabeto con sus frecuencias dar el código 
que representa el mensaje utilizando precisión infinita (reescalado)
El intervalo de trabajo será: [0,R), R=2**k, k menor entero tal que R>4T
T: suma total de frecuencias
"""

# Basado en https://people.cs.nctu.edu.tw/~cmliu/Courses/Compression/chap4.pdf

def bitfield(n):
    return [int(digit) for digit in bin(n)[2:]]

def bitfield_to_dec(bit_array):
    dec = 0
    for i in range(len(bit_array)):
        dec += bit_array[-(i+1)] * 2**i
    return dec

# Most significant bit equal
def equal_msb(a, b):
    return a[0] == b[0]

def get_bitfields_lower_upper(lower_bound, upper_bound, nbits):
    lower = bitfield(lower_bound)
    upper = bitfield(upper_bound)
    return (nbits-len(lower))*[0] + lower, (nbits-len(upper))*[0] + upper # para que tengan nbits

def shift_left_and_set_lsb(bfield, bit):
    length = len(bfield)
    for i in range(1, len(bfield)):
        bfield[i-1] = bfield[i]
    bfield[length-1] = bit
    return bfield

def e3(lower, upper):
    return lower[0:2] == [0, 1] and upper[0:2] == [1, 0]

def IntegerArithmeticCode(mensaje,alfabeto,frecuencias):
    codigo = ''
    T = sum(frecuencias)
    acumuladas = [0] + list(accumulate(frecuencias))
    indices = dict(zip(alfabeto,range(len(frecuencias))))
    k = int(math.log2(4*T)) + 1
    R = 2**k
    lower, upper = get_bitfields_lower_upper(0, R-1, k)
    e3_counter  = 0
    for c in mensaje:
        decimal_lower_bound = bitfield_to_dec(lower)
        decimal_upper_bound = bitfield_to_dec(upper)
        indice = indices[c]
        lower_c = acumuladas[indice]
        upper_c = acumuladas[indice+1]
        new_lower = decimal_lower_bound + ((decimal_upper_bound-decimal_lower_bound+1)*lower_c)//T
        new_upper = decimal_lower_bound + ((decimal_upper_bound-decimal_lower_bound+1)*upper_c)//T - 1
        lower, upper = get_bitfields_lower_upper(new_lower, new_upper, k)
        while equal_msb(lower, upper) or e3(lower, upper):
            if equal_msb(lower, upper): # escalado e1, e2
                b = lower[0]
                codigo += str(b) + e3_counter * str(1-b) # send b (+ los esperados por e3)
                lower = shift_left_and_set_lsb(lower, 0)
                upper = shift_left_and_set_lsb(upper, 1)
                e3_counter = 0
            if e3(lower, upper): # escalado e3
                lower = shift_left_and_set_lsb(lower, 0)
                upper = shift_left_and_set_lsb(upper, 1)
                # complement
                lower[0] = 1-lower[0]
                upper[0] = 1-upper[0]
                e3_counter += 1
    for e in lower:
        codigo += str(e) + e3_counter * str(1-e)
        if e3_counter > 0:
            e3_counter = 0
    return codigo

    
    
#%%
            
            
"""
Dada la representación binaria del número que representa un mensaje, la
longitud del mensaje y el alfabeto con sus frecuencias 
dar el mensaje original
"""
           
def IntegerArithmeticDecode(codigo,tamanyo_mensaje,alfabeto,frecuencias):
    mensaje = ''
    T = sum(frecuencias)
    k = int(math.log2(4*T)) + 1
    R = 2**k
    acumuladas = list(accumulate(frecuencias))
    lower = [0]*k
    upper = [1]*k
    c_k = k
    t = []
    for i in range(c_k):
        t.append(int(codigo[i]))
    while len(mensaje) < tamanyo_mensaje:
        decimal_t = bitfield_to_dec(t)
        decimal_lower_bound = bitfield_to_dec(lower)
        decimal_upper_bound = bitfield_to_dec(upper)
        j = 0
        frec_acum = int(((decimal_t-decimal_lower_bound+1)*T-1)/(decimal_upper_bound-decimal_lower_bound+1))
        while acumuladas[j] <= frec_acum:
            j += 1
        mensaje += alfabeto[j]
        lower_c = 0 if j <= 0 else acumuladas[j-1]
        upper_c = acumuladas[j]
        new_lower = decimal_lower_bound + ((decimal_upper_bound-decimal_lower_bound+1)*lower_c)//T
        new_upper = decimal_lower_bound + ((decimal_upper_bound-decimal_lower_bound+1)*upper_c)//T - 1
        lower, upper = get_bitfields_lower_upper(new_lower, new_upper, k)
        while equal_msb(lower, upper) or e3(lower, upper):
            if equal_msb(lower, upper):
                lower = shift_left_and_set_lsb(lower, 0)
                upper = shift_left_and_set_lsb(upper, 1)
                t = shift_left_and_set_lsb(t, int(codigo[c_k]))
                c_k += 1
            if e3(lower, upper):
                lower = shift_left_and_set_lsb(lower, 0)
                upper = shift_left_and_set_lsb(upper, 1)
                t = shift_left_and_set_lsb(t, int(codigo[c_k]))
                c_k += 1
                # complement
                lower[0] = 1-lower[0]
                upper[0] = 1-upper[0]
                t[0] = 1-t[0]
    return mensaje


    


             
            
#%%
       




#%%
'''
Definir una función que codifique un mensaje utilizando codificación aritmética con precisión infinita
obtenido a partir de las frecuencias de los caracteres del mensaje.
Definir otra función que decodifique los mensajes codificados con la función 
anterior.
'''


def EncodeArithmetic(mensaje_a_codificar):
    fuente = {}
    for c in mensaje_a_codificar:
        if c not in fuente:
            fuente[c] = 1
        else:
            fuente[c] += 1
    alfabeto, frecuencias = list(fuente.keys()), list(fuente.values())
    mensaje_codificado = IntegerArithmeticCode(mensaje_a_codificar, alfabeto, frecuencias)
    return mensaje_codificado,alfabeto,frecuencias
    
def DecodeArithmetic(mensaje_codificado,tamanyo_mensaje,alfabeto,frecuencias):
    mensaje_decodificado = IntegerArithmeticDecode(mensaje_codificado,tamanyo_mensaje,alfabeto,frecuencias)
    return mensaje_decodificado
        
#%%
'''
Ejemplo (!El mismo mensaje se puede codificar con varios códigos¡)
'''
"""
C='0011101101100100111010011001001001101100010011110111111101101001011111011001000110000100111101000101001010111110001111001001001010010111101100001100101000100101001000110101001011000010011110010100011100110101000111011011010110111000101101000110011111110010011111110001001001100101011000100111011000111011010110010110111111110000100000100101000101011110100100111101101001110101010011101100000001110000001010010100010011000001100110111100100111000000111101010100000001101011011111111011100011001010101001111011000110110011011100101110010000001100001000111011000110000101100111110100011001001000001011001101111010101111110001110110101011101011101101100000110001010101110110000010010110100010001010010110001010010111011001101110110010101110001001001000100100110111010101001000010100010000110110000111101100111101010000111000111101011010001111011010000110111101000100100000011001011100000000110110110110001000100000111111100000001001001001001001010111011010100001110001000100000000010011111011110110011110'
alfabeto = [' ', ',', '.', 'D', 'G', 'H', 'I', 'M', 'T', 'W', '[', ']', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'y']
frecuencias = [70, 5, 9, 1, 1, 1, 3, 1, 2, 1, 1, 1, 27, 4, 10, 8, 40, 9, 5, 14, 14, 2, 12, 10, 22, 27, 4, 25, 19, 30, 7, 1, 4, 6]
#mensaje='dddcabccacabadac'
#tamanyo_mensaje=len(mensaje)  

#for C in lista_C:
mensaje_recuperado=DecodeArithmetic(C,396,alfabeto,frecuencias)
print(mensaje_recuperado)
"""


#%%

'''
Ejemplo
'''

print('\n\n\n\n\n')
alfabeto=[' ', '!', ',', '.', 'A', 'B', 'D', 'F', 'G', 'H', 'I', 'L', 'M', 'P', 'T', 'W', '[', ']', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y']
frecuencias=[77, 1, 3, 11, 1, 2, 1, 1, 1, 2, 4, 1, 3, 1, 4, 3, 1, 1, 26, 4, 7, 10, 33, 10, 6, 19, 18, 4, 11, 5, 19, 27, 2, 11, 14, 25, 6, 5, 6]
longitud = 386
mensaje='The Island of Doctor Moreau, by H. G. Wells. [...] The Man with the Bandaged Arm speaks a strange thing, said one of the Beast Folk. I tell you it is so, I said. The Master and the House of Pain will come again. Woe be to him who breaks the Law! They looked curiously at one another. With an affectation of indifference I began to chop idly at the ground in front of me with my hatchet.'
codigo = IntegerArithmeticCode(mensaje, alfabeto, frecuencias)

print('\n')
print(codigo[0:1000])
print('\n')
print(IntegerArithmeticDecode(codigo, longitud, alfabeto, frecuencias) == mensaje)
