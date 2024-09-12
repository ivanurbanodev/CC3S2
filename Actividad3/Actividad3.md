
# Repositorio de la actividad3

https://github.com/ivanurbanodev/Actividad3.git

# Preguntas:
## 1. ¿Cómo te ha ayudado Git a mantener un historial claro y organizado de tus cambios?

Git es muy util ya que guarda un historial detallado de cada cambio con mensajes que explican qué se hizo inclusive se puede revisar cualquier cambio pasado y saber cuándo se hizo.

## 2. ¿Qué beneficios ves en el uso de branches para desarrollar nuevas características o corregir errores?

 Los branches son muy utiles porque nos permite trabajar en nuevas características o correcciones sin afectar el codigo fuente además que facilita la colaboración entre desarrolladores.

## 3. Realiza una revisión final del historial de commits para asegurarte de que todos los cambios

Usemos el comando para revisar el historial:
**git log --oneline --graph** :

```bash
*   dc4c678 (HEAD -> main) Merge branch 'feature/new-feature' into main
|\  
| * 115fc06 saludo
* | 88e6d65 (hotfix/bugfix) abc1234
|/  
* 4d0a413 (feature/login, feature/another-new-feature2, feature/another-new-feature, develop) Add main.py
* e0b1c7c Set up the repository base documentation
* ff23f23 Initial commit with README.md
(END)
```

podemos verificar que los cambios se realizaron correctamente

## 4. Revisa el uso de branches y merges para ver cómo Git maneja múltiples líneas de desarrollo.

 Git maneja las ramas permitendo varias líneas de desarrollo, mientars los merges combinan esos cambios. Si hay conflictos, Git te permite resolverlos de manera manual antes de la fusión.
