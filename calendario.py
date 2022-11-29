from script import cursor,conn
file = open(r"C:\Users\Thomas\Downloads\gtfsv40\calendar.txt","r")

c = 0
for x in file:
    if c > 0:
        dato = x.strip().split(',')
        #print(dato)
        cursor.execute("insert into Calendario(id_servicio, lunes, martes, miercoles, jueves, viernes, sabado, domingo) values (?, ?, ?, ?, ?, ?, ?, ?)", dato[0], dato[1],dato[2], dato[3], dato[4], dato[5], dato[6], dato[7])
    c += 1
conn.commit()
c = 0