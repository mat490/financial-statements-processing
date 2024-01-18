import tabula
import pandas as pd

pdf_path = "FY23_Q4_Consolidated_Financial_Statements.pdf"

# Utiliza el método read_pdf para extraer tablas del PDF
# Puedes ajustar los argumentos según sea necesario
tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

pandas_tables = []
for i, tabla in enumerate(tables):
    df = pd.DataFrame(tabla)
    pandas_tables.append(df)

def limpiar_data(valor):
    if isinstance(valor, str):  # Verificar si el valor es una cadena
        return valor.replace('!', '')
    else:
        return valor 

# Aplicar la función de limpieza de datos a cada DataFrame en pandas_tables
for i, df_actual in enumerate(pandas_tables):
    pandas_tables[i] = df_actual.applymap(limpiar_data)

    # Mostrar el DataFrame resultante
    print(f"DataFrame {i + 1} ha cocnluido su limpieza de datos:")
    print("\n")

tabla2_parte1 = pandas_tables[1].iloc[:14, :].copy()
tabla2_parte2 = pandas_tables[1].iloc[14:35, :].copy()


tabla2_parte1 = tabla2_parte1.drop(columns=['ASSETS:', 'Unnamed: 1'])
tabla2_parte2 = tabla2_parte2.drop(columns=['ASSETS:', 'Unnamed: 1'])

del pandas_tables[1]
pandas_tables.insert(1, tabla2_parte1)
pandas_tables.insert(2, tabla2_parte2)

columnas_nombres = [['Net sales: ', 'September 30 , 2023', 'September 24 , 2022','September 30 , 2023','September 24, 2022'],
                    ['Assets: ', 'September 30 , 2023', 'September 24 , 2022'],
                    ['LIABILITIES AND SHAREHOLDERS’ EQUITY:', 'September 30 , 2023', 'September 24 , 2022'],
                    ['Cash, cash equivalents and restricted cash, beginning balances:', 'September 30 , 2023', 'September 24 , 2022']]

for i in range(len(pandas_tables)):
    pandas_tables[i].columns = columnas_nombres[i]
    

# Convertir cada DataFrame a archivos CSV
for i, df in enumerate(pandas_tables):
    nombre_archivo = f"tabla_apple{i + 1}.csv"
    df.to_csv(nombre_archivo, index=False)

    print(f"DataFrame {i + 1} convertido a CSV: {nombre_archivo}")