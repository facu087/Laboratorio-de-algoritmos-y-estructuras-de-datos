# Práctica Métodos y Ayuda 1
# Remueve los caracteres a la izquierda de nuestro texto principal:

# ,

# :

# %

# _

# #

# Utiliza el método lstrip(). Imprime el resultado en pantalla:

print(",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(",:%_#"))

# Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa. Puedes utilizar variables intermedias si las necesitas.



# Práctica Métodos y Ayuda 2
# Añade el elemento "naranja" como el cuarto elemento de la siguiente lista "frutas", utilizando

# el método insert():


frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert (4, "naranja")
print(frutas)

# Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa y cómo es su funcionamiento.


# Práctica Métodos y Ayuda 3
# Verifica si los sets a continuación forman conjuntos aislados (es decir, que no tienen elementos en común), utilizando el método isdisjoint(). Almacena dicho resultado en la variable conjuntos_aislados:


marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados= marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)

# Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa y cómo es su funcionamiento




# Funciones Propias

def mi_funcion():
    '''esta funcion se encarga de 
    imprimir un saludo en pantalla'''
    #print("hola luciano")

mi_funcion()

def mi_funcion(nombre):
    """ esta funcion se encarga de 
    imprimir un saludo en pantalla"""
    #print(f"hola {nombre}")

mi_funcion("luis")


# Práctica Crear Funciones 1
# Declara una función llamada saludar, que cada vez que sea llamada imprima en pantalla "¡Hola mundo!"

# Solo debes definir la función, no debes invocarla luego.

def saludar():
    """esta funcion va a imprimir un ¡Hola Mundo!"""
    print("¡Hola Mundo!")

saludar()




# Práctica Crear Funciones 2
# Declara una función llamada bienvenida, que tome como argumento el nombre de una persona, y que cada vez que sea llamada imprima en pantalla "¡Bienvenido {nombre_persona}!"

# Crea la variable nombre_persona, y almacena dentro de la misma el nombre que prefieras.

# Solo debes definir la función y crear la variable, no debes invocar la función luego.

nombre_persona="Andres Ciro Martinez"
def bienvenida (nombre_persona):
    """esta funcion va a imprimir una frase"""
    print(f"¡Hola {nombre_persona}!")

bienvenida(nombre_persona)




# Práctica Crear Funciones 3
# Declara una función llamada cuadrado, que tome como argumento un número cualquiera, y que cada vez que sea llamada, imprima en pantalla el cuadrado de dicho número (es decir, la potencia 2 del valor).

# El nombre del argumento que debe tomar dicha función es un_numero. Crea dicha variable y asígnale un número cualquiera.

# Solo debes definir la función y crear la variable, no debes invocar la función luego.


un_numero=5

def cuadrado (un_numero):
    total = un_numero**2
    print(f"El resultado es: {total}")

cuadrado(un_numero)

# Return 

def multiplicar(numero1,numero2):
    total = numero1 * numero2
    return total

resultado = multiplicar(5,200)
print(resultado)


# Práctica Return 1
# Crea una función llamada potencia que tome dos valores numéricos como argumentos. Deberá devolver el número que resulte de resolver una potencia, utilizando el primer número como base, y el segundo como exponente:



def potencia(numero1, numero2):
    return[numero1**numero2]    

resultado=potencia(5,2)
print(resultado)



# Práctica Return 2
# Crea una función llamada usd_a_eur que tome como único parámetro un valor numérico (un monto en dólares estadounidenses), y devuelva como resultado el monto equivalente en euros. A fines de este ejemplo, tomaremos la conversión 1 USD = 0.90 EUR.

# Crea una variable llamada dolares y almacena en ella un monto cualquiera para entregárselo a tu función y evaluar su resultado.

# Pista: para realizar la conversión, la función internamente debe multiplicar este valor en dólares por 0.90 para obtener el monto equivalente en euros.


def usd_a_eur(dolar):
    cambio = dolar * 0.90
    return cambio

dolar=int(input("Ingrese un monto para cambiarlo a Euro: "))
resultado=usd_a_eur(dolar)

print(f"El monto {dolar} en dolares son {resultado} en euros")




# Práctica Return 3
# Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como argumento, invierta el orden de sus caracteres y los devuelva de ese modo y en mayúsculas.

# Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: "NOHTYP"

# También, deberás crear una variable llamada palabra, que contenga el string que tú prefieras, para sumisitrarle como argumento a la función creada.

# Pista: dentro de la función creada, deberás utilizar métodos de strings ya vistos.


palabra="Argentina"

def invertir_palabra(palabra):
    invertido=(palabra[::-1])
    return invertido

resultado=invertir_palabra(palabra)
print (resultado.upper())




def chequear_3_cifras(lista):
    lista_3_cifras =[]
    for n in lista:
        if n == range(100,1000):
            lista_3_cifras.append(n)
        else:
            continue
    return lista_3_cifras

resultado = chequear_3_cifras([555,99,600])
print(resultado)


# Práctica Funciones Dinámicas 1
# Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva True si todos los valores de una lista son positivos, y False si al menos uno de los valores es negativo. Crea una lista llamada lista_numeros con valores positivos y negativos.

# No invoques la función, solo es necesario definirla.

lista_numeros=[20, -40, 50, 60]

def todos_positivos(lista):
    for num in lista_numeros:
        if num <=0:
            return False
    return True


print (todos_positivos(lista_numeros))


# Práctica Funciones Dinámicas 2
# Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.

lista_numeros=[20, 40, 120]

def suma_numeros(lista):
    suma=0
    for num in lista:
        if num>0 and num<100:
           suma+=num
    return suma
        
print(suma_numeros(lista_numeros))




# Práctica Funciones Dinámicas 3
# Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.


lista_numeros=[30, 20, 23, 5, 15]

def cantidad_pares(lista):
    suma=0
    for num in lista:
        if num%2==0:
            suma+=num
    return suma

print (cantidad_pares(lista_numeros))


precios_cafe = [("capuchino",1.5), ("Expresso",2.5), ("Moka",3.5)]

def cafe_mas_caro(lista_precios):

    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio_mayor
            cafe_mas_caro = cafe
        else:
            pass
    return(cafe_mas_caro,precio_mayor)

cafe, precio = cafe_mas_caro(precios_cafe)
print(f"El cafe mas caro es {cafe} cuyo precio es {precio}")
