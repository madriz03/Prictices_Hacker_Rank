
dict = {'ashley': [20,18,14], 'camila':[15,15,17]}

for key in dict:
    suma_valores = sum(dict[key])
    promedio = round(suma_valores / len(dict[key]), 2)
    print("Promedio de notas de ", key, "es:", promedio)
