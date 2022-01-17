#crea una función que acepte una lista y devuelva la suma del
#  primer valor de la lista, más la longitud de la lista.
#jemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 
# 6 (primer valor: 1 +length: 5)

def primero_mas_longitud(lista):
    return(lista[0]+len(lista))

print(primero_mas_longitud([1,2,3,4,5]))