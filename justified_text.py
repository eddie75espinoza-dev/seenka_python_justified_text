#!/usr/bin/python
"""
Dev: Eddie Espinoza
date: 26/11/2021
modified: 07/01/2022
Hacer un programa en python que "justifique" un texto con fuente monoespaciada.


⚠️ no usar ninguna librería, solo Python puro
"""

def bucle(text):
    large = 0
    cadena = []
    for pos, txt in enumerate(text):
        large += len(txt)
        end = large + pos
        if end <= long:
            cadena.append(txt)
        if end >= long:
            break
    first = " ".join(cadena)

    return first
    
def impression(text):
    myspace = long - len(text)         
    contador = 1
    for pos, txt in enumerate(text):
        print(txt,end='')
        if txt.isspace():
            contador += 1
            if contador <= myspace:
                print(' ', end='')
            else:
                continue 
        long_text = pos + myspace + 1
        if long_text == long:
            print(end='\n')

def justify_text(my_text, long):
    
    line = round(len(my_text)/long)
    for l in range(line+1):
        text = my_text.split()
        cadena = (bucle(text))       
        impression(cadena)
        my_text = my_text[len(cadena)+1:len(my_text)]
    

if __name__ == '__main__':
    
    #my_text = input('Escriba una Oración: ').strip()
    my_text = "La historia de la ópera tiene una duración relativamente corta dentro del contexto de la historia de la música en general: apareció en 1597, fecha en que se creó la primera ópera."
    
    long = int(input("Ingrese un número para el largo de la línea: "))
    
    justify_text(my_text, long)