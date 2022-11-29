from script import cursor,conn
from type_route import definir_tipo
file = open(r"C:\Users\Thomas\Downloads\gtfsv40\routes.txt","r")

c = 0
for x in file:
    if c > 0:
        dato = x.strip().split(',')
        #print(type(dato[5]))
        #tipo = definir_tipo(dato[5])
        #print(tipo)
        cursor.execute("insert into Ruta(id_ruta, id_agencia, nomrbe_recorrido, destino_recorrido, tipo_transporte, color_ruta, color_texto) values (?, ?, ?, ?, ?, ?, ?)", dato[0], dato[1],dato[2], dato[3],definir_tipo(dato[5]),dato[7], dato[8])
    c += 1
conn.commit()
c = 0