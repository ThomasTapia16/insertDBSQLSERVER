from script import cursor,conn


file = open(r"C:\Users\Thomas\Downloads\gtfsv40\shapes.txt","r")

c = 0
lshapesid = []
for x in file:
    if c > 0:
        dato = x.strip().split(',')
        print(dato)
        if dato[0] not in lshapesid:
            cursor.execute("insert into ShapeId(id_shape) values (?)", dato[0])
        cursor.execute("insert into Shape(id_shape, latitud, longitud, secuencia) values (?, ?, ?, ?)", dato[0], dato[1], dato[2], dato[3])
        lshapesid.append(dato[0])
    c += 1
conn.commit()
c = 0
