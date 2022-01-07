#!/usr/bin/python
"""
Dev: Eddie Espinoza
date: 26/11/2021
modified: 07/01/2022
Hacer un programa en python que "justifique" un texto con fuente monoespaciada.


⚠️ no usar ninguna librería, solo Python puro

output:
Enter a number for the length of the line: 49
La  historia  de  la  ópera  tiene  una duración
relativamente  corta  dentro  del contexto de la
historia  de  la  música en general: apareció en
1597,  fecha  en  que  se creó la primera ópera.

"""

def bucle(text):
    """
    Obtiene un sub string
    """
    large = 0
    chain = []
    for pos, txt in enumerate(text):
        large += len(txt)
        end = large + pos
        if end <= long:
            chain.append(txt)
        if end >= long: #evita recorrer todo el texto
            break
    sub_string = " ".join(chain)

    return sub_string
    
def impression(text):
    """
    agrega espacios al sub string y ejecuta la impresion
    """
    myspace = long - len(text)         
    count = 1
    for pos, txt in enumerate(text):
        print(txt,end='')
        if txt.isspace():
            count += 1
            if count <= myspace:
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
        chain = (bucle(text))       
        impression(chain)
        my_text = my_text[len(chain)+1:len(my_text)]
    

if __name__ == '__main__':
    
    my_text = "La historia de la ópera tiene una duración relativamente corta dentro del contexto de la historia de la música en general: apareció en 1597, fecha en que se creó la primera ópera."
    
    long = int(input("Enter a number for the length of the line: "))
    
    justify_text(my_text, long)