# crea una función que acepte un número como entrada. Devuelve una lista nueva que
#  cuente de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento). 
# Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]

def cuentaRegresiva(num):
    lista=[]
    for i in range(num,-1,-1):
        lista.append(i)
    return lista

print(cuentaRegresiva(5))

