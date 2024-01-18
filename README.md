# Proyecto de Procesamiento de Estados Financieros en PDF

## Descripción
Este proyecto utiliza la biblioteca Tabula en Python para extraer tablas de los Estados Financieros Consolidados Condensados de Apple Inc. desde un archivo PDF. Luego, limpia los datos, divide las tablas en partes específicas y convierte cada parte en archivos CSV.

## Configuración
**1. Instala las bibliotecas necesarias ejecutando el siguiente comando:**
    ```bash
     pip install pandas tabula-py
    ```

> [!IMPORTANT]
>**2. Asegúrate de tener Java instalado, ya que Tabula utiliza la biblioteca Apache PDFBox que requiere Java.**

**3. Descarga el archivo PDF de los Estados Financieros de Apple Inc. y actualiza la variable pdf_path en el script con la ruta correcta del archivo.**

## Ejecución del Script
Ejecuta el script extract_financial_data.py para iniciar el procesamiento de los datos. Asegúrate de que el entorno tenga los requisitos instalados y sigue las instrucciones de la consola.

## Estructura del Proyecto
+ **extract_financial_data.py:** Contiene el script principal para extraer, limpiar y procesar los datos financieros.
+ **FY23_Q4_Consolidated_Financial_Statements.pdf:** Archivo PDF que contiene los Estados Financieros de Apple Inc.
+ **outputs/:** Carpeta que almacena los archivos CSV resultantes.

## Resultados
Los DataFrames resultantes se almacenan en archivos CSV en la carpeta outputs/. Cada archivo CSV corresponde a una parte específica de los Estados Financieros.

> [!CAUTION]
> Esta versión del programa está diseñada para trabajar especificamente con el PDF proporcionado, si desea utilizar otro estado financiero debera modificar el código de la linea 16 en adelante.
