import statistics

lista = list()

for i in range(3):
    lista.append(float(input("Introduzca un valor : ")))

media = statistics.fmean(lista)
mediana = statistics.median(lista)
varianza = statistics.variance(lista)

print("Lista: ",lista)
print("Media: ", media)
print("Mediana: ", mediana)
print("Varianza: ", varianza)

