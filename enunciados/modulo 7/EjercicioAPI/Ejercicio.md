## Consumo de API sobre Listado de Asteroides NeoWs (Near Earth Object Web Service) de la NASA

Se requiere realizar la siguiente tarea:

### 1. Consumir la API de la NASA para obtener el listado de asteroides NeoWs en un día determinado (Near Earth Object Web Service):

- Obtener la **API_KEY** desde [API NASA](https://api.nasa.gov/)
- **Endpoint**: Neo - Feed

### 2. Generar un archivo `.csv` de ancho fijo con la siguiente información:
- **Datos a mostrar**:
  - **ID (id)** del asteroide. Tipo String
  - **Nombre (name)** del asteroide. Tipo String
  - **Diámetro mínimo estimado (estimated_diameter_min)** (en kilómetros). Tipo Float
  - **Diámetro máximo estimado (estimated_diameter_max)** (en kilómetros). Tipo Float
  - **Potencialmente peligroso (is_potentially_hazardous_asteroid)** (True/False). Tipo Boolean
- **Condiciones**:
  - Mostrar solo los asteroides cuyo **diámetro mínimo estimado sea mayor a 0.01 km**.
  - Ordenar los asteroides en el archivo de la siguiente manera:
    - Primero los **potencialmente peligrosos** (True), seguidos de los no peligrosos.
    - Ordenar por **diámetro mínimo estimado** de mayor a menor.
- **Separador**: El archivo `.csv` debe utilizar la coma (`,`) como separador de columnas.

### Ejemplo de contenido del archivo `.csv`:

```
123456789012345;AsteroideX;160.50;250.70;True
123456789012346;AsteroideY;120.80;180.10;True
123456789012347;AsteroideZ;150.00;200.20;False
123456789012348;AsteroideW;100.00;200.20;False
...
```

### 3. Aplicación Web Interactiva con **Streamlit**

**Objetivo:**
Crear una aplicación web interactiva utilizando **Streamlit** donde el usuario pueda:
- Subir el archivo `.CSV` generado previamente.
- Editar el contenido del archivo directamente desde la web.
- Descargar la versión modificada del archivo.

#### Librerías a utilizar:
1. **Streamlit**: 
   - Es una biblioteca de Python de código abierto que facilita la creación de aplicaciones web interactivas para análisis de datos y machine learning.
   - Permite crear interfaces gráficas de usuario (GUI) de manera simple y rápida, ideal para mostrar gráficos, tablas, formularios y otros elementos interactivos sin necesidad de tener experiencia en desarrollo web.
   - Funciona en cualquier navegador, y es perfecta para crear aplicaciones para visualizar, editar o interactuar con datos.

2. **Pandas**: 
   - Es una poderosa librería de Python utilizada para manipulación y análisis de datos, especialmente en formato tabular como archivos `.CSV`.
   - Ofrece herramientas para la carga, transformación, limpieza y manipulación de grandes conjuntos de datos de manera eficiente.

#### Detalles del ejercicio:
- **Cargar archivo CSV**: La aplicación debe permitir al usuario subir un archivo `.CSV`. Streamlit proporciona un componente llamado `st.file_uploader()` que facilita la carga de archivos desde la interfaz web.
  
- **Edición del archivo**: Una vez cargado el archivo, se mostrará su contenido utilizando **Pandas** para manipular los datos en tablas. La aplicación debe permitir al usuario realizar modificaciones en los datos (ej., cambiar valores de celdas o agregar/eliminar filas/columnas) directamente desde la interfaz.

- **Descargar archivo modificado**: Después de que el usuario haya editado el archivo, la aplicación debe permitir descargar la nueva versión del `.CSV` con los cambios aplicados, usando la función `st.download_button()`.