import sqlite3
# Brukerhistorie 5
def brukerhistorie5():
    con = sqlite3.connect("kaffe.db")
    cursor = con.cursor()
    cursor.execute("SELECT brenneri_navn, kaffe_navn, land, metode_navn "
                   "FROM kaffe NATURAL JOIN kaffebrenneri NATURAL JOIN kaffeparti NATURAL JOIN gaard NATURAL JOIN foredlingsmetode "
                   "WHERE (land LIKE '%Rwanda%' OR  land LIKE '%Colombia%') AND metode_navn NOT LIKE '%vasket%'")
    rows = cursor.fetchall()
    print("Kaffer og dens brennerier som ikke er 'Vasket', men kommmer fra Colombia eller Rwanda: \n")

    if not rows:
        print("Finnes ingen Kaffer som ikke er Vasket og som kommer fra Colombia eller Rwanda!")
    else:
        for row in rows:
            print(row)
            print("")
    con.close()
    print("")
    return


if __name__ == '__main__':
    brukerhistorie5()
