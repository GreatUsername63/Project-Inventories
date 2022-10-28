#Aqui es el codigo, se llama main por que si.
#Acuerdense poner notas para explicar como funciona 
#su codigo.

#Aqui pongo un import de OS para usar el metodo exists
import os

#-----------------------------------------
#Aqui abajo definan fuciones
#-----------------------------------------
def productos_almacen():
    archivo = open("DatosProductos.txt", "r") #abre el archivo en read
    matriz = txt_a_matriz(archivo) #lo convierte en matriz
    archivo.close()
    print("\n=======================================" +
    "================================")
    print("Para registrar la llegada de productos al almacen" +
    ", ingresa el nombre del producto seguido de la cantidad que llego" +
    "(Separados por comas).")
    print("Ejemplo:manzanas verdes,150")
    print("Para dejar de registrar ingrese un solo *")
    print("===============================================================" +
    "========")
    while True:
        entrada = input()
        if entrada == "*":
            break #Sale del ciclo while si se pone un *
        lista_registro = entrada.split(",") #usar split para convertir la entrada en lista
        for i in range(len(lista_registro)):
            lista_registro[i] = lista_registro[i].lstrip().rstrip().lower() #Quita los espacios al inicio y al final y pone todo en minusculas de cada cosa de la lista

        #En esta seccion checa si hay un error en la sintaxis
        if len(lista_registro) != 2:
            print("Error. Se tiene que ingresar 2 datos separados por una coma.")
            continue #No lo acepta si no se dan los 2 terminos
        if lista_registro[1].isnumeric() == False:
            print("Error. La cantidad en inventario tiene que ser un numero entero.")
            continue #No lo acepta si no es numero entero

        numero_producto = -1 #Los numeros empiezan en -1 por si no se encuentran
        #Buscar el producto
        for i in range(len(matriz)):
            if lista_registro[0] == matriz[i][0]:  #Busca en las listas de la matriz de productos el nombre.
                numero_producto = i #Numero de la lista en la que lo encuentra.
        
        if numero_producto == -1:
            print("Error. No hay productos registrados con ese nombre.")
            continue #No lo acepta si no encuentra el nombre

        #Sumar los nuevos productos a la cantidad ya en inventario
        matriz[numero_producto][1] = str(int(matriz[numero_producto][1]
        ) + int(lista_registro[1]))
        print("------------------------------------------------------------")
        print("Exito!. Se registro la llegada de inventario:")
        print("Producto: " + lista_registro[0])
        print("Nueva cantidad en inventario: " + lista_registro[1])
        print("------------------------------------------------------------")
    
    archivo = open("DatosProductos.txt", "w") #Abre el archivo en write
    matriz_a_txt(matriz, archivo) #Guarda la matriz al texto
    archivo.close()
    print("---------------------------------------------------------")

def ventas_por_vendedor_o_por_articulo(): #Reporte de ventas por vendedor (V) y por artículo (A)
    while True:
        print("Este es el reporte de ventas.")
        print("Mostrar ventas por vendedor o por artículo (v o a)")
        print("Ingrese * para salir de este modo.")
        respuesta = input().lower().lstrip().rstrip() #Para que sea con minusculas, mayusculas y espacios
        if respuesta == "a":
            print("\n" + "Este es el reporte de ventas por artículo:\n")  
            print("|------PRODUCTOS------|   |--VENTAS--|")
            productos = open("DatosProductos.txt", "r") #Abres los datos de los productos en read
            matriz = txt_a_matriz(productos)
            for i in range(len(matriz)): #Ciclo para seperar los datos en la tabla
                ventas_productos = "{}{}".format(matriz[i][0].ljust(26), matriz[i][2].ljust(
                18))
                print(ventas_productos) #Imprimir la tabla de los vendedore
            continuar()
        elif respuesta == "v":
            print("\n" + "Este es el reporte de ventas por vendedor:\n")  
            print("|------VENDEDOR------| |--VENTAS--|")
            vendedores = open("DatosVendedores.txt", "r") #Abres los datos de los vendedores en read
            matriz = txt_a_matriz(vendedores)
            for i in range(len(matriz)): #Ciclo para seperar los datos en la tabla
                ventas_vendedores = "{}{}".format(matriz[i][0].ljust(26), matriz[i][1].ljust(
                18))
                print(ventas_vendedores) #Imprimir la tabla de los vendedores
            continuar()
        elif respuesta == "*":
            print("---------------------------------------------------------")
            break


