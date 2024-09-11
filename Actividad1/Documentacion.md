
# Documentación 

## Configuración del entorno

### 1. Inicialización del proyecto Node.js

Lo primero que se hizo fue hacer un proyecto en Node.js

1. Crear un directorio llamado **devops-practice** :
   ```bash
   mkdir devops-practice
   cd devops-practice
   ```

2. Se inició el proyecto  con el siguiente comando:
   ```bash
   npm init -y
   ```

### 2. Instalación de dependencias

Se usaron los frameworks  express para el API REST, Jest y supertest para las pruebas. Estos se instalaron con los siguientes comandos:

```bash
npm install express jest suopertest
```

### 3. Estructura del proyecto

El proyecto fue estructurado según los lineamientos y se usaron los siguientes comandos para crear los directorios y  archivos.
```bash
mkdir src tests
touch src/app.js tests/app.test.js
```

- **src/app.js** En este archivo está la logica del API REST.
 - **tests/app.test.js** En este archivo se encuentran los test.



### 4. Implementación de la API en **src/app.js**

El API REST  responde con **Hello, World!** a la solicitud GET en la raíz (`/`), se configuró para que el servidor solo se inicie cuando el archivo se ejecute directamente, esto para no tener problemas cuando el test lo importe.

```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello, World!');
});

// Solo inicia el servidor si este archivo se está ejecutando directamente
if (require.main === module) {
  const port = process.env.PORT || 3000;
  app.listen(port, () => {
    console.log(`Server running on port ${port}`);
  });
}

module.exports = app;
```

### 5. Pruebas con Jest  y Supertest en  **tests/app.test.js**

La prueba verifica que el API responda con **Hello, World!**.

```javascript
const request = require('supertest');
const app = require('../src/app');

describe('GET /', () => {
  let server;

  beforeAll(() => {
    server = app.listen(0); // Usar 0 permite que el sistema asigne un puerto libre
  });

  afterAll((done) => {
    server.close(done); // Cierra el servidor después de las pruebas
  });

  it('should return Hello, World!', async () => {
    const res = await request(app).get('/');
    expect(res.statusCode).toEqual(200);
    expect(res.text).toBe('Hello, World!');
  });
});
```

### 6. Configuración de Jest en package.json

Se configuró el test en el archivo **package.json** para usar Jest con la opción **--detectOpenHandles** para detectar puertos no cerrados.

```json
{
  "name": "devops-practice",
  "version": "1.0.0",
  "scripts": {
    "test": "jest --detectOpenHandles"
  },
  "dependencies": {
    "express": "^4.17.1"
  },
  "devDependencies": {
    "jest": "^27.0.0",
    "supertest": "^6.3.4"
  }
}
```

---

## Pipeline CI/CD 

## Configura integración continua (CI) con GitHub Actions

Se configuró GitHub Actions para ejecutar el pipeline que hace lo siguiente:
 
1. **Revisa del código (checkout)**: 
   Utiliza  **checkout@v2** para clonar el repositorio en la máquina virtual.

2. **Instala Node.js**: 
   Configura la versión de Node.js con **setup-node@v2**.

3. **Instala de dependencias**:
   Con **npm install** instala dependencias.

4. **Verifica de versiones de Docker y Docker Compose**:
   Ejecutar  los comandos **docker --version** y **docker compose version** apra asegurarse de que Docker y Docker Compose estén instalados con la versión correcta.

5. **Construye y ejecuta con Docker Compose**:
   Construir la imagen de Docker y ejecutar el servicio .

6. **Ejecuta pruebas**:
   Ejecutar las pruebas dentro del contenedor usando **docker exec**.

7. **Detiene y limpia**:
   Detiene y elimina los contenedores y redes creados durante el proceso.

Archivo **ci.yml**:

```yaml
name: CI Pipeline

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '14'

      - name: Install dependencies
        run: npm install
        working-directory: Actividad1/devops-practice

      - name: Check Docker and Docker Compose versions
        run: |
          docker --version
          docker compose version

      - name: Build and run Docker Compose
        run: |
          docker compose up --build -d
        working-directory: Actividad1/devops-practice

      - name: Run tests
        run: docker exec devops-practice-app npm test

      - name: Stop and clear docker compose
        run: |
          docker compose down
        working-directory: Actividad1/devops-practice
```

---
##  Subir el código a GitHub:

###  Crea un nuevo repositorio en GitHub y empuja tu código:

```bash
 git init 
 git add .
 git commit -m "CC3S2"
 git branch -M main
 git remote add origin https://github.com/ivanurbanodev/CC3S2.git
 git push -u origin

   ```
 
---

## Configura entrega continua (CD) con Docker

### 1. Creación del archivo Dockerfile

Archivo **Dockerfile**:

```dockerfile
# Usa la imagen oficial de Node.js
FROM node:14

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos package.json y package-lock.json
COPY package*.json ./

# Instala las dependencias
RUN npm install

# Copia el resto de los archivos de la aplicación
COPY . .

# Expone el puerto en el que la aplicación correrá
EXPOSE 3000

# Comando para iniciar la aplicación
CMD ["node", "src/app.js"]
```

### 2. Construcción y ejecución de la imagen Docker

Con el Dockerfile se construyó la imagen con el comando:

```bash
docker build -t devops-practice .
```

### 3. Ejecución del contenedor

Para correr la imagen exponiendo el puerto 3000 localmente, se uso el siguiente:

```bash
docker run -p 3000:3000 devops-practice
```

---

## Automatización

### 1. Creación de docker-compose.yml

Para automatizar el entorno se uso Docker Compose. 
Archivo **docker-compose.yml**: 

```yaml
version: '3.8'
services:
  app:
    container_name: devops-practice-app
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
```

### 2. Ejecución de la aplicación con Docker Compose

PAra construir la imagen y ejecutar la aplicación con Docker Composes, se uso el siguiente comando:

```bash
docker-compose up --build -d
```

---

## Evaluación de la experiencia

La automatización con CI/CD hace que los cambios pasen por pruebas y despliegues de manera  automatica, esto hace que los errores durante el desarrollo sean menos, admás con Docker y Docker Compose el despliegue de la aplicación es sencillo y garantiza que el entorno de desarrollo y producción sean similares, todo esto ayuda a mejroar la eficiencia del equipo, ya que los desarrolladores pueden centrarse en el código y el equipo de operaciones en gestionar un despliegue automatico y seguro.