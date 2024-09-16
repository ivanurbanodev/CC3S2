
# Preguntas de discusión

## 1. ¿Por qué se considera que rebase es más útil para mantener un historial de proyecto lineal en comparación con merge?

 Esto se debe a que rebase reescribe el historial moviendo commits a una nueva rama haciendo que el historial sea más fácil de leer y depurar.

## 2. ¿Qué problemas potenciales podrían surgir si haces rebase en una rama compartida con otros miembros del equipo?

Como rebase reescribe el historial puede causar conflictos entre colaboradores si ya han comenzado a trabajar en esa rama, además no se sabrá cuando se agregó nuevas caracteristicas y quienes son los autores.
## 3. ¿En qué se diferencia cherry-pick de merge, y en qué situaciones preferirías uno sobre el otro?

LA diferencia es que mientras merge une todo el historial de una rama en otra, cherry-pick selecciona commits individuales. Cherry-pick es mas conveniente cuando se necesite aplicar commits específicos, sin necesidad de traer toda el historial de la rama.

## 4. ¿Por qué es importante evitar hacer rebase en ramas públicas?

Porque  como hemos dicho antes rebase reescribe el historial y esto podría causar que los desarrolladores configuren de diferentes maneras esa rama, generando problemas de coordinación durante el desarrolo.