def consultar_inventario(): # Función para indicar lo que hay en el inventario 
    print("\n" + "Actualmente en el inventario hay lo siguiete:\n")  
    print("|------PRODUCTOS------|  |---CANTIDAD---|  |--VENTAS--|")
    inventario = open("DatosProductos.txt", "r") # abrir inventario en modo read 
    remplazo = str.maketrans(",",".")  # reemplazar ',' por '.'
    intercambio = inventario.read()  
    filtro1 = intercambio.translate(remplazo)  
    remplazo_2 = str.maketrans("\n"," ")   # reempazar '\n' por ' ' 
    filtro2 = filtro1.translate(remplazo_2)
    lista = filtro2.split(".") # función para realizar una lista
    if "" in lista: # if para borrar espacios vacios para que la lista no quede con indices vacios
        lista.remove("")
    else:
        pass
    if " " in lista:
        lista.remove(" ")
    else:
        pass
    lista_productos = (lista [0::3])  # lista de productos
    lista_cantidades = (lista [1::3])   # lista de cantidades
    lista_ventas = (lista [2::3])   # lista de ventas
    j = 0 # variable contadora
    for i in lista_productos:     # ciclo for para formateo de las listas
        tabla_inventario = '{}{}{}'.format(i.ljust(26),  
                            lista_cantidades[j].ljust(18),
                            lista_ventas [j])                 
        j += 1                                                                                               
        print(tabla_inventario)
    inventario.close  # cerrar inventario
    continuar()
    # fin de la función     

def txt_a_matriz(archivo): #Funcion que hice para cargar la matriz ya hecha y ponerla en cualquier lugar. Toma un archivo en modo r como entrada.
    mat = [] #la matriz que vamos a generar
    while True:
        linea = archivo.readline() #Lee una linea
        if linea == "": #Sale del ciclo si la linea esta vacia
            break
        linea = linea[0:-2] #Quita el ,\n del final de la linea
        mat.append(linea.split(",")) #Convierte la linea en lista y la lista la pone en la matriz
    return mat #regresa la matriz
    #Fin de txt_a_matriz

def matriz_a_txt(mat, archivo): #Funcion que hice para pasar una matriz al texto de nuevo. Toma una matriz y un archivo en modo r como entrada
    for i in range(len(mat)):
        string = "" #string en el que pondremos la lista de la matriz
        for j in range(len(mat[i])):
            string += mat[i][j] + ","
        string += "\n"
        archivo.write(string) #Agrega todo lo de la matriz al .txt.
#fin de la funcion

def añadir_productos():
    
    archivo_productos_r = open("DatosProductos.txt", "r") #Abre el archivo en modo read
    mat = txt_a_matriz(archivo_productos_r) #hace una matriz con los datos que ya estan en el .txt para agregarlos con los nuevos mas tarde. La funcion la definí ahi arriba.
    print("\n=======================================" +
    "================================")
    print("Para añadir productos, pon el nombre del producto seguido" +
    " de su cantidad en inventario (separado por una coma)")
    print("Ejemplo:manzanas verdes,150")
    print("Para dejar de añadir productos ingrese un solo *")
    print("==================================================================" +
    "=====")
    while True:
        nuevo_producto = input() #datos de entrada
        if nuevo_producto == "*":
            break #Sale del ciclo while si se pone un *
        lista_producto = nuevo_producto.split(",") #usar split para convertir la entrada en lista
        for i in range(len(lista_producto)):
            lista_producto[i] = lista_producto[i].lstrip().rstrip().lower() #Quita los espacios al inicio y al final y pone todo en minusculas de cada cosa de la lista
        lista_producto.append("0") #Añade un 0 para representar los productos vendidos hasta ahora
        
        #En esta seccion checa si hay un error en la sintaxis
        if len(lista_producto) != 3: #es 3 por el 0 que añadimos
            print("Error. Se tiene que ingresar 2 datos separados por una coma.")
            continue #No lo acepta si no se dan los 2 terminos
        if lista_producto[1].isnumeric() == False:
            print("Error. La cantidad en inventario tiene que ser un numero entero.")
            continue #No lo acepta si no es numero entero

        mat.append(lista_producto) #añade la lista a la matriz
        print("------------------------------------------------------------")
        print("Exito!. El producto se registro como:")
        print("Nombre: " + lista_producto[0])
        print("Cantidad inventario: " + lista_producto[1])
        print("Cantidad vendida: " + lista_producto[2])
        print("------------------------------------------------------------")

    archivo_productos_w = open("DatosProductos.txt", "w") #Abre el archivo en modo write
    matriz_a_txt(mat, archivo_productos_w) #Guarda la matriz al texto nuevamente con otra funcion que hice
    
    archivo_productos_w.close() #cerrar el archivo
    archivo_productos_r.close()
    print("---------------------------------------------------------")
    #Fin de la funcion para añadir productos

def añadir_vendedores():
    archivo_vendedores_r = open("DatosVendedores.txt", "r") #Abre el archivo en modo read
    mat = txt_a_matriz(archivo_vendedores_r) #hace una matriz con los datos que ya estan en el .txt para agregarlos con los nuevos mas tarde. La funcion la definí ahi arriba.
    print("\n=============================================================" +
    "==========")
    print("Para añadir vendedores, simplemente pon el nombre del vendedor")
    print("Para dejar de añadir vendedores ingrese un solo *")
    print("=============================================================" +
    "==========")
    while True:
        nuevo_vendedor = input() #dato de entrada
        lista_vendedor = [] #lista para poner en la matriz
        if nuevo_vendedor == "*":
            break #Sale del ciclo while si se pone un *
        nuevo_vendedor = nuevo_vendedor.lstrip().rstrip().lower() #Quita los espacios al inicio y al final y pone todo en minusculas
        lista_vendedor.append(nuevo_vendedor) #añade el nombre a la lista
        lista_vendedor.append("0") #añade la cantidad de productos vendidos desde el registro

        mat.append(lista_vendedor) #añade la lista a la matriz
        print("------------------------------------------------------------")
        print("Exito!. El producto el vendedor se registro como:")
        print("Nombre: " + nuevo_vendedor)
        print("------------------------------------------------------------")
    archivo_vendedores_w = open("DatosVendedores.txt", "w") #Abre el archivo en modo write
    matriz_a_txt(mat, archivo_vendedores_w) #Guarda la matriz al texto con otra funcion que hice

    archivo_vendedores_w.close()
    archivo_vendedores_r.close()
    print("---------------------------------------------------------")
    #Fin de la funcion para añadir vendedores

def registrar_ventas():
    archivo_productos_r = open("DatosProductos.txt", "r") #Abre el archivo en modo read de los 2 archivos
    archivo_vendedores_r = open("DatosVendedores.txt", "r") #Abre el archivo en modo read
    archivo_ventas_r = open("DatosVentas.txt", "r")
    mat_productos = txt_a_matriz(archivo_productos_r) #hace dos matrizes con los datos que ya estan en el .txt para agregarlos con los nuevos mas tarde. La funcion la definí ahi arriba.
    mat_vendedores = txt_a_matriz(archivo_vendedores_r)
    mat_ventas = txt_a_matriz(archivo_ventas_r)
    print("\n=============================================================" +
    "==========")
    print("Para registrar ventas, introduce el nombre del producto, el " +
    "nombre del vendedor y la cantidad vendida (Separado en minusculas).")
    print("Ejemplo: manzana verde, gustavo, 2")
    print("Para dejar de registrar ventas poner un solo *")
    print("=============================================================" +
    "==========")
    while True:
        entrada = input()
        if entrada == "*":
            break #Sale del ciclo si hay asterisco
        lista_entrada = entrada.split(",") #Divide la string en una lista. 0 = producto, 1 = vendedor, 2 = cantidad
        for i in range(len(lista_entrada)):
            lista_entrada[i] = lista_entrada[i].lstrip().rstrip().lower() #A cada dato de la lista le corta los espacios en el principio y final y lo pone en minusculas
        
        #checar si si se pusieron los 3 digitos
        if len(lista_entrada) != 3:
            print("Error. Se tiene que ingresar 3 datos separados por una" +
            " coma.")
            continue #No lo acepta si no se dan los 3 terminos
        
        #Buscar las filas correspondientes en las matrizes
        numero_producto = -1 #Los numeros empiezan en -1 por si no se encuentran
        numero_vendedor = -1
        #Buscar el producto
        for i in range(len(mat_productos)):
            if lista_entrada[0] == mat_productos[i][0]:  #Busca en las listas de la matriz de productos el nombre.
                numero_producto = i #Numero de la lista en la que lo encuentra.
        #Buscar el vendedor
        for i in range(len(mat_vendedores)):
            if lista_entrada[1] in mat_vendedores[i][0] : #Busca en las listas de la matriz de productos el nombre.
                numero_vendedor = i #Numero en la lista en la que lo encuentra
        
        #Checar si hay errores
        if numero_producto == -1:
            print("Error. No hay productos registrados con ese nombre.")
            continue
        if numero_vendedor == -1:
            print("Error. No hay vendedores registrados con ese nombre.")
            continue
        if lista_entrada[2].isnumeric() == False:
            print("Error. La cantidad vendida tiene que ser" +
            "un numero entero.")
            continue #No lo acepta si no es numero entero

        #Registrar la venta en el producto
        mat_productos[numero_producto][1] = str(int(mat_productos[numero_producto][1]) - int(lista_entrada[2]))
        mat_productos[numero_producto][2] = str(int(mat_productos[numero_producto][2]) + int(lista_entrada[2]))

        #Registrar la venta en el vendedor
        mat_vendedores[numero_vendedor][1] = str(int(mat_vendedores[numero_vendedor][1]) + int(lista_entrada[2]))

        #Registrar la venta
        mat_ventas.append(lista_entrada)
        print("------------------------------------------------------------")
        print("Exito!. Venta registrada")
        print("------------------------------------------------------------")

    archivo_productos_w = open("DatosProductos.txt", "w")
    archivo_vendedores_w = open("DatosVendedores.txt", "w") #Abre el archivo en modo write
    archivo_ventas_w = open("DatosVentas.txt", "w")
    #Guarda las matrizes con la funcion a los txt
    matriz_a_txt(mat_productos, archivo_productos_w)
    matriz_a_txt(mat_vendedores, archivo_vendedores_w)
    matriz_a_txt(mat_ventas, archivo_ventas_w)

    archivo_productos_r.close()
    archivo_productos_w.close()
    archivo_vendedores_r.close()
    archivo_vendedores_w.close()
    archivo_ventas_w.close()
    archivo_ventas_r.close()
    print("------------------------------------------------------------")

def añadir_o_editar():
    while True:
        print("Para empezar a añadir productos ingrese A")
        print("Para editar productos existentes, ingrese E")
        print("Si ya no quiere hacer nada ingrese *")
        print("---------------------------------------------------------")
        eleccion = input().lower().lstrip().rstrip() #Formatea el string para que funcione en mayusculas, minusculas y con espacios
    
        if eleccion == "a":
            añadir_productos()
        elif eleccion == "e":
            editar_productos()
        elif eleccion == "*":
            break
        else:
            continue

def editar_productos(): #Edita datos de un producto. Entradas especificadas en los print
    archivo_productos_r = open("DatosProductos.txt", "r") #archivo modo read
    mat = txt_a_matriz(archivo_productos_r) #agarra el txt y lo hace matriz
    consultar_inventario()
    print("\n=============================================================" +
    "==========")
    print("Para editar un producto:")
    print("1. Introduce el nombre del producto.")
    print("2. Introduce el numero del parametro que quieres modificar.")
    print("(1 = nombre, 2 = cantidad en inventario, 3 = cantidad vendida)")
    print("3. Introduce el nuevo valor del parametro.")
    print("Todo separado por comas. ejemplo: manzanas verdes, 1, manzanas rojas")
    print("Para dejar de editar introduce un solo *.")
    print("=============================================================" +
    "==========")
    while True:
        entrada = input()
        if entrada == "*":
            break
        lista_entrada = entrada.split(",") #usar split para convertir la entrada en lista
        for i in range(len(lista_entrada)):
            lista_entrada[i] = lista_entrada[i].lstrip().rstrip().lower() #Quita los espacios al inicio y al final y pone todo en minusculas de cada cosa de la lista

        #checar errores
        #checar si si se pusieron los 3 digitos
        if len(lista_entrada) != 3:
            print("Error. Se tiene que ingresar 3 datos separados" +
            " por una coma.")
            continue #No lo acepta si no se dan los 3 terminos
        #checar si el numero del parametro es un int
        if lista_entrada[1].isnumeric == False:
            print("Error. El numero del parametro tiene que ser entero.")
            continue
        else:
            lista_entrada[1] = int(lista_entrada[1]) #Convertido a int para el proximo chequeo
        #checar si el numero de parametro es valido
        if lista_entrada[1] > 3 or lista_entrada[1] < 1:
            print("Error. El numero del parametro tiene que ser de 1 a 3.")
            continue
        #Checar que el nuevo valor sea un int si el parametro a modificar no es el primero
        if lista_entrada[1] != 1 and lista_entrada[2].isnumeric == False:
            print("Error. En este caso, el valor a editar tiene que ser un" +
            " numero entero.")
            continue

        #Buscar el producto
        num_linea = -1 #Variable que almacena la linea con el nombre del producto, si no, se queda en -1
        for i in range(len(mat)): #Buscar el nombre del producto, si no lo encuentra marcar error
            if mat[i][0] == lista_entrada[0]:
                num_linea = i
        if num_linea == -1:
            print("Error. No hay productos registrados con ese nombre.")
            continue
        
        #Editar el valor
        #mat[numero de la linea del producto][el numero del parametro -1 (para que funcione como indice)] = valor nuevo
        mat[num_linea][lista_entrada[1]-1] = lista_entrada[2]
        print("------------------------------------------------------------")
        print("Exito!. El producto quedo como:")
        print("Nombre: " + mat[num_linea][0])
        print("Cantidad inventario: " + mat[num_linea][1])
        print("Cantidad vendida: " + mat[num_linea][2])
        print("------------------------------------------------------------")
    
    archivo_productos_w = open("DatosProductos.txt", "w") #abre el archivo como write
    matriz_a_txt(mat, archivo_productos_w) #Guarda la matriz al texto nuevamente con otra funcion que hice
    
    archivo_productos_w.close() #cerrar el archivo
    archivo_productos_r.close()
    print("---------------------------------------------------------")
    #Fin de la funcion para editar productos

