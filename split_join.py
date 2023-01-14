"""
    Utilizamos 3 metodos de manera didactica
    replace: reemplaza un caracter de un string por otro
    split: Se utilizar para tomar una cadena string separada por el caracter que indiquemos
    y colocar todos los elementos como subcadenas de una lista separados
    join: Se utiliza para unir una lista de cadenas como string separados por el caracter q indiquemos
    Este fue una manera didactica de usar los 3 metodos, si solo queriamos reemplazar los * por espacios
    con replace es suficiente
"""

def split_join(string):
  
    clean = string.replace('*', ' ')
    div = clean.split(' ')
    end = " ".join(div)
    return end

if __name__ == "__main__":
    string = 'Hola*Mundo*este*es*un*string'
    print(split_join(string))


