from script import cursor,conn
file = open(r"C:\Users\Thomas\Downloads\gtfsv40\stops.txt","r")

c = 0
for x in file:
    if c > 0:
        dato = x.strip().split(',')
        #print(dato)
        cursor.execute("insert into Parada(id_parada, nombre_parada, longitud, latitud) values (?, ?, ?, ?)", dato[0], dato[2],dato[3], dato[4])
    c += 1
conn.commit()
c = 0