def mostrar_datos_venta_producto(): #Muestra los datos de las ventas registradas en DatosVentas.txt
    datos_v = open("DatosVentas.txt", "r")
    matriz = txt_a_matriz(datos_v)

    print("|------PRODUCTOS------|  |---VENDEDOR---|  |--VENTAS--|")

    for i in range(len(matriz)):
        tabla_datos_de_ventas = "{}{}{}".format(
        matriz[i][0].ljust(26),matriz[i][1].ljust(
        18), matriz[i][2])
        print(tabla_datos_de_ventas)
    continuar()


def continuar():
    input("Presione enter para continuar...")
    #Espera a que el usuario presione enter para continuar con el codigo
    #Lo hice su propia funcion para lo escribirlo tantas veces

#---------------------------------------------
#Aqui se acaba el espacio de funciones
#---------------------------------------------

#---------------------------------------------
#Inicio del programa principal
#---------------------------------------------
def main():
    datos_existen = os.path.exists("DatosProductos.txt") and os.path.exists("DatosVendedores.txt") and os.path.exists("DatosVentas.txt")  #Usa el metodo .path.exists para ver si existen 
                                                                                                #ya los archivos de texto del programa.
                                                                                                #P.d: resulta que con solo poner el nombre del archivo era suficiente c:
    if datos_existen == False:
        archivo_productos = open("DatosProductos.txt", "w") #lo abre y cierra para crear el archivo
        archivo_productos.close()
        archivo_vendedores = open("DatosVendedores.txt", "w")
        archivo_vendedores.close()
        archivo_ventas = open("DatosVentas.txt", "w")
        archivo_ventas.close()
        #Proceso de registro inicial
        print("Bienvenido! Como esta es la primera vez que se abre el" +
        "programa, se requiere que ingreses la información de los productos y " +
        "los vendedores.")
        print("No te preocupes. Si te equivocas en ingresar algun dato, " +
        "mas tarde se puede editar.")
        print("Primero toca añadir la información de los productos.")
        añadir_productos()
        print("\nListo! Ahora solo falta ingresar la información sobre los " +
        "vendedores.")
        añadir_vendedores()
        print("\nAhora si! Has terminado con el registro inicial del " +
        "programa. Ahora puedes usar las demas funciones que ofrece. " +
        "Provecho!\n")

    while True:
        print("---------------------------------------------------------")
        print("   Programa de inventario por el equipo nosequenumero.")                                                              
        print("------------------------- MENU --------------------------")   
        print("    ============= SELECCIONE UN NÚMERO =============    ")           
        print (" 1. Registrar ventas.\n" +
            " 2. Añadir o editar un producto.\n" +                     # aqui hice un pequeño rediseño para que el menu en 
            " 3. Registrar llegada de articulos al almacen.\n" +       # el shell sea un poco mas estetico owo
            " 4. Consultar los datos del inventario.\n" + 
            " 5. Consultar datos de las ventas.\n" +
            " 6. Mostrar reportes de ventas por vendedor o articulo.\n" + 
            " 0. Salir del programa\n" + 
            "    ================================================\n" +
            "---------------------------------------------------------")    

        numero = input("Ingresa el número de la función que quieres usar: ")
        print("---------------------------------------------------------")
        if numero == "1":
            registrar_ventas()
        elif numero == "2":
            añadir_o_editar()
        elif numero == "3":
            productos_almacen()
        elif numero == "4":
            consultar_inventario() #Funcion Julian
        elif numero == "5":
            mostrar_datos_venta_producto()
        elif numero == "6":
            ventas_por_vendedor_o_por_articulo()
        elif numero == "0":
            break
        else:
            pass

if __name__ == '__main__':
    main()
