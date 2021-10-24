# -*- coding: utf-8 -*-

from nombres import *

################################################################
#  Funciones de test
################################################################

def test_filtrar_por_genero(registros):
  pass     

def test_calcular_nombres(registros):
  pass     

def test_calcular_top_nombres_de_año(registros):
  pass     

def test_calcular_nombres_ambos_generos(registros):
  pass     
    
def test_calcular_nombres_compuestos(registros):
  pass     

def test_calcular_nombre_mas_frecuente_por_año(registros):
  pass   

def test_calcular_frecuencia_por_año(registros):
  pass   

def test_mostrar_evolucion_por_año(registros):
  pass
  
def test_calcular_frecuencia_acumulada(registros):
  pass

def test_calcular_frecuencias_por_nombre(registros):
  pass     

def test_mostrar_frecuencias_nombres(registros):
  pass     

################################################################
#  Programa principal
################################################################

registros = leer_frecuencias_nombres('./data/frecuencias_nombres.csv')
print(registros[:10], "\n")

#test_filtrar_por_genero(registros)
#test_calcular_nombres(registros)
#test_calcular_top_nombres_de_año(registros)
#test_calcular_nombres_ambos_generos(registros)
#test_calcular_nombres_compuestos(registros)
#test_calcular_nombre_mas_frecuente_por_año(registros)
#test_calcular_frecuencia_por_año(registros)
#test_mostrar_evolucion_por_año(registros)
#test_calcular_frecuencia_acumulada(registros)
#test_calcular_frecuencias_por_nombre(registros)
#test_mostrar_frecuencias_nombres(registros)
