import psycopg2
import csv


conn = psycopg2.connect(
    dbname="prueba",
    user="brahian",
    password="pass",
    host="localhost",  
    port="5431"  # Puerto por defecto de PostgreSQL
)

tablas = ["cat_perfil_riesgo","catalogo_activos","catalogo_banca","historico_aba_macroactivos"]

for tabla in tablas:
    try:
        cur = conn.cursor()
        
        # Abrimos el archivo CSV y lo leemos usando el módulo csv
        with open(f"data/{tabla}.csv", 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Si hay encabezados en el CSV, ignoramos la primera línea
            for row in reader:
                # Insertamos cada fila del CSV en la tabla de la base de datos
                num = len(row)
                #print(num)
                placeholders = ', '.join(['%s'] * num)
                cur.execute("INSERT INTO {} VALUES ({})".format(tabla,placeholders), row)
        
        # Confirmamos los cambios y cerramos el cursor y la conexión
        conn.commit()

        print("Datos cargados correctamente desde el archivo CSV.")
    except (psycopg2.Error, csv.Error) as e:
        print("Error:", e)

print("Fin de la ejecucíon")
cur.close()
conn.close()