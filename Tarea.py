#Estudiante:Carlos Andrés Molina Jaramillo

#Ejercicio 1

import math 
from datetime import date

class Operaciones:

     
     #TIPOS DE DATOS Y ACCIONES ELEMENTALES

     
     #Dados dos números calcule la suma, resta, multiplicación, división y módulo
     def operacionesBasicas(self):
          num1 = int(input("Ingrese un número: "))
          num2 = int(input("Ingrese un número: "))
          a = num1 + num2 
          d = num1 - num2
          p = num1 * num2
          c = num1 / num2
          cround = round(c, 2)
          m = num1 % num2

          print("La suma es: {}".format(a))
          print("La resta es: {}".format(d))
          print("La multiplicación es: {}".format(p))
          print("La división es: {}".format(cround))
          print("El módulo es: {}".format(m))  

    
     #Dados tres números, hacer una aplicación que calcule la resolvente
     def resolvente(self):
          num1 = int(input("Ingrese un número: "))
          num2 = int(input("Ingrese un segundo número: "))
          num3 = int(input("Ingrese un tercer número: "))

          d = ((num2)**2)-4*num1*num3 
         
          if d > 0:               
               x1 = (-num2 + math.sqrt(d))/(2*num1)
               x1round = round(x1, 2)
               x2 = (-num2 - math.sqrt(d))/(2*num1) 
               x2round = round(x2, 2)
               print("Las soluciones de la ecuación son: ({} , {})".format(x1round,x2round))
          elif d == 0:
               x = -num2/(2*num1)
               print("La única solución es: {}".format(x))  
          else:
               x3 = "No existe solución"
               print(x3)

     
     #Dados dos lados de un triángulo en cm, calcular la hipotenusa del mismo
     def hipotenusa(self):
          num1 = int(input("Ingrese un número: "))
          num2 = int(input("Ingrese un número: "))
    
          h = math.sqrt((num1)**2 + (num2)**2)
          hround = round(h, 2)
          print("La hipotenusa es: {}".format(hround),"cm")

     
    
     #Dado un número, imprimir 0 si es par y 1 si es impar        
     def paridadImparidad(self):
          num1 = int(input("Ingrese un número: "))

          if num1 % 2 == 0:
               print("El número {}".format(num1),"es 0 par")
          else:
               print("El número {}".format(num1),"es 1 impar")
               

     
     #Dado un número binario de cuatro dígitos, imprimir su bit de paridad. El bit de paridad es 1 si el número de bits 1 es impar 
     #y 0 en caso contrario
     def bitParidad(self):
          binario = str(input("Ingrese un número binario de 4 dígitos: "))
          
          bit1 = int(binario[0])
          bit2 = int(binario[1])
          bit3 = int(binario[2])
          bit4 = int(binario[3])
          contador = bit1 + bit2 + bit3 + bit4

          if contador % 2 == 0:
               print("El bit de paridad es 0")
          else:
               print("El bit de paridad es 1")

   
     #Dado un número binario de cuatro dígitos imprimir su valor
     def imprimirValor(self):
          nbin = str(input("Ingrese un número binario que conste de 4 dígitos: "))

          m1 = int(nbin[0])
          m2 = int(nbin[1])
          m3 = int(nbin[2])
          m4 = int(nbin[3])
          bin_a_decimal = (m4 *2**0) + (m3 *2**1) + (m2 *2**2) + (m1 *2**3)
          print("El valor del número binario es: {}".format(bin_a_decimal))

     
     #Dado un número de cuatro dígitos, imprimirlo por separado en unidades, decenas, centenas y unidades de mil
     def sistemadecimal(self):
          num5 = int(input("Ingrese un número de 4 dígitos: "))

          while  num5 > 1000 and num5 < 10000:
               unidad_de_mil = num5 // 1000
               print("La unidad de mil es: ", unidad_de_mil)
               centena = (num5 - (unidad_de_mil * 1000)) // 100
               print("La centena es: ", centena)
               decena = (num5 - (unidad_de_mil * 1000 + centena * 100)) // 10
               print("La decena es: ", decena)
               unidad = (num5 - (unidad_de_mil*1000 + centena*100 + decena*10)) 
               print("La unidad es: ", unidad)
               break


     #ESTRUCTURAS DE CONTROL DE FLUJO DE DATOS

     
     #Todos los años que se dividen exactamente entre 400, o que son divisibles exactamente entre 4 y no son divisibles
     #exactamente entre 100, son años bisiestos. Usando estas premisas crea un algoritmo que lea una fecha como un número entero
     #con el formato ddmmaaaa, y luego extraiga el año de la fecha indicando si el mismo es un año bisiesto o no     
     def añoBisiesto(self):
          ddmmaaaa = int(input("Ingrese día, mes y año: "))
          
          año = ddmmaaaa % 10000
          día = ddmmaaaa // 1000000
          mes = (ddmmaaaa //10000) % 100

          if ((año % 4 == 0) and (año % 100 != 0) or (año % 400 == 0)):
               print("Es año bisiesto")
          else:
               print("No es año bisiesto")

    
     #Dado un número entero cuya cantidad de dígitos es igual a 5, determine si es capicúa
     def capicúa(self):
          c = int(input("Ingrese un número capicúa de 5 dígitos: "))

          if c > 9999 and c < 99999:
               if str(c) == str(c)[::-1]:
                    print("Es capicúa")
               else:
                    print("No es capicúa")
          else:
               print("Ingrese un número de 5 dígitos")
     
     
     #Cree un algoritmo que tome por entrada las horas y minutos de un día, y de como resultado
     #su equivalente en segundos
     def horasMinutosDía(self):
          horas = int(input("Ingresar el tiempo en horas: "))
          minutos = int(input("Ingresar el tiempo en minutos: "))

          s1 = horas * 3600
          print("{}".format(horas),"horas en segundos es: {}".format(s1),"segundos")
          s2 = minutos * 60
          print("{}".format(minutos),"minutos en segundos es: {}".format(s2),"segundos")

     
     #Para un valor entero positivo que representa una cantidad en segundos, indicar su equivalencia en minutos, horas y días
     def convertirSegundos(self):
          segundos = int(input("Ingresar un valor en segundos: "))

          if segundos > 0:
               minutos = segundos / 60
               minutosround = round(minutos, 2)
               print("{} segundos".format(segundos),"son: {}".format(minutosround),"minutos")

               horas = segundos / 3600
               horasround = round(horas, 2)
               print("{} segundos".format(segundos),"son: {}".format(horasround),"horas")


               días = segundos / 86.400
               díasround = round(días, 2)
               print("{} segundos".format(segundos),"son: {}".format(díasround),"días")
               
          else:
               print("El valor es negativo, ingrese un dato positivo: ")

     
     #Dados tres números enteros positivos A,B y C, determine,¿cuál de ellos es el mayor? y ¿cuál es el segundo mayor?
     def ComparacionMayorQue(self):
          A = int(input("Ingresar el valor de A: "))
          B = int(input("Ingresar el valor de B: "))
          C = int(input("Ingresar el valor de C: "))
          
          if A and B and C > 0:
              
               if A > B and A > C:
                    print("El mayor de los 3 números es: {}".format(A))
                    if B > C:
                         print("El segundo número mayor es: {}".format(B))
                    else:
                         print("El segundo número mayor es: {}".format(C)) 

               elif B > A and B > C:
                    print("El mayor de los 3 números es: {}".format(B))
                    if A > C:
                         print("El segundo número mayor es: {}".format(A))
                    else: 
                         print("El segundo número mayor es: {}".format(C)) 

               elif C > A and C > B:
                    print("El mayor de los 3 números es: {}".format(C))
                    if A > B:
                         print("El segundo número mayor es: {}".format(A))
                    else:
                         print("El segundo número mayor es: {}".format(B))
               
               else:
                    print("Los números son iguales")

          else:
               print("Ingrese un número positivo")

    


     #El IMC resulta de la división de la masa del individuo (en kilogramos) entre el cuadrado de la estatura (en metros)
     #El índice de masa corporal es un indicador del peso de una persona en relación con su altura.
     #Dado el peso de una persona en libras (1 libra = 0,453592 Kg) y su estatura en centímetros, calcule su IMC e indique como salida el peso en kilogramos, el valor
     #de IMC de la persona y la categoría en la cual fue clasificado.

     def pesoCorporal(self):
          masa = int(input("Ingresar masa corporal: "))
          estatura = int(input("Ingresar estatura: "))

          masa_kg = masa / 2.205                 #1kg = 2.205 lb
          estatura_metros = estatura / 100

          IMC = masa_kg / (estatura_metros)**2

          if IMC < 16:
               print("Criterio de ingreso")
          elif IMC >= 16 and IMC <= 16.9:
               print("Infra peso")
          elif IMC >= 17 and IMC <= 18.4:
               print("Bajo peso")
          elif IMC >= 18.5 and IMC <= 24.9:
               print("Peso normal")
          elif IMC >= 25 and IMC <= 29.9:
               print("Sobrepeso")
          elif IMC >= 30 and IMC <= 34.9:
               print("Obesidad pre-mórbida")
          elif IMC >= 40 and IMC <= 45:
               print("Obesidad mórbida")
          elif IMC > 45:
               print("Obesidad híper-mórbida")
          else:
               pass

     
     #Escriba un algoritmo que reciba una fecha (día y mes) correspondiente al año 2014
     #e imprima por pantalla el número de días que han pasado desde el 1 de Enero de 2014 hasta la fecha dada
     def recibirFecha(self):
          Mes = int(input("Indicar el Mes por número, ingresar valor: "))
          Días = int(input("Indicar el número del día, ingresar valor: "))


          hoy = date(2014, Mes, Días)
          pasada_fecha = date(2014,1,1)
          días_transcurridos = hoy - pasada_fecha
          print("Han pasado {}".format(días_transcurridos.days),"días desde el 1 de Enero de 2014")

     
     #Solicitar un número entre el 1 y el 12 e imprimir el mes correspondiente a dicho número
     def MesCorrespondiente(self):
          mes = int(input("Indicar el mes por número, ingresar valor: "))

          if mes >=1 and mes <= 12:
               if mes == 1:
                    print("Enero")
               elif mes == 2:
                    print("Febrero")
               elif mes == 3:
                    print("Marzo")
               elif mes == 4:
                    print("Abril")
               elif mes == 5:
                    print("Mayo")
               elif mes == 6:
                    print("Junio")
               elif mes == 7:
                    print("Julio")
               elif mes == 8:
                    print("Agosto")
               elif mes == 9:
                    print("Septiembre")
               elif mes == 10:
                    print("Octubre")
               elif mes == 11:
                    print("Noviembre")
               elif mes == 12:
                    print("Diciembre")
          else:
               pass

   
     #En un almacén se hace un 20% de descuento a los clientes cuya compra supere
     #los Bs 1000, se desea que realice un algoritmo el cual tome por entrada el monto a
     #pagar por el cliente y arroje como salida el monto aplicando el descuento de ser
     #necesario.

     def descuento(self):
          precio = float(input("Ingresar precio: "))

          if precio > 1000:
               descuento = precio * 0.20
               precio_final = precio - descuento
               print("El precio a pagar es de: {}".format(precio_final),"Bs")
          else:
               print("El precio a pagar es de: {}".format(precio))

    
     #ESTRUCTURAS ITERATIVAS

     #Dado un número entero N, calcular e informar el usuario cuántos dígitos tiene dicho número
     def digitosDeN(self):
          n1 = int(input("Ingresar un número: "))

          while n1 < 0 or n1 >= 0:
               digitos = len(str(n1))
               print("El número tiene: {}".format(digitos),"dígitos")
               break

   
     #Dado un número, determine si es capicúa
     def determinarCapicúa(self):    
          d = int(input("Ingresar un valor capicúa: "))

          if str(d) == str(d)[::-1]:
               print("Es capicúa")
          else:
               print("No es capicúa")

 
     #Dado un número N determinar si es un número primo   
     def númeroprimo(self):
          nprimo = int(input("Ingresar un número: "))

          for i in range(2, nprimo):
               if nprimo % i == 0:
                    print("El número {}".format(nprimo),"no es primo")
               else:
                    print("El número {}".format(nprimo),"sí es primo")
               break
     
    
     #Construya un programa que dado un valor entero N, haga el cálculo de la función factorial
     #estructuras iterativas
     def factorial(self):
          num = int(input("Ingresar un número: "))

          while True:      
               if num < 0:
                    print("No existe factorial")
               elif num == 0: 
                    print("El factorial es 1")
               else:
                    resultado1 = num - 1
                    while resultado1 > 0:
                         num = num * resultado1
                         resultado1 = resultado1 - 1               
                    print("El factorial es: {} ".format(num))
               break

    

     #Dado un número entero N que representa una contraseña y asumiendo que una contraseña
     #debe tener al menos 10 dígitos para ser segura, determine si la contraseña ingresada por el
     #usuario es correcta, de no serlo debe pedirla nuevamente hasta que tenga los 10 (diez dígitos solicitados)
     #y al ser correcta mostrar un mensaje de éxito al usuario, por salida estándar

     def contraseña(self):
          clave = int(input("Ingresar una contraseña: "))

          z = 0
          while clave > 0:
               clave //= 10
               z = z + 1
          if z == 10:
               print("La contraseña es segura")
          else:
               print("La contraseña no es segura")

     #Dada una secuencia de números terminada en cero (0), elaborar un algoritmo que informe al usuario qué valor tiene el número mayor
     #y qué valor tiene el número menor, sin contar el cero (0)

     def secuenciaNúmeros(self):
          lista = []
          t = True
          while t:
               dato = int(input("Ingresar un número(digitar 0 si desea terminar): "))
               if dato == 0:
                    t = False
               else:
                    lista.append(dato)
          mayor,menor = Operaciones.mayor_menor_que(lista)
          if len(lista) > 0: 
               print("El número mayor es: ", mayor)
               print("El número menor es: ", menor)
          
     def mayor_menor_que(lista):
          mayor = 0
          menor = 999999999999999
          for dato in lista:
               if dato > mayor:
                    mayor = dato
               if dato < menor:
                    menor = dato
          return mayor, menor

     
     #Se tiene una secuencia de enteros terminada en cero, que corresponde a la edad,
     # peso y estatura de una muestra de hombres y mujeres mayores de 18 años. Con
     #base en dicha secuencia se desea realizar un estudio a fin de conocer:
     #Edad promedio de todas las personas en la muestra.
     #Peso promedio de todas las personas en la muestra.
     #Estatura promedio de todas las personas en la muestra.
     #Cuántas personas hay con edad entre los 18 y 25 años.
     # Cuántas personas son mayores a 36 años. Cuál es el promedio de peso de las personas con edades entre 18 y 35
     #años.
     def  secuencia(self):
          edad=[20,30,40,50,60,70]
          peso=[40,50,60,70,80,90]
          estatura=[1.40,1.50,1.60,1.70,1.80,1.90]
          prom_edad=(sum(edad))/len(edad)
          prom_peso=(sum(peso))/len(peso)
          prom_estatura=(sum(estatura))/len(estatura)
          c=0
          x=0
          while c < 8:
               x+=(edad.count(20+c))
               c+=1  
          c=1
          m=0  
          while c<150:
               m+=(edad.count(40+c))
               c+=1
          c=0
          contPos=0
          while c<36:
               contPos=[i for i,x in enumerate(edad) if x>=18 and x<=35]
               c+=1
          suma=0
          c=0
          while c<len(contPos):
               suma+=peso[contPos[0+c]]
               c+=1
          print(contPos)
          print(f"El promedio de edades de todas las personas es de: {prom_edad:.2f}")
          print(f"El promedio de peso de todas las personas es de: {prom_peso:.2f}")
          print(f"El promedio de estatura de todas las personas es de: {prom_estatura:.2f}")
          print(f"Hay {x}, personas con edad de entre [18-25] ")
          print(f"Hay {m}, personas mayor(es) a 36 años")
          print(f"El promedio de peso entre las personas de 18 a 35 años es: {suma/len(contPos):.2f}")
     
    
     #Construye un algoritmo  que calcule e imprima la tabla de multiplicar, desde la tabla del 1 hasta la del 10
     def tablaMultiplicar(self):
          factor1 = int(input("Ingrese un número: "))

          for i in range(0, 11):  
               respuesta = factor1 * i
               print("{}".format(factor1),"x",i,"= {}".format(respuesta))

   
     #Escribir un algoritmo que muestre todas las fichas de dominó, sin repetir
     def fichasDomino(self):

          for i in range(0, 7):
               for j in range(0, i+1):
                    print("|" + str(i) + "|" + str(j) + "|")

    
     #Dados N números positivos (N>1), calcular el promedio de esta serie. Considere que la serie termina al leer un 0
     def promedio(self):
          m1 = int(input("Ingrese un número: "))
   
          contador = 0
          suma = 0
          while m1 > 1:
              m1 = int(input("Ingresar otro dato: "))
              suma = suma + m1
              contador = contador + 1
          if contador == 0:
               print("Termina el proceso")
          else:
               promedio = suma / contador
               print("El promedio de los {}".format(contador), "números es igual a : {}".format(promedio))
          


      
     
     #PROCEDIMIENTOS (ACCIONES Y FUNCIONES)
     
     #Construya una función que solicite edades al usuario y determine el promedio de las edades mayores a 18 años.
     #El usuario indicará cuando sea dejar de suministrar datos de entrada. En la Acción Principal se informará el promedio calculado.
     def calcularProm(self):
          lista = []
          a = True
          while a:
               edad = int(input("Ingresar una edad (si desea detener el ingreso de datos digite 0), las edades deben ser mayores a 18: "))
               if edad > 18:
                    lista.append(edad)
               else:
                    a = False

          promedio = Operaciones.prom_edad(lista)
          if len(lista) > 0:
               print("El promedio de las edades ingresadas es: {}".format(promedio))
          else:
               print("No es posible calcular el promedio")
     def prom_edad(lista):
          for edad in lista:
               if edad > 18:
                    promedio = sum(lista) / len(lista)
                    return promedio          
          

     
     #Escriba una función que calcule el perímetro del pentágono (siendo el perímetro la suma de los lados del polígono)
     def p_pentágono(self): 
          acum = 0
          for i in range(5):
               lado = int(input("Ingresar la medida de un lado: "))         
               acum = Operaciones.perimetro(acum, lado)
          print("El perímetro del pentágono es: {}".format(acum))
     
     def perimetro(acum, lado):
          acum = acum + lado
          return acum
    
         
     
          
     #Construya una función "Eleva" que reciba como parámetros una base y un exponente y retorne al algoritmo principal
     #el resultado de elevar un número al otro
     def Eleva(self):
          base = int(input("Ingresar el valor de la base: "))
          exponente = int(input("Ingresar el exponente: "))

          potencia = Operaciones.potencia(self,base,exponente)
          print("El número {}".format(base),"elevado al exponente {}".format(exponente),"es: {}".format(potencia))


     def potencia(self, base, exponente):  
          potencia = base ** exponente
          return potencia
          


     #En una empresa pagan según las horas trabajadas y una tarifa fija por hora. Si la cantidad de horas trabajadas 
     #en una semana es mayor a 40, la tarifa se incrementa en un 35% para las horas extras. Escribe una acción princial 
     #que solicite la identificación de 5 empleados, el monto cancelado por hora, y la cantidad de horas trabajadas por 
     #cada uno, llame a acciones/funciones que calculen el salario semanal por horas trabajadas (<=40) y los ingresos 
     #por concepto de horas extras, y finalmente informe los resultados en la acción principal.
     def nombreEmpleado(self):
          id = {}
          cp = Operaciones()

          while len(id) <= 4:
               c = input("Ingresar identificación del trabajador(Nombre): ")
               id[c] = int(input("Ingresar las horas trabajadas de {}: ".format(c)))
          horas = int(input("Ingresar el monto por hora: "))

          pt = cp.calcularSalario(id, horas)
          for i in pt:
               print(i,"cobrará: ",pt[i][1])
     def calcularSalario(self, c, ht):
          psc = Operaciones()
          for i in c:
               if c[i] <= 40:
                    c[i] = [c[i],(c[i]*ht)]
               else:
                    c[i] = [c[i],(40*ht)]
                    c[i][1] = psc.aumentoTarifa(c[i],ht)
          print("****siguiente proceso***")
          return c
     def aumentoTarifa(self,k,ht):
          extra = k[1] + ((k[0]-40)*(ht + (ht*0.35)))
          return extra

     
     #Escriba una acción (MillasAKilómetros) que convierte una distancia en millas a kilómetros (1milla = 1.60935km)
     #Esta acción recibirá como parámetros: el nombre de la ciudad origen, el nombre de la ciudad destino y la distancia
     #en millas entre ellas y debe retornar la distancia entre las ciudades en kilómetros.
     #Desarrolle además una acción principal donde utilice a la acción MillasAKilómetros para convertir e informar la distancia 
     #en kilómetros entre 4 pasos de ciudades suministradas por el usuario.
     
     def nombreCiudad(self):
          for i in range(4):
               ciudad1 = input("Ingresar el nombre de una ciudad A: ")
               ciudad2 = input("Ingresar el nombre de una ciudad B: ")
  
               milla_a_km = Operaciones.MillasAKilómetros(self)
               print("La distancia entre {}".format(ciudad1),"y {}".format(ciudad2),"es: {}".format(milla_a_km),"Km")   

     def MillasAKilómetros(self):             
               distancias_en_millas = float(input("Ingresar una distancia: "))
               milla_a_km = distancias_en_millas * 1.60935
               return milla_a_km
          
         
         







andres = Operaciones()





        


                    
               
                              
                    
                         
                    
          
              
               
          
            

          
          




     
          











          




