#Primero: ¿cuántas veces aparece cada una de las letras que eligió? Para lograr esto, te  recomiendo almacenar esas letras en una lista y luego usar algún método propio de string  que nos permita contar cuantas veces aparece un sub string dentro del string. Algo que  debes tener en cuenta es que al buscar las letras pueden haber mayúsculas y minúsculas  y esto va a afectar el resultado. Lo que deberías hacer para asegurarte de que se  encuentren absolutamente todas las letras es pasar, tanto el texto original como las  letras a buscar, a minúsculas.  

texto =input ("Inserte aqui un texto de cualquier indole, puede ser un articulo, parrafo, frase, poema, etc: ")
texto_minus=texto.lower()
lista_info_letras= input ("Elija 3 letras de su interes para saber cuantas veces aparece en su texto (Escribalas con una coma seguido de un espacio): ")

letras_elegidas=lista_info_letras.split(", ")

print (f"Sus 3 letra elegidas son : {letras_elegidas}")

for letra in letras_elegidas:
    cantidad = texto_minus.count(letra)
    print(f"La letra '{letra}' aparece {cantidad} veces en el texto.")

#Segundo: le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto. Y  para lograr esta parte, recuerda que hay un método de string que permite transformarlo  en una lista y que luego hay una función que permite averiguar el largo de una lista.  

palabras=texto_minus.split()
cantida_de_palabras=len(palabras)
print (f"El texto que escogiste tiene {cantida_de_palabras} palabras!")

#Tercero: nos va a informar cuál es la primera letra del texto y cuál es la última. Aquí  claramente echaremos mano de la indexación.  

primer_palabra=(palabras[0])
print(f"La primer palabra del texto es '{primer_palabra}'")       

ultima_palabra=(palabras[-1])
print(f"La ultima palabra del texto es '{ultima_palabra}'")

#Cuarto: el sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de  las palabras. ¿Acaso hay algún método que permita invertir el orden de una lista, y otro  que permita unir esos elementos con espacios intermedios? Piénsalo.  

texto_invertido=(texto[::-1])
print (f"Su texto invertido quedaria de esta manera: {texto_invertido}")

letras_elegidas.reverse()
print (letras_elegidas)

lista_unida=" ".join(letras_elegidas)
print(lista_unida)

#Y por último: el sistema nos va a decir si la palabra “Python” se encuentra dentro del  texto. Esta parte puede ser algo complicada de imaginársela, pero te voy a dar una pista:  puedes usar booleanos para hacer tu averiguación y un diccionario para encontrar la  manera de expresarle al usuario tu respuesta

palabra = "python"
if palabra in texto_minus:
    print(f"La palabra {palabra} se encuentra en el texto.")
else:
    print(f"La palabra {palabra} no se encuentra en el texto")

