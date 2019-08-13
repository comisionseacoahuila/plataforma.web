#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Sitio web https://www.comisionseacoahuila.mx
SITEURL = 'https://comisionseacoahuila.github.io'
SITENAME = 'Comisión de Selección del SEA Coahuila'
SITELOGO = 'theme/images/generic_company.png'
SITEDESCRIPTION = 'Comisión de Selección SEA Coahuila'
SITETWITTER = '@comselcc'

# Autor
AUTHOR = 'webmaster'

# Directorio donde esta el contenido
PATH = 'content'

# Directorios que tienen los articulos
ARTICLE_PATHS = ['sala-de-prensa']

# Directorios que tienen páginas fijas, no artículos
PAGE_PATHS = ['3de3', 'documentacion', 'procesos', 'quienes-somos']

# Directorios y archivos que son fijos
# Agregue también los directorios que tienen archivos para artículos y páginas
STATIC_PATHS = [
    'favicon.ico',
    'LICENSE',
    'README.md',
    'robots.txt',
    '3de3',
    'documentacion',
    'formato-unico',
    'procesos',
    'quienes-somos',
    'sala-de-prensa',
    ]

# Encabezados para las categorías
CATEGORIES_TITLES = {
    '3de3': '3 de 3',
    'documentacion': 'Documentación',
    'procesos': 'Procesos',
    'quienessomos': 'Quienes somos',
    'sala-de-prensa': 'Sala de Prensa',
    }

# Usar el nombre del directorio como la categoría
USE_FOLDER_AS_CATEGORY = True

# Los artículos van en directorios categoria/titulo/
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'

# Las páginas fijas van en directorios categoria/titulo/
PAGE_URL = '{category}/{slug}/'
PAGE_SAVE_AS = '{category}/{slug}/index.html'

# Tema
THEME = 'themes/startbootstrap-agency'

# Lenguaje y zona horaria
DEFAULT_LANG = 'es'
TIMEZONE = 'America/Mexico_City'

# Para desarrollo, los vinculos son relativos
RELATIVE_URLS = True

# Para desarrollo, se desactiva la paginacion
DEFAULT_PAGINATION = False

# Para desarrollo, no hay cargas desde Internet
USE_REMOTE_SERVICES = False

# Para desarrollo, borrar todo output
DELETE_OUTPUT_DIRECTORY = True

# No eliminar de output los siguientes directorios y archivos
OUTPUT_RETENTION = ['.git', '.gitignore']

# Siempre aprovechar lo que se tenga en caché
LOAD_CONTENT_CACHE = True

# Para desarrollo se desactiva la generacion de feeds
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
