
# 8. Documentación y reflexión

### Documentación de los comandos usados y resultados obtenidos

1. **Inicialización del proyecto**
   ```bash
   # Se creó un directorio para realizar la actividad.
   $ mkdir proyecto-colaborativo
   $ cd proyecto-colaborativo
   ```
  
   Resultado: Se creó el proyecto local.(no se uso git init ya que ya tenemos la rama main lista de actividades antriores)

2. **Creación de un archivo de texto y primer commit**
   ```bash
   # Se creó un archivo de texto con contenido inicial y se agrega al área de staging y se hace commit.
   $ echo "Este es el contenido inicial del proyecto" > archivo_colaborativo.txt
   $ git add .
   $ git commit -m "Commit inicial con contenido base"
   ```
   
   Resultado: El archivo `archivo_colaborativo.txt` fue agregado y comiteado.

3. **Creación de la rama `feature-branch` y cambios**
   ```bash
   # Se creó la nueva rama feature-branch y se realiza un cambio en el archivo.
   $ git branch feature-branch
   $ git checkout feature-branch
   $ echo "Este es un cambio en la feature-branch" >> archivo_colaborativo.txt
   $ git add .
   $ git commit -m "Cambios en feature-branch"
   ```
   
   Resultado: Se creó la rama `feature-branch` y se hizo un commit con cambios en `archivo_colaborativo.txt`.

4. **Cambios en la rama `main`**
   ```bash
   # Se regresa a main y se hace un cambio en el archivo.
   $ git checkout main
   $ echo "Este es un cambio en la rama main" >> archivo_colaborativo.txt
   $ git add .
   $ git commit -m "Cambios en main"
   ```
   
   Resultado: Se hicieron cambios en la misma línea del archivo en `main`.

5. **Fusión y conflictos**
   ```bash
   # Cuando se intenta fusionar y surgen conflictos de fusión.
   $ git merge feature-branch
   $ git status
   ```
   
   Resultado: Al intentar la fusión, surgió un conflicto en `archivo_colaborativo.txt` ya que se cambio la misma linea en diferentes ramas.

6. **Resolución de conflictos**
   ```bash
   # Se resuelvió el conflicto de fusión aceptando los cambios de feature-branch.
   $ git checkout --theirs archivo_colaborativo.txt # Aceptar cambios de feature-branch
   $ git add .
   $ git commit -m "Conflictos resueltos"
   ```
   
   Resultado: Se resolvió el conflicto aceptando los cambios de `feature-branch`.

![[Pasted image 20240917234241.png]]


7. **Simulación de fusión y uso de git diff**
   ```bash
   # Se simula una fusión sin confirmar con --no-commit para ver los cambios antes del merge.
   $ git merge --no-commit --no-ff feature-branch
   $ git diff --cached
   $ git merge --abort
   ```
   
   Resultado: Se simuló la fusión y se observaron los cambios en el área de staging, luego se abortó la fusión.

![[Pasted image 20240917220726.png]]

![[Pasted image 20240917220516.png]]



8. **Uso de `git mergetool`**
   ```bash
   # Se configura la herramienta visual de fusión (meld en este caso) y se inicia para resolver conflictos.
   $ git config --global merge.tool vscode
   $ git config --global mergetool.vscode.cmd "code --wait $MERGED"
   $ git mergetool
   ```
  
   Resultado: Se configuró `vscode` como la herramienta de fusión y se usó para resolver conflictos.
   Se observan los conflictos.
   ![[Pasted image 20240917232303.png]]
   en esta ocasión se escoge Accept Both Changes y se obtiene lo siguiente:
   ![[Pasted image 20240917232340.png]]
   
Luego se guarda y se commitea termianndo la fusión.

![[Pasted image 20240917233339.png]]

![[Pasted image 20240917233438.png]]

9. **Uso de `git revert` y `git reset`**
   ```bash
   # Se revierte un commit erróneo 
   $ git revert 08c4c26 # Revertir un commit especificado
   ```
![[Pasted image 20240917235418.png]]

![[Pasted image 20240917235453.png]]

   Resultado: PAra probar `git revert` se creo un archivo y se le comiteo y al hacer revert se nota que se elimina ya que deshace los cambios de ese commit creando un nuevo commit.

   ```bash
   $ git reset --mixed 08c4c26 # Reestructurar el historial de commits
   ```
   ![[Pasted image 20240918000636.png]]
![[Pasted image 20240918000734.png]]
   
   Resultado: Para probar que `git reset --mixed`  quita archivos del staging area se agrega al staging area a un archivo que creamos llamado hola.txt  y para reestructurar el historial sin perder los cambios no comiteados ejecutamos `git reset --mixed`.
   Al ejecutar git status podemos onservar que quito a hola.txt del staging area y que conservó el directorio de trabajo, ya que `git reset --mixed` conserva los cambios no commiteados. 
10. **Versionado semántico**
    ```bash
    # Se marca la primera versión estable del proyecto usando un tag con versionado semántico.
    $ git tag -a v1.0.0 -m "Primera versión estable"
    $ git push origin v1.0.0
    ```

      ![[Pasted image 20240918001546.png]]
    Resultado: Se creó una etiqueta `v1.0.0` para marcar la primera versión estable del proyecto.
    
11. **Uso de `git bisect` para depuración**
    ```bash
    # Se utiliza git bisect para encontrar el commit malo.
    $ git bisect start
    $ git bisect good
    $ git bisect bad
    $ git bisect reset
    ```
   
	Resultado: Se utilizó `git bisect` para identificar el commit que introdujo un error, probando cada commit intermedio hasta encontrar el problemático, para la demostración de como funciona `git bisect` se crearon 5 commits adicionales y se etiquetó al primero como bueno y el ultimo como malo y sea realizó la búsqueda del commit malo.
    
		![[Pasted image 20240918002036.png]]
---

### Reflexión sobre la utilidad de los comandos

- **`git init` y `git add/commit`** estos comandos sirven para iniciar el control de versiones y poder capturar sus cambios. Permiten llevar un historial claro durante el desarrollo.
- **`git branch` y `git checkout`** estos comandos nos crear y cambiar entre diferentes ramas, esto es muy importante para un desarrollo colaborativo.
- **`git merge`**  este comando es fundamental para integrar ramas y garantiza el trabajo colaborativo.
- **`git mergetool`** es un comando  útil cuando hay conflictos y necesitamos ayuda de herramientas gráficas para visualizar y solucionar de maneraa mas efectiva los conflictos.
- **`git revert` y `git reset`** estos son comandos para corregir errores en el historial de commits. `git revert` ayuda mantener el historial mas claro creando un commit nuevo del que queremos restaurar, mientras que `git reset` permite hacer correcciones más dificiles eliminando commits y manteniedo nuestro directorio de trabajo intacto.
- los versionados semánticos y tags nos ayudan a marcar momentos importantes en el desarrollo, y así poder hacer un seguimiento de versiones estables.
- **`git bisect`** es una herramienta excelente encontrar el commit que introdujo un error en grandes proyectos, usando el algoritmo de búsqueda binaria.

Estos comandos nos ayudan a gestionar código de manera mas eficiente y por ese motivo estos comandos son esenciales en un flujo de trabajo de DevOps, ya que nos ayudan a  trabajar colaborativamente, solucionar problemas y mantener un historial de cambios limpio.
