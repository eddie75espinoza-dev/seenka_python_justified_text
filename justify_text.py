# -*- coding: utf-8 -*-
"""
Dev: Eddie Espinoza
date: 26/11/2021

Hacer un programa en python que "justifique" un texto con fuente monoespaciada.


⚠️ no usar ninguna librería, solo Python puro



### Input

- Un string de una sola linea
- El ancho de la línea esperada

Ninguna palabra del string será más larga que el ancho de línea esperado.

### Output

Mostrar por standard output el texto justificado, de acuerdo a las siguientes reglas:

- Use espacios para separar las palabras
- Cada línea deberá contener la mayor cantidad de palabras posibles
- Usar \n para separar líneas
- El máximo y el mínimo gap de una misma fila no puede diferir en más de 1 espacio
    - Incorrecto: Lorem-----ipsum--dolor
    - Correcto: Lorem----ipsum---dolor
- Las líneas deberán terminar en una palabra, no un espacio
- '\n' no está incluido en el largo de una línea
- Espacios más largos van primero, luego los espacios más pequeños.
    - Correcto: 'Lorem---ipsum---dolor--sit--amet' (3, 3, 2, 2 espacios).
    - Incorrecto: 'Lorem--ipsum--dolor---sit---amet' (2, 2, 3, 3 espacios).
- La última línea no estará justificada, sólo un espacio entre palabras
- Líneas con una sola palabra larga no necesitan espacios ('unapalabralarga\n').

## Ejemplo:

### Input:

```
La historia de la ópera tiene una duración relativamente corta dentro del contexto de la historia de la música en general: apareció en 1597, fecha en que se creó la primera ópera.
```

Largo de la línea: 30

### Output:

```
La  historia de la ópera tiene
una   duración   relativamente
corta  dentro  del contexto de
la  historia  de  la música en
general   apareció   en  1597,
fecha   en   que  se  creó  la
primera ópera.
```

☝ Notar que todas las líneas, salvo la última, terminan exactamente en la misma columna. Esa es la idea de justificar.

"""
from string import Template
from typing import List

def justifyText(text, large) -> None:
    """
    Function to convert text to justified text
    text>   myText
    large>  line width
    """
    line = round(len(text)/large)
    width = large    
    phrase = ()
    textListLine = []
    # primera linea y justificado
    for num in range(line):
        if num == 0:
            primera = text[:large] 
            space = primera.rfind(' ')
            textMod = text[:space]
            myspace = large - (space - 1)
            otraforma = primera.rpartition(" ")
            #print(otraforma[0]) # tamaño original del texto
            contador = 1
            for pos, txt in enumerate(otraforma[0]):
                print(txt,end='')
                if txt.isspace():
                    contador += 1
                    if contador <= myspace:
                        print(' ', end='')
                    else:
                        continue            
                if (pos+1) == space:
                    print(end='\n')

        # lineas siguientes    
        if num != 0 and num < line:
            large = large *(num+1)
            unaLinea = text[space+1:large] 
            #print(unaLinea)
            space = unaLinea.rfind(" ") 
            #print("space: ", space)
            myspace = width - (space)
            #print("myspace: ", myspace)
            ult_spacio = unaLinea.rpartition(" ")        
            #large, space = space * num, large
            #print(ult_spacio[0], space, myspace)
            imprime_linea(ult_spacio,width,myspace)
                 
    """ if txt == line:
        large += width 
        print(text[large:],+ "txt-1 ", end='\n')

    unaLinea = text[space+1:large]
    otraforma = unaLinea.rpartition(" ")
    print(otraforma[0])
    space = len(otraforma[0])
    large += width
        """

def imprime_linea(interline, width, myspace):
    contador = 0
    print(len(interline[0]))
    for pos, char in enumerate(interline[0]):
        print(char,end='')
        if char.isspace():
            contador += 2
            if contador <= myspace:
                print('_', end='')
            else:
                continue           
        if (pos+1) == width:
            print(end='\n')       
        
    

if __name__ == '__main__':
    
    #mySentence = input('Escriba una Oración: ').strip()
    myText = "La historia de la ópera tiene una duración relativamente corta dentro del contexto de la historia de la música en general: apareció en 1597, fecha en que se creó la primera ópera."
    lineWidth = int(input("Largo de la línea: "))

    #print("Texto original:\n",myText)

    justifyText (myText, lineWidth)
    

"""
for i, char in enumerate(text):
        phrase += char
        if char.isspace() and i == large:
            print(phrase,'\n')
            print("large 1: ",large)
            large += large
        if i == large:
            print(phrase.strip())
            phrase = ""                    
            print("large 2: ",large)
            large = large * 2
        


"""