'''
### 2. Aplicación Web Interactiva con **Streamlit**

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

'''

# Solución

import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Editor de Archivos CSV de Pokémon")

# Subir archivo CSV
uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"]) # Solo permite archivos CSV

if uploaded_file is not None:
   # Leer el archivo CSV
   df = pd.read_csv(uploaded_file) # Creamos un DataFrame a partir del archivo CSV

   # Mostrar el contenido del archivo CSV
   st.write("Contenido del archivo CSV:") # Título para el contenido del archivo CSV
   st.dataframe(df) # Mostramos el contenido del archivo CSV como una tabla

   # Editar el archivo CSV
   edited_df = st.data_editor(df) # Creamos un editor de datos para el DataFrame

   # Descargar el archivo modificado
   st.download_button( # Botón para descargar el archivo modificado
      label="Descargar archivo CSV modificado", # Etiqueta del botón
      data=edited_df.to_csv(index=False).encode('utf-8'), # Contenido del archivo a descargar
      file_name="pokemon_evoluciones_modificado.csv", # Nombre del archivo a descargar
      mime="text/csv" # Tipo de archivo a descargar
   )