"""
    Campaña electoral
        a) Escribir una función que reciba una tupla con nombres, y para cada nombre imprima
        el mensaje Estimado <nombre>, vote por mí.
        b) Escribir una función que reciba una tupla con nombres, una posición de origen p y una
        cantidad n, e imprima el mensaje anterior para los n nombres que se encuentran a partir
        de la posición p.
        c) Modificar las funciones anteriores para que tengan en cuenta el género del destinatario,
        para ello, deberán recibir una tupla de tuplas, conteniendo el nombre y el género.

"""

def saludar_nombres(tupla):
    # a) Recibe una tupla con nombres e imprime un mensaje "Estimado <nombre>, vote por mí"

    for nombre, genero in tupla:
        if genero == 'M':
            print(f"Estimado {nombre}, vote por mí.")
        else:
            print(f"Estimada {nombre}, vote por mí.")

# saludar_nombres((("Joel","M"),("Sol","F"),("Graciela","F"),("Martin","M")))
# print("-------------------------------------")


def saludar_nombres_b(tupla, p, n):
    # b) Recibe una tupla con nombres, una posición de origen p y una cantidad n, e imprima el mensaje anterior para los n nombres que se encuentran a partir de la posición p

    while p<len(tupla) and n>0:
        if n>0:
            if tupla[p][1] == 'M':
                print(f"Estimado {tupla[p]}, vote por mí.")
            else:
                print(f"Estimada {tupla[p]}, vote por mí.")
        n-=1
        p+=1

saludar_nombres_b((("Joel","M"),("Sol","F"),("Martin","M"),("Graciela","F"),("Belen","F"),("Omar","M")),4,3)
print("--------------------------------")
saludar_nombres_b((("Joel","M"),("Sol","F"),("Martin","M"),("Graciela","F"),("Belen","F"),("Omar","M")),0,4)

