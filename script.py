#conexion a la bdd
import pyodbc


    
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-C3PU4DH;DATABASE=santiago2018v2;UID=thomas;PWD=1234')

cursor = conn.cursor()




