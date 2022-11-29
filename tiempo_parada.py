from script import cursor,conn
file = open(r"C:\Users\Thomas\Downloads\gtfsv40\frequencies.txt","r")

c = 0
for x in file:
    if c > 0:
        dato = x.strip().split(',')
        print(dato)
        cursor.execute("insert into frecuencia(trip_id, tiempo_inicio, tiempo_fin, headway_secs, exact_times) values (?, ?, ?, ?, ?)", dato[0], dato[1],dato[2], dato[3], dato[4])
    c += 1
conn.commit()
c = 0
