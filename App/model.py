﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
# Construccion de modelos

def newCatalog():

    catalog= {'videos': None, 
              'category': None}

    catalog['videos'] = lt.newList()
    catalog['category'] = lt.newList('ARRAY_LIST',
                                     cmpfunction=comparecategory)
    return catalog
    
# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):

    lt.addLast(catalog['videos'], video)
    categorias = video['categorias'].split(",")
    for category in categorias:
        addCategory(catalog, category.strip(), video)

def addCategory(catalog, categoria):

    categorias = catalog['categorias']
    poscategory = lt.isPresent(categorias, categoria)
    if poscategory > 0:
        category = lt.getElement(categorias, poscategory)
    else:
        category = newCategory(categoria)
        lt.addLast(categorias, category)
    lt.addLast(category['videos'], categoria)


# Funciones para creacion de datos

def newCategory(name):

    category = {'name': "", "videos": None, "views": 0}
    category['name'] = name
    category['videos'] = lt.newList('ARRAY_LIST')
    return category

# Funciones de consulta

def getVideosByCategory(catalog, categoria):

    poscategory = lt.isPresent(catalog['categorias'], categoria)
    if poscategory > 0:
        category = lt.getElement(catalog['categorias'], poscategory)
        return category
    return None

def getBestVideos(catalog, number):

    videos = catalog['videos']
    bestvideos = lt.newList()
    for cont in range(1, number+1):
        video = lt.getElement(videos, cont)
        lt.addLast(bestvideos, video)
    return bestvideos

# Funciones utilizadas para comparar elementos dentro de una lista

def compareviews(video1, video2):
    return (float(video1['views']) > float(video2['views']))

def comparecategory(categoria1, category):

    if(categoria1.lower() in category['name'].lower()):
        return 0
    return -1
def cmpVideosByViews(video1, video2):
    
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'views'
    video2: informacion del segundo video que incluye su valor 'views'
    """
    views1 = False
    if (float(video2['views'])) > (float(video1['views'])):
        views1 = True
    return views1   

# Funciones de ordenamiento

def subList(lst, pos, numelem):
    """ Retorna una sublista de la lista lst.

    Se retorna una lista que contiene los elementos a partir de la
    posicion pos, con una longitud de numelem elementos.
    Se crea una copia de dichos elementos y se retorna una lista nueva.

    Args:
        lst: La lista a examinar
        pos: Posición a partir de la que se desea obtener la sublista
        numelem: Numero de elementos a copiar en la sublista

    Raises:
        Exception
    """
    try:
        return lt.subList(lst, pos, numelem)
    except Exception as exp:
        error.reraise(exp, 'List->subList: ')

def sortVideos(catalog):
    sa.sort(catalog['videos'], compareviews)

def sort(lst, cmpfunction):
    size = lt.size(lst)
    pos1 = 1
    while pos1 < size:
        minimum = pos1    # minimun tiene el menor elemento
        pos2 = pos1 + 1
        while (pos2 <= size):
            if (cmpfunction(lt.getElement(lst, pos2),
               (lt.getElement(lst, minimum)))):
                minimum = pos2  # minimum = posición elemento más pequeño
            pos2 += 1
        lt.exchange(lst, pos1, minimum)  # elemento más pequeño -> elem pos1
        pos1 += 1
    return lst

def insertionVideos(lst, lessfunction):
    size = lt.size(lst)
    pos1 = 1
    while pos1 <= size:
        pos2 =pos1
        while (pos2 > 1) and (lessfunction(lt.getElement(lst, pos2), lt.getElement(lst, pos2-1))):
            lt.exchange(lst, pos2, pos2-1)
            pos2 -=1
        pos1 +=1
    return lst

def shellVideos(lst, lessfunction):
    n = lt.size(lst)
    h = 1
    while h < n/3:
        h = 3*h + 1
    while(h >= 1):
        for i in range(h,n):
            j = i
            while (j >= h) and (lessfunction(lt.getElement(lst, j+1), lt.getElement(lst, j-h+1))):
                lt.exchange(lst, j+1, j-h+1)
                j -= h
        h //=3
    return lst

