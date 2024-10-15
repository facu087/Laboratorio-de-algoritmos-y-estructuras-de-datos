
#Creacion de la lista
lista_estudiantes=[]

#Validacion
while True:
    #Ingreso de datos
    nombres=input("Ingrese los nombres de los estudiantes. Cuando finalice ingrese la palabra FIN. Si desea ver los nombres ingresados hasta el momento, escriba REPETIR: ")
    #Condicion para que termine la lista si la palabra ingresada es "fin"(ya sea en minuscula o mayuscula)
    nombres=nombres.lower().strip()
    if nombres=="fin":
        break
    #Condicion para que muestre los datos ingresados hasta el momento si se ingresa "repetir"(ya sea minuscula o mayuscula)
    elif nombres=="repetir":
        if lista_estudiantes:
            print("Los nombres que ingresó hasta el momento son: ")
            for nombre in lista_estudiantes:
                print(nombre)
        #Sino ocurre ninguna de las anteriores se muestra que no se ingreso ningun dato
        else:
            print("No se ha ingresado ningun nombre.")
    else:
        #Revisamos que los datos sean validos
        if nombres and all(nombres.isalpha() or nombres.isspace() for nombres in nombres):
            lista_estudiantes.append(nombres)
        else:
            print("El nombre ingresado es invalido. Recuerda que no puede estar vacio, ni ser un numero, ni un simbolo")
print("\nIngreso finalizado. Estos son los nombres ingresados: ")
for nombre in lista_estudiantes:
    print(nombre)




while True:
    print("\nMenu de opciones")
    print("1. Mostrar nombres ingresados")
    print("2. Ordenar los nombres")
    print("3. Analisis de longitud de los nombres")
    print("4. Contar vocales y consonantes")
    print("5. Contar palabras en cada nombres")
    print("6. Inversion de nombres")
    print("7. Mostrar solo los nombres que empiezan con una letra en particular")
    print("8. Buscar si un nombre esta en la lista")
    print("9. Finalizar")

    opcion_elegida=input("Elige la opcion que quieras realizar: ")

    #Mostrar nombres ingresados
    if opcion_elegida=="1":
        print("Nombres ingresados: ")
        for nombre in lista_estudiantes:
            print(nombre)
    

    #Ordenar los nombres
    elif opcion_elegida=="2":
        lista_estudiantes.sort()
        print("Nombres ordenados alfabeticamente: ")
        for nombres in lista_estudiantes:
            print (nombres)

    
    #Analisis de longitud de los nombres
    elif opcion_elegida=="3":
        nombre_mas_corto=min(lista_estudiantes, key=len)
        nombre_mas_largo=max(lista_estudiantes, key=len)
        print(f"El nombre mas largo de la lista es: {nombre_mas_largo}")
        print(f"El nombre mas corto de la lista es: {nombre_mas_corto}")

   
   #Contar vocales y consonantes
    elif opcion_elegida=="4":
            vocales=("aeiouAEIOU")
            consonantes=("bcdfghjklmnpqrstvwxyzBCDFGHJKLNPQRSTVWXYZ")
            total_vocales=0
            total_consonantes=0
            for nombre in lista_estudiantes:
                for letra in nombre:
                    if letra in vocales:
                        total_vocales=total_vocales+1
                    elif letra in consonantes:
                        total_consonantes=total_consonantes+1
            print(f"El  total de vocales es: {total_vocales}")
            print(f"El  total de consonantes es: {total_consonantes}")

    
    #Contar palabras en cada nombres
    elif opcion_elegida=="5":
        for nombre in lista_estudiantes:
            cantidad_nombre=(len(nombre.split()))
            print(f"El nombre {nombre} esta compuesto por {cantidad_nombre} palabras")


    #Inversion de nombres
    elif opcion_elegida=="6":
        for nombre in lista_estudiantes:
            print(f"El nombre invertido de {nombre} es: {nombre[::-1]}")
            

    #Mostrar solo los nombres que empiezan con una letra en particular
    elif opcion_elegida=="7":
        letra=input("Ingrese una letra para mostrar los nombres que aparecen con ella: ").lower()
        nombres_letra=[nombre for nombre in lista_estudiantes if nombre.lower().startswith(letra)]
        if nombres_letra:
            print(f"Los nombres que comienzan con la letra '{letra}' son:")
            for nombre in nombres_letra:
                print(nombre)
        else:
                print(f"No hay ningun nombre que comience con la letra '{letra}'")

        
    #Buscar si un nombre esta en la lista
    elif opcion_elegida=="8":
        nombre1=input("Ingrese el nombre que quiere buscar: ").strip()
        if nombre1 in lista_estudiantes:
            print(f"El nombre '{nombre1}' esta en la lista de estudiantes")
        else:
            print (f"El nombre '{nombre1}' no esta en la lista")


    #Finalizar
    elif opcion_elegida=="9":
        print("El programa es siendo cerrado...")
        break



 
 

    # #Buscar si un nombre esta en la lista
    # elif opcion_elegida=="8":
    #     nombre1=input("Ingrese el nombre que quiere buscar: ").strip()
    #     if nombre1 in lista_estudiantes:
    #         print(f"El nombre '{nombre1}' esta en la lista de estudiantes")
    #     else:
    #         print (f"El nombre '{nombre1}' no esta en la lista")


    # # Buscar si un nombre o nombre completo está en la lista
    # elif opcion_elegida == "8":
    #     nombre1 = input("Ingrese el nombre o nombre completo que quiere buscar: ").strip().lower()

    #     # Verificar si el nombre1 está contenido en alguno de los nombres completos de la lista
    #     nombres_encontrados = [nombre for nombre in lista_estudiantes if nombre1 in nombre.lower()]

    #     if nombres_encontrados:
    #         print(f"Se encontraron los siguientes nombres que contienen '{nombre1}':")
    #         for nombre in nombres_encontrados:
    #             print(nombre)
    #     else:
    #         print(f"No se encontró ningún nombre que contenga '{nombre1}'")