import sqlite3
import pandas as pd

# Creación de la DB y carga de datos.
conn = sqlite3.connect('Load_data.db')

df1 = pd.read_csv('ciudades.csv')
df2 = pd.read_csv('list.csv')

df1.to_sql('ciudades', conn, if_exists='replace', index=False)
df2.to_sql('list', conn, if_exists='replace', index=False)

# Query para verificar si las ciudades más pobladas tienen la peor calidad del aire.
query = '''
SELECT Cities.City, Cities."Total population", ConAir.CO, ConAir.NO2, ConAir.O3, ConAir."PM2.5", ConAir.PM10
FROM Cities
JOIN ConAir ON ConAir.City = Cities.City
ORDER BY Cities."Total population" DESC
LIMIT 0, 10;
'''
result_df1 = pd.read_sql_query(query, conn)
result_df1.to_csv("calidad_aire.csv")
#print(result_df1)
conn.close()