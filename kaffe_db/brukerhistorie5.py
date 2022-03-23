import sqlite3

def brukerhistorie5():
    con = sqlite3.connect("kaffe.db")
    cursor = con.cursor()
    cursor.execute("SELECT brenneri_navn, kaffe_navn, land, metode_navn "
                   "FROM kaffe NATURAL JOIN kaffebrenneri NATURAL JOIN kaffeparti NATURAL JOIN gaard NATURAL JOIN foredlingsmetode "
                   "WHERE (land LIKE '%Rwanda%' OR  land LIKE '%Colombia%') AND NOT metode_navn LIKE '%Vasket%'")
    rows = cursor.fetchall()
    print("Kaffer og dens brennerier som ikke er 'Vasket', men kommmer fra Colombia eller Rwanda: \n")
    print(rows)
    con.close()

if __name__ == '__main__':
    brukerhistorie5()
