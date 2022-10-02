# -*- coding: utf-8 -*-
''' Análisis de frecuencias de nombres

AUTOR: José A. Troyano
REVISOR: Toñi Reina
ÚLTIMA MODIFICACIÓN: 13/11/2019
   
En este proyecto trabajaremos con datos correspondientes a los nombres de las
personas nacidas en España desde 2002 a 2017. Los datos están tomados del Instituto
Nacional de Estadística (https://www.ine.es/), donde se pueden encontrar muchos datos interesantes
principalmente sobre la demografía, economía, y sociedad españolas. Representaremos 
la información de entrada mediante listas de tuplas, y a partir de esta estructura implementaremos
una serie de funciones que nos permitirán realizar varios tipos de consultas y generar visualizaciones.
 
FORMATO DE ENTRADA :
-------------------
Trabajaremos con ficheros en formato CSV. Cada registro del fichero de entrada ocupa
una línea y contiene cuatro informaciones sobre los nombres (año, nombre, frecuencia, genero). 
Estas son las primeras líneas de un fichero de entrada:
   
    Año,Nombre,Frecuencia,Género
    2002,ALEJANDRO,8020,Hombre
    2002,PABLO,5799,Hombre
    2002,DANIEL,5603,Hombre
    2002,DAVID,5414,Hombre
    2002,ADRIAN,4949,Hombre
    2002,JAVIER,4909,Hombre
    2002,ALVARO,4595,Hombre
    2002,SERGIO,3744,Hombre

FUNCIONES A IMPLEMENTAR:
------------------------
- lee_registros(fichero):
    lee el fichero de registros y devuelve una lista de tuplas con nombre
- filtrar_por_genero(registros, genero):
    recibe una lista de tuplas y devuelve solo los registros del género recibido como parámetro
- calcular_nombres(registros, filtro=None):
    calcula el conjunto de nombres aplicando el filtro de género recibido como parámetro
- calcular_top_nombres_de_año(registros, año, limite=10, filtro=None):
    calcula los nombres más frecuentes de un año
- calcular_nombres_ambos_generos(registros):
    calcula el conjunto de nombres que han sido usados en ambos géneros
- calcular_nombres_compuestos(registros, filtro=None):
    calcula el conjunto de nombres con más de una palabra
- calcular_nombre_mas_frecuente_por_año(registros, filtro=None):
    calcula una lista de tuplas (año, nombre) con el nombre más frecuentes cada año
- calcular_frecuencia_por_año(registros, nombre):
    calcula una lista de tuplas (año, frecuencia) con las frecuencias de un nonmbre cada año
- mostrar_evolucion_por_año(registros, nombre):
    genera un gráfico con la evolución de la frecuencia de un nombre
- calcular_frecuencia_acumulada(registros, nombre):
    calcula la frecuencia acumulada de un nombre en todos los años
- calcular_frecuencias_por_nombre(registros):
    calcula un diccionario {nombre:frecuencia} con la frecuencia acumulada de cada nombre
- mostrar_frecuencias_nombres(registros, limite=10):
    genera un diagrama de barras con las frecuencias de los nombres más populares
'''

import csv
from collections import namedtuple, defaultdict
from matplotlib import pyplot as plt

# EJERCICIO 1:

Registro = namedtuple('Registro', 'año, nombre, frecuencia, genero')

def leer_frecuencias_nombres(fichero):
    ''' Lee el fichero de registros y devuelve una lista de tuplas con nombre
    
    ENTRADA: 
       - fichero: nombre del fichero de entrada -> str
    SALIDA: 
       - lista de registros (año, nombre, frecuencia, género) -> [Registro(int, str, int, str)]
    '''
    with open(fichero, 'r', encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        registros = [Registro(int(año), nombre, int(frecuencia), genero) 
                     for año, nombre, frecuencia, genero in lector]
    return registros


# EJERCICIO 2:
def filtrar_por_genero(registros, genero):
    ''' Recibe una lista de tuplas y devuelve solo los registros del género recibido como parámetro
    
    ENTRADA: 
       - registros: lista de registros (año, nombre, frecuencia, género) -> [Registro(int, str, int, str)]
       - genero: del que se seleccionarán los registros -> str
    SALIDA: 
       - lista de registros seleccionados -> [Registro(int, str, int, str)]
    '''
    return [r for r in registros if r.genero==genero]


# EJERCICIO 3:
def calcular_nombres(registros, filtro=None):
    ''' Calcula el conjunto de nombres aplicando el filtro de género recibido como parámetro 
    
    ENTRADA: 
       - registros: lista de registros (año, nombre, frecuencia, género) -> [Registro(int, str, int, str)]
       - filtro: 'Hombre', 'Mujer', o None si no se aplica filtro  -> str
    SALIDA: 
       - conjunto de nombres encontrados -> {str}
    '''
    if filtro is not None:
        registros = filtrar_por_genero(registros, filtro)

    return set(r.nombre for r in registros)


# EJERCICIO 4:
def calcular_top_nombres_de_año(registros, año, limite=10, filtro=None):
    ''' Calcula los nombres más frecuentes de un año
    
    ENTRADA: 
       - registros: lista de registros (año, nombre, frecuencia, género) -> [Registro(int, str, int, str)]
       - año: del que se hace la consulta -> int
       - limite: número de nombres a recuperar -> int
       - filtro: 'Hombre', 'Mujer', o None si no se aplica filtro  -> str
    SALIDA: 
       - lista de tuplas (nombre, frecuencia) ordenanda de mayor a menor frecuencia  -> [(str, int)]
    '''
    if filtro is not None:
        registros = filtrar_por_genero(registros, filtro)

    resultado = [(r.nombre, r.frecuencia) for r in registros if r.año==año]
    resultado.sort(key=lambda x:x[1], reverse=True)
    
    # EJEMPLOS:
    # -----------------------------------
    # students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
    # Ordenación ASCENDETE por edad
    # sorted(students, key=lambda x:x[2])
    # Resultado:
    # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
    # -----------------------------------
    # students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
    # Ordeación DESCENDIENTE por edad
    # sorted(students, key=lambda x:x[2], reverse=True)
    # Resultado:
    # [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
    # -------------------------------------
    # L=[('b',2),('a',1),('c',3),('d',4)]
    # Uso parámetro cmp para ordenar
    # sorted(L, cmp=lambda x,y:cmp(x[1],y[1]))
    # Resultado:
    # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

    return resultado[:limite]


# EJERCICIO 5:
def calcular_nombres_ambos_generos(registros):
    ''' Calcula el conjunto de nombres que han sido usados en ambos géneros
    
    ENTRADA: 
       - registros: lista de registros (año, nombre, frecuencia, género) -> [Registro(int, str, int, str)]
    SALIDA: 
       - conjunto de nombres comunes a ambos géneros  -> {str}
    '''
    nombres_hombres = calcular_nombres(registros, 'Hombre')
    nombres_mujeres = calcular_nombres(registros, 'Mujer')

    return nombres_hombres.intersection(nombres_mujeres)


# EJERCICIO 6:
def calcular_nombres_compuestos(registros, filtro=None):
    ''' Calcula el conjunto de nombres con más de una palabra
    
    ENTRADA: 
       - registros: lista de registros (año, nombre, frecuencia, género) -> [Registro(int, str, int, str)]
       - filtro: 'Hombre', 'Mujer', o None si no se aplica filtro  -> str
    SALIDA: 
       - conjunto de nombres con más de una palabra  -> {str}
    '''
    nombres = calcular_nombres(registros, filtro)
    return {n for n in nombres if ' ' in n}


# EJERCICIO 7:
def calcular_nombre_mas_frecuente_por_año(registros, filtro=None):
    ''' Calcula una lista de tuplas (año, nombre) con el nombre más frecuentes cada año
    
    ENTRADA: 
       - registros: lista de registros (año, nombre, frecuencia, género) -> [Registro(int, str, int, str)]
       - filtro: 'Hombre', 'Mujer', o None si no se aplica filtro  -> str
    SALIDA: 
       - lista de tuplas (año, nombre, frecuencia) ordenanda por año  -> [(int, str, int)]
       
    Se calculará en primer lugar la lista de años y, posteriormente, se buscará el nombre
    más frecuente para cada año.
    '''
    if filtro is not None:
        registros = filtrar_por_genero(registros, filtro)
        
    # Monta el conjunto de valores ordenado (años)
    años = sorted(set(r.año for r in registros))
    
    # Inicializa la lista
    nombres_mas_frecuentes = []

    for año in años:

        # Contiene todos los registros que cumplen la condición (if)
        registros_año = [r for r in registros if r.año==año]
        
        # Usa dos variables (nombre y frecuencia) para recoger el nombre que 
        # tiene la frecuencia mayor. 
        _, nombre, frecuencia, _ = max(registros_año, key=lambda r:r.frecuencia)

        # Usa la variable del for (año) y las obtenidas anteriormente (nombre y frecuencia)
        nombres_mas_frecuentes.append((año, nombre, frecuencia))
                                      
    return nombres_mas_frecuentes


# EJERCICIO 8:
def calcular_frecuencia_por_año(registros, nombre):
    ''' Calcula una lista de tuplas (año, frecuencia) con las frecuencias de un nonmbre cada año
    
    ENTRADA: 
       - registros: lista de registros (año, nombre, frecuencia, género) -> [Registro(int, str, int, str)]
       - nombre: del que se hace la consulta  -> str
    SALIDA: 
       - lista de tuplas (año, frecuencia) ordenanda por año  -> [(int, int)]
       
    En el caso de que un nombre se use para hombres y mujeres, se sumarán ambas frecuencias
    '''
    
    # Monta el conjunto de valores ordenado (años)
    años = sorted(set(r.año for r in registros))
    
    # Inicializa la lista
    frecuencia_por_año = []
    
    for año in años:
    
        frecuencia = sum(r.frecuencia for r in registros if r.año==año and r.nombre==nombre)
        frecuencia_por_año.append((año, frecuencia))
                                      
    return frecuencia_por_año
    

# EJERCICIO 9:
def mostrar_evolucion_por_año(registros, nombre):
    ''' Genera un gráfico con la evolución de la frecuencia de un nombre
    
    ENTRADA: 
       - registros: lista de registros (año, nombre, frecuencia, género) -> [Registro(int, str, int, str)]
       - nombre: del que se hace la consulta  -> str
    SALIDA EN PANTALLA: 
       - curva con la evolución de la frecuencia del nombre
    
    Se usarán las siguientes instrucciones para generar la gráfica:
        plt.plot(años, frecuencias)
        plt.title("Evolución del nombre '{}'".format(nombre))
        plt.show()
    Donde 'años' y 'frecuencias' se extraen del resultado de la función
    'calcular_frecuencia_por_año'
    '''

    años_frecuencias = calcular_frecuencia_por_año(registros, nombre)
    años = [año for año,_ in años_frecuencias]
    
    frecuencias = [frecuencia for _,frecuencia in años_frecuencias]
    
    plt.plot(años, frecuencias)
    plt.title("Evolución del nombre '{}'".format(nombre))
    plt.show()


# EJERCICIO 10:
def calcular_frecuencia_acumulada(registros, nombre):
    ''' Calcula la frecuencia acumulada de un nombre en todos los años
    
    ENTRADA: 
       - registros: lista de registros (año, nombre, frecuencia, género) -> [Registro(int, str, int, str)]
       - nombre: del que se hace la consulta  -> str
    SALIDA: 
       - suma de las frecuencias del nombre en todos los años  -> int
    '''
    return sum(r.frecuencia for r in registros if r.nombre==nombre)


# EJERCICIO 11:
def calcular_frecuencias_por_nombre(registros):
    ''' Calcula un diccionario {nombre:frecuencia} con la frecuencia acumulada de cada nombre
    
    ENTRADA: 
       - registros: lista de registros (año, nombre, frecuencia, género) -> [Registro(int, str, int, str)]
    SALIDA: 
       - diccionario con la frecuencia acumulada de cada nombre -> {str:int}
    '''
    # Los diccionarios se utilizan para almacenar valores de datos en pares (clave, valor) 
    frecuencias = dict()
    
    nombres = calcular_nombres(registros)
    
    for nombre in nombres:
        frecuencias[nombre] = calcular_frecuencia_acumulada(registros, nombre)
    return frecuencias

    '''
    # Solución alternativa un poco más eficiente, de O(n)
    frecuencias = defaultdict(int)
    for r in registros:
        frecuencias[r.nombre] += r.frecuencia
    return frecuencias
    '''


# EJERCICIO 12:
def mostrar_frecuencias_nombres(registros, limite=10):
    ''' Genera un diagrama de barras con las frecuencias de los nombres más populares
    
    ENTRADA: 
       - registros: lista de registros (año, nombre, frecuencia, género) -> [Registro(int, str, int, str)]
       - limite: número de nombres a mostrar -> int
    SALIDA EN PANTALLA: 
       - diagrama de barras con las frecuencias de los nombres más populares
    
    Se usarán las siguientes instrucciones para generar la gráfica:
        plt.bar(nombres, frecuencias)
        plt.xticks(rotation=80)
        plt.title("Frecuencia de los {} nombres más comunes".format(limite))
        plt.show()
        
    Donde 'nombres' y 'frecuencias' se extraen del resultado de la función
    'calcular_frecuencias_por_nombre'. El cálculo de los nombres más populares se puede
	realizar ordenando las claves del diccionario devuelto por 'calcular_frecuencias_por_nombre'
	en función de sus valores asociados.
    '''
    frecuencias_nombres = calcular_frecuencias_por_nombre(registros)
    nombres = sorted(frecuencias_nombres, key=frecuencias_nombres.get, reverse=True)[:limite]
    frecuencias = [frecuencias_nombres[nombre] for nombre in nombres]
    
    plt.bar(nombres, frecuencias)
    plt.xticks(rotation=80)
    plt.title("Frecuencia de los {} nombres más comunes".format(limite))
    plt.show()
