from script import cursor,conn


file = open(r"C:\Users\Thomas\Downloads\gtfsv40\calendar_dates.txt","r")

c = 0
for x in file:
    if c > 0:
        dato = x.strip().split(',')
        print(dato)
        cursor.execute("insert into fecha_calendario(id_servicio, fecha, tipo_excepcion) values (?, ?, ?)", dato[0], dato[1],dato[2])
    c += 1
conn.commit()
c = 0
