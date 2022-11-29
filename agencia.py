from script import cursor,conn
file = open(r"C:\Users\Thomas\Downloads\gtfsv40\agency.txt","r")

c = 0
for x in file:
    if c > 0:
        dato = x.strip().split(',')
        print(dato)
        cursor.execute("insert into Agencia(id_agencia, nombre_agencia, url_agencia, timezone) values (?, ?, ?, ?)", dato[0], dato[1],dato[2], dato[3])
    c += 1
conn.commit()
c = 0
