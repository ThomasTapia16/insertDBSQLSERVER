from script import cursor,conn
file = open(r"C:\Users\Thomas\Downloads\gtfsv40\trips.txt","r")

c = 0
for x in file:
    if c > 0:
        dato = x.strip().split(',')
        #print(dato)
        cursor.execute("insert into Viaje(id_viaje, id_ruta, id_servicio, destino_viaje, direccion_viaje, id_shape) values (?, ?, ?, ?, ?, ?)", dato[2], dato[0],dato[1], dato[3], dato[4], dato[5])
    c += 1
conn.commit()
c = 0