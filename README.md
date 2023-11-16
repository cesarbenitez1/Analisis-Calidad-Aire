# Análisis de calidad del aire y datos demográficos

El análisis que se realiza en estos ejercicios implica cargar datos demográficos y datos de calidad del aire, limpiar y procesar estos datos, y luego realizar análisis en una base de datos SQLite. Aquí está el análisis punto por punto:

## Ejercicio 1: Cargar Datos Demográficos

Función: ej_1_cargar_datos_demograficos

## 1. Cargar Datos:
Se utiliza la biblioteca Pandas para cargar los datos demográficos desde una URL proporcionada.
El separador de campos es ;.

## 2. Limpieza de Datos Demográficos:
Se eliminan las columnas Race, Count, y Number of Veterans.
Se eliminan las filas duplicadas.

## Ejercicio 2: Cargar Calidad del Aire y Crear Tabla de Dimensiones
Función: ej_2_cargar_calidad_aire

## 1. Cargar Datos de Calidad del Aire:
Se utiliza la API https://api-ninjas.com/api/airquality para obtener datos de calidad del aire para cada ciudad en la tabla demográfica.
Se extrae el elemento concentration de cada entrada por fila.

## 2. Almacenar Datos en una Tabla de Dimensiones:
Se crea un DataFrame de Pandas para almacenar los datos de calidad del aire.
Los datos incluyen concentraciones de CO, NO2, O3, SO2, PM2.5, PM10, overall_aqi y la ciudad.

## Ejercicio 3: Crear Base de Datos SQLite y Realizar Análisis

## 1. Creación de Base de Datos SQLite:

Se crea una base de datos SQLite.
Se cargan las dos tablas procesadas (datos demográficos y calidad del aire) en la base de datos.

## 2. Análisis en SQLite:

Se aplican joins y agregaciones para verificar si las ciudades más pobladas tienen la peor calidad del aire.
Se muestran las primeras 10 columnas del resultado.

## Creación de un Script y Documentación
Se crea un script para el ejercicio 3, y luego se proporciona una query SQL

## Interpretación
Los hallazgos indicaron que, en contra de lo anticipado, Los Ángeles, a pesar de no ser la ciudad más habitada, exhibe una calidad del aire más deficiente en términos de concentraciones de CO, NO2, O3, PM2.5 y PM10 en comparación con Nueva York, la ciudad más poblada. Así, los datos no respaldan la suposición de que las ciudades con mayor población tengan necesariamente una peor calidad del aire. Para obtener detalles adicionales, se recomienda consultar el archivo 'calidad_aire.csv'.
