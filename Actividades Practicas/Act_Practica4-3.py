
# Práctica Zip 1
# Muestra en pantalla frases como la del siguiente ejemplo:

# La capital de Alemania es Berlín

# Utiliza la función zip, loops, y las siguientes listas de países y capitales para resolverlo rápida y eficientemente.

# capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
# paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]


capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinar=list(zip(capitales, paises))

for capitales, paises in combinar:
    print(f"La capital de {paises} es {capitales}")


# Práctica Zip 2
# Crea un objeto zip formado a partir de listas, de un conjunto de marcas y productos que tú prefieras, dentro de la variable mi_zip.

marcas = ["ford","chevrolet","lancia","audi","fiat","volkswagen","IKA"]
productos =["mustang","corvette","delta integrale","S4","125 bialbero","gol power","torino tsx"]

mi_zip=list(zip(marcas, productos))

for marcas, productos in mi_zip:
    print (f"El producto {productos} pertenece a la marca {marcas}")


# Práctica Zip 3
# Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros:

# uno / um / one

# dos / dois / two

# tres / três / three

# cuatro / quatro / four

# cinco / cinco / five

# El resultado deberá seguir la estructura:

# [('uno', 'um', 'one'), ('dos', 'dois', 'two'), ... ]

numeros_espaniol = ['uno','dos','tres','cuatro','cinco'] 
numeros_portugues = ['um','dois','três',"quatro","five"]
numeros_ingles = ['one','two','three','four','five']

numeros=list(zip(numeros_espaniol, numeros_portugues, numeros_ingles))

for numeros_espaniol, numeros_portugues, numeros_ingles in numeros:
    print (numeros)



#-----------------------------------------------------------------------------------------


#lista = [58,96,72,64,35]

#print(f'El menor es {min(lista)} y el mayor es {max(lista)}')

#numeros_espaniol = ['uno','dos','tres','cuatro','cinco'] 

#print(min(numeros_espaniol))

#dic = {'C1':45,'B2':75}

#print(min(dic))


# Práctica Min y Max 1
# Obtén el valor máximo entre los valores de la siguiente lista, y almacénalo en una variable llamada valor_maximo:

lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]

valor_maximo= max(lista_numeros)
print(f"El numero mayor de la lista es {valor_maximo}")


# Práctica Min y Max 2
# Calcula la diferencia entre el valor máximo y el mínimo en la siguiente lista de números, y almacénalo en una variable llamada rango:

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

valor_maximo=max(lista_numeros)
valor_minimo=min(lista_numeros)
rango= valor_maximo - valor_minimo
print(rango)

# Práctica Min y Max 3
# Utilizando max(), min() y métodos de diccionarios, obtén el mínimo valor a partir del siguiente diccionario:

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima=min(diccionario_edades.values())

print(f"La edad minima es {edad_minima}")

ultimo_nombre=max(diccionario_edades.keys())

print(f"El valor que se encuentra ultimo en el orden alfabetico es {ultimo_nombre}")

# Almacena dicho valor en una variable llamada edad_minima.

# También, obtén el nombre que se ubica último en orden alfabético, y almacénalo en una variable llamada ultimo_nombre.





#--------------------------------------------------------------------------------------------------------------



from random import *

#aleatorio = randint(1,50) # un numero aleatorio entre 1 y 50
#print(aleatorio)


#aleatorio = round(uniform(1,50),2) # un numero aleatorio entre 1 y 50
#print(aleatorio)

#aleatorio = random() # un numero aleatorio entre 0 y 1
#print(aleatorio)

#colores= ['azul','rojo','verde','amarillo']
#aleatorio = choice(colores)
#print(aleatorio)

#cartas= list(range(1,12)) 
#shuffle(cartas)
#print(cartas)

# Práctica Random 1
# Implementa la función randint() de la librería random que te permita obtener un número entero del 1 al 10, y almacena dicho valor en una variable llamada aleatorio

from random import *
aleatorio = randint(1,50)
print(f"El valor aleatorio entre 1 y 50 fue: {aleatorio}")

# Práctica Random 2
# Implementa la función random() de la librería random que te permita obtener un número decimal entre 0 y 1, y almacena dicho valor en una variable llamada aleatorio

from random import *
aleatorio = uniform(0,1)
print(f"El valor decimal aleatorio entre 0 y 1 es: {aleatorio}")

# Práctica Random 3
# Utiliza el método choice() de la librería random para obtener un elemento al azar de la lista de nombres a continuación, y almacena el nombre escogido en una variable llamada sorteo.

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
from random import *
sorteo= choice(nombres)
print(f"El nombre aleatorio de la lista es: {sorteo}")

