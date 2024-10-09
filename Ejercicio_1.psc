Algoritmo Ejercicio_1
	//1) Solicitar a un usuario que ingrese valores para una matriz de 2 x 5 y determinar cual fué el numero mayor mediante una búsqueda.
	Dimension matrizA[2,5] 
	Mostrar "Ingrese valores de la matriz"
	Para i<-1 Hasta 2 Con Paso 1 Hacer
		Para j<-1 Hasta 5 Con Paso 1 Hacer
			Leer matrizA[i,j]
		FinPara
	FinPara
	
	Mostrar "La matriz formada es "
	Para i<-1 Hasta 2 Con Paso 1 Hacer
		Para j<-1 Hasta 5 Con Paso 1 Hacer
			Escribir "[ ", matrizA[i,j],"]" Sin Saltar;
		Fin Para
		Escribir " ";
	Fin Para
	
	valor_mayor=matrizA[1,1]
	
	Para i<-1 Hasta 2 Con Paso 1 Hacer
		Para j<-1 Hasta 5 Con Paso 1 Hacer
			si matrizA[i,j]>valor_mayor
				valor_mayor<-matrizA[i,j]
			FinSi
		FinPara
	FinPara
	
Mostrar "El valor mayor es: " valor_mayor
	
	
	

FinAlgoritmo