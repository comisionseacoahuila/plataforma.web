
# Comisión SEA Coahuila - plataforma.web

Creador del sitio web de la Comisión de Selección del SEA Coahuila hecho con Pelican

### Apuntes

Para crear los vínculos a los archivos PDF

    $ find . -name "*.pdf" -printf '[%P](%P)\n' | sort > list.txt
