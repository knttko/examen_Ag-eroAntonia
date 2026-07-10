peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
}

cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
}

def leer_opcion():
    opcion=0
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion>=1 and opcion<= 6:
                break
            else:
                print("ingrese una opcion dentro del rango.")
        except ValueError:
            print("ingrese un numero entero")
    return opcion

def cupos_genero(genero):
    acumulador=0
    for i in peliculas:
        if genero.lower()== peliculas[i][1].lower():
            acumulador=acumulador+cartelera[i][1]
    print("El total de cupos disponibles es: ",acumulador)


def busqueda_precio(p_min, p_max):
    lista=[]
    for i in cartelera:
        if peliculas[i][3]=="A":
            if cartelera[i][0]>=p_min and cartelera[i][0]<=p_max:
                A=(peliculas[i][0],"--",i)
                lista.append(A)
            else:
                print("fuera de rango")
        elif peliculas[i][3]=="B":
            if cartelera[i][1]>0:
                B=(peliculas[i][0],"--",i)
                lista.append(B)
            else:
                print("no hay cupos")
    if len(lista)>0:
        lista.sort()
        print("Las peliculas encontradas son: ", lista)
    else:
        print("No hay películas en ese rango de precios.")
        
def buscar_codigo(codigo):
    for i in peliculas:
        if codigo.lower()==i.lower():
            return True
    return False

def actualizar_precio(codigo,nuevo_precio):
    if buscar_codigo(codigo)==True:
        if nuevo_precio>=0:
            cartelera[codigo][0]=nuevo_precio
            return True
    return False


def val_codigo(codigo):
    if (len(codigo.strip().replace(" ", "")) > 0) and codigo.strip() not in peliculas:
        return True
    return False

def val_titulo(titulo):
    if len(titulo.strip().replace(" ", "")) > 0:
        return True
    return False

def val_genero(genero):
    if len(genero.strip().replace(" ", "")) > 0:
        return True
    return False

def val_duracion(duracion):
    if duracion > 0:
        return True
    return False

def val_clasificacion(clasificacion):
    if clasificacion=="A" or clasificacion=="B" or clasificacion=="C":
        return True
    return False

def val_idioma(idioma):
    if len(idioma.strip().replace(" ", "")) > 0:
        return True
    return False

def val_es_3d(es_3d):
    if es_3d.lower()=="s":
        return True
    elif es_3d.lower()=="n":
        return False
    return None

def val_precio(precio):
    if precio >= 0:
        return True
    return False

def val_cupos(cupos):
    if cupos >= 0:
        return True
    return False


def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos):
    if val_codigo(codigo):
        if buscar_codigo(codigo)==False:
            if val_titulo(titulo):
                if val_genero(genero):
                    if val_duracion(duracion):
                        if val_clasificacion(clasificacion):
                            if val_idioma(idioma):
                                if val_es_3d(es_3d) != None:
                                    if val_es_3d(es_3d):
                                        es_3d_val = True
                                    elif val_es_3d(es_3d) == False:
                                        es_3d_val = False                                
                                    if val_precio(precio):
                                        if val_cupos(cupos):
                                            peliculas[codigo] = [titulo, genero, duracion, clasificacion, idioma, es_3d_val]
                                            cartelera[codigo] = [precio, cupos]
                                            return True
    return False
def eliminar_pelicula(codigo):
    if buscar_codigo(codigo)==True:
        del peliculas[codigo]
        del cartelera[codigo]
        return True
    return False

opc=0
while opc!=6:
    print("========== MENÚ PRINCIPAL ==========d")
    print("1. Cupos por género")
    print("2. Búsqueda de películas por rango de precio")
    print("3. Actualizar precio de película")
    print("4. Agregar película")
    print("5. Eliminar película")
    print("6. Salir")
    print("=====================================")
    opc=leer_opcion()
    match opc:
        case 1:
            genero=input("ingrese nombre del genero: ")
            cupos_genero(genero)
        case 2:
            while True:
                try:
                    p_min=int(input("ingrese precio minimo: "))
                    p_max=int(input("ingrese precio maximo: "))
                    if p_min>=0 and p_max>=0 and p_min<=p_max:
                        break
                    else:
                        print("el minimo y maximo debe ser mayor o igual al 0, y el minimo debe ser menor o igual al maximo ")
                except ValueError:
                    print("Debe ingresar valores enteros")
            busqueda_precio(p_min,p_max)
        
        case 3:
            codigo=input("ingrese codigo de la pelicula: ")
            act="s"
            while act.lower()=="s":
                try:
                    nuevo_precio=int(input("ingrese nuevo precio: "))
                    if actualizar_precio(codigo,nuevo_precio)==True:
                        print("precio actualizado")
                    else:
                        print("el codigo no existe")
                except ValueError:
                    print("Debe ingresar un numero entero")
                act=input("¿desea actualizar otro precio (s/n)?: ")
            
        case 4:
            codigo=input("ingrese codigo de la pelicula: ")
            titulo=input("ingrese titulo: ")
            genero=input("ingrese genero: ")
    
            try:
                duracion=int(input("ingrese duracion: "))
            except ValueError:
                print("Debe ingresar un numero entero")
            
            clasificacion=input("ingrese clasificacion: ")
            idioma=input("ingrese  idioma: ")
            es_3d=input("¿Es 3D (s/n)?: ")
    
            try:
                precio=int(input("ingrese precio: "))
            except ValueError:
                print("Debe ingresar un valor entero")
            try:
                cupos=int(input("ingrese cupos: "))
            except ValueError:
                print("Debe ingresar un valor entero")
                
            if agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos):
                print("pelicula agregada")
    
            else:
                print("el codigo ya existe")
        
        case 5:
            codigo=input("ingrese el codigo de la pelicula a eliminar: ")
            if eliminar_pelicula(codigo)==True:
                print("pelicula eliminada")
            else:
                print("el codigo no existe")
        case 6:
            print("Programa finalizado.")
            