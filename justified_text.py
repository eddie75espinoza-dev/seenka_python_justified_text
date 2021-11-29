
from typing import Tuple


def justified_text(text: str, line_width: int) -> None:
    """
    Function to convert text to justified text.
    text>   myText
    line_width>  line width
    """
    line = round(len(text)/line_width)
    
    # primera linea y justificado
    for num in range(line):
        if num == 0:
            firt_line = text[:line_width] 
            space = firt_line.rfind(' ')         
            myspace = line_width - (space -1)
            text_tup = firt_line.rpartition(" ")            
            count = 1
            for pos, txt in enumerate(text_tup[0]):
                print(txt,end='')
                if txt.isspace():
                    count += 1
                    if count <= myspace:
                        print(' ', end='')
                    else:
                        continue            
                if (pos+1) == space:
                    print()                    
                    
        # lineas siguientes
        if num != 0 and num < line:            
            inter_line = text[space:line_width*num]           
            final_space = inter_line.rfind(' ')
            var_line = inter_line.rpartition(' ')            
            if final_space == -1:  
                space = space + myspace
                print(end='')
            if final_space != 0:
                space = line_width * num
                print(var_line[0])  
                           
            else:
                impression(var_line, space)
                
            
            
        # linea final
        if num == (line-1):
        
            print(text[line_width*num:])

        

def impression(text:Tuple, final_space:int) -> None:                 
    myline = ''.join(text)
    space = myline.rfind(' ') 
    myspace = final_space - line_width            
    contador = 1
    for pos, txt in enumerate(text[0]):
        print(txt,end='')
        if txt.isspace():
            contador += 1
            if contador <= myspace:
                print(' ', end='')
            else:
                continue 
        if pos == space:
            print(end='\n')    
    

if __name__ == '__main__':
    
    #my_text = input('Escriba una Oración: ').strip()
    my_text = "La historia de la ópera tiene una duración relativamente corta dentro del contexto de la historia de la música en general: apareció en 1597, fecha en que se creó la primera ópera."
    
    line_width = int(input("Ingrese un número para el largo de la línea: "))
    
    justified_text(my_text, line_width)
    
        