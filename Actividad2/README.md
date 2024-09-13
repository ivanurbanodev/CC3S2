# Preguntas de reflexión - DevSecOps

1. **¿Qué significa "desplazar a la izquierda" en el contexto de DevSecOps y por qué es importante?**
   - "Desplazar a la izquierda" en DevSecOps quiere decir que vamos a integrar la seguridad en el desarrollo desde etapas iniciales para así poder detectar problemas desde las priemras etapas y reducir riesgos.

2. **Explica cómo IaC mejora la consistencia y escalabilidad en la gestión de infraestructuras.**
   - IaC consite en automatizar configuraciones y  despliegue para replicar entornos de forma eficiente.

3. **¿Cuál es la diferencia entre monitoreo y observabilidad? ¿Por qué es crucial la observabilidad en sistemas complejos?**
   - El monitoreo observa métricas conocidas, mientras que la observabilidad permite entender mejor el sistema de manera holística. 

4. **¿Cómo puede la experiencia del desarrollador impactar el éxito de DevOps en una organización?**
   - La experiencia del desarrollador impacta en DevOps mejorando la productividad y colaboración, lo cual hace que el equipo trabaje de manera eficiente.

5. **Describe cómo InnerSource puede ayudar a reducir silos dentro de una organización.**
   - InnerSource ayuda a reducir los silos  promoviendo la colaboración de trabajo en equipo ya que usa código abierto para cualquier departamento de la empresa.

6. **¿Qué rol juega la ingeniería de plataformas en mejorar la eficiencia y la experiencia del desarrollador?**
   - La ingeniería de plataformas mejora la eficiencia de los desarrolladores porque ofrece herramientas de automatización  de tareas simplificando así el trabajo, haciendo que los desarrolladores se centren más en el desarrollo de la aplicación.

# 1.Configuración del entorno

### 1. Inicializa el proyecto de Node.js:

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
npm install express jest supertest
```
### 3. Crea la estructura del proyecto:

El proyecto fue estructurado según los lineamientos y se usaron los siguientes comandos para crear los directorios y  archivos.

```bash
mkdir src tests    # Crea las carpetas src (para el código fuente) y tests (para las pruebas).
touch src/app.js tests/app.test.js    # Crea los archivos app.js (para la API) y app.test.js (para las pruebas)
```

### 4. Implementa la API REST en `src/app.js`:

El API REST  responde con **Hello, World!** a la solicitud GET en la raíz (`/`), se configuró para que el servidor solo se inicie cuando el archivo se ejecute directamente, esto para no tener problemas cuando el test lo importe.

```javascript
const express = require('express');   // Importa Express para manejar las rutas y el servidor
const app = express();                // Instancia la aplicación Express

// Define una ruta GET en el endpoint raíz '/' que responde con "Hello, World!"
app.get('/', (req, res) => {
  res.send('Hello, World!');
});

// Solo inicia el servidor si este archivo se está ejecutando directamente
if (require.main === module) {
  const port = process.env.PORT || 3000;  // Configura el puerto 
  app.listen(port, () => {
    console.log(`Server running on port ${port}`);  // MImprime un mensaje en la consola indicando que el servidor está corriendo en su puerto correspondiente
  });
}

module.exports = app;  // Exporta la aplicación p
```

### 5. Escribe un test básico en `tests/app.test.js`:

La prueba verifica que el API responda con **Hello, World!**.

```javascript
const request = require('supertest');      // Importa Supertest
const app = require('../src/app');         // Importa app

describe('GET /', () => {
  let server;

  beforeAll(() => {
    server = app.listen(0);  // Inicia el servidor en un puerto aleatorio (0 hace que el sistema asigne un puerto libre)
  });

  afterAll((done) => {
    server.close(done);  // Cierra el servidor después de que las pruebas se hayan ejecutado
  });

  it('should return Hello, World!', async () => {
    const res = await request(app).get('/');  // Realiza la petición GET 
    expect(res.statusCode).toEqual(200);      // Cmprueba que el código sea 200
    expect(res.text).toBe('Hello, World!');   // Comprueba la respuesta 
  });
});
```

### 6. Configura el script de test en `package.json`:

Se configuró el test en el archivo **package.json** para usar Jest con la opción **--detectOpenHandles** para detectar puertos no cerrados.

```json
{
  "name": "devops-practice",
  "version": "1.0.0",
  "scripts": {
    "test": "jest --detectOpenHandles"  // Define el script de pruebas 
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

#  2.Implementación de DevSecOps

## Integración de Seguridad:

### 1. Configura un análisis de seguridad estática con `npm audit`:

Se ejecutó un análisis de las dependencias instaladas para encontrar vulnerabilidades de seguridad con el siguiente comando:

```bash
npm audit  
```

### 2. Automatiza el análisis de seguridad en GitHub Actions:

##  Automatiza el análisis de seguridad en GitHub Actions:

Se configuró GitHub Actions para ejecutar el pipeline que hace lo siguiente:

1. **Revisa el código (checkout)**:
   Utiliza **checkout@v2** para clonar el código del repositorio en una máquina virtual.

2. **Instala Node.js**: 
   Configura la versión de Node.js con **setup-node@v2**.

3. **Instala de dependencias**:
   Con **npm install** instala dependencias.

4. **Ejecución de pruebas**:
   Se ejecutan las pruebas del proyecto con el comando `npm test`.

5. **Análisis de seguridad**:
   Se realiza una auditoría de las dependencias para detectar vulnerabilidades de seguridad con el comando `npm audit`.

## Archivo **ci.yml** detallado:

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
      uses: actions/checkout@v2  # Clona el repositorio
      
    - name: Set up Node.js 
      uses: actions/setup-node@v2  #configura node
      with:  
        node-version: '14'  
        
    - name: Install dependencies  
      run: |
        npm install  
      working-directory: Actividad2/devops-practice  # Define el directorio donde se encuentran los archivos

    - name: Run tests  
      run: |
        npm test  
      working-directory: Actividad2/devops-practice  # Ejecuta las pruebas dentro del directorio del proyecto

    - name: Run security audit  
      run: |
        npm audit  
      working-directory: Actividad2/devops-practice  # Ejecuta la auditoría en el directorio del proyecto
```


# 3. Implementación de Infraestructura como Código (IaC)

## Usa Docker para contenerizar la aplicación:

### 1. Crea un archivo `Dockerfile`:

```Dockerfile
# Usa la imagen oficial de Node.js (versión 14)
FROM node:14

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos package.json y package-lock.json
COPY package*.json ./

# Instala las dependencias
RUN npm install

# Copia el resto de los archivos de la aplicación al contenedor
COPY . .

# Expone el puerto en el que la aplicación correrá
EXPOSE 3000

# Comando para iniciar la aplicación
CMD ["node", "src/app.js"]
```

### 2. Construye y corre el contenedor:

```bash
docker build -t devops-practice .  # Construye la imagen Docker con el nombre "devops-practice"
docker run -p 3000:3000 devops-practice  # Corre el contenedor en el puerto 3000
```

### 3. Automatiza la gestión de contenedores usando Docker Compose:

```yaml
services:
  app:
    build: .                       # Construye el servicio a partir del Dockerfile en el directorio actual
    ports:
      - "3000:3000"                # Mapea el puerto 3000 del contenedor al puerto 3000 del host
    environment:
      - NODE_ENV=production         # Configura la variable de entorno para indicar que está en modo producción
```

Para levantar el servicio:

```bash
docker-compose up --build -d  # Construye y corre el contenedor en segundo plano
```

# 4. Implementación de Observabilidad

## Configura Prometheus y Grafana para monitorear la aplicación:

### 1. Crea un archivo `prometheus.yml`:

```yaml
global:
  scrape_interval: 15s  # Configurs el tiempo en el que Prometheus recolectará métricas

scrape_configs:
  - job_name: 'node-app'
    static_configs:
      - targets: ['app:4000']  # Especifica la URL de la aplicación para recolectar métricas
```

### 2. Configura Grafana utilizando un `docker-compose.yml` actualizado:

```yaml
services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
  
  prometheus:
    image: prom/prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml  # Configura Prometheus desde el archivo prometheus.yml
    ports:
      - "9090:9090"  # Prometheus expone su interfaz web en el puerto 9090
  
  grafana:
    image: grafana/grafana
    ports:
      - "3001:3000"  # Mapea el puerto 3001 del host al puerto 3000 del contenedor (donde Grafana está por defecto)
```


# 5. Documentación y evaluación

- La documrntación se muestra lineas arriba.

- Reflexión: Usar npm audit en los pipelines permite identificar vulnerabilidades de seguridad, reduciendo riesgos con los paquetes. Implementar IaC con Docker Compose automatizó la configuración y despliegue de la app. Con Prometheus para métricas y Grafana para monitoreo gráfico, se logró un seguimiento continuo de la app.

