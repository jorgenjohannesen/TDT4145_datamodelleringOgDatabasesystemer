import sqlite3
# Brukerhistorie 5
def brukerhistorie5():
    con = sqlite3.connect("kaffe.db")
    cursor = con.cursor()
    cursor.execute("SELECT brenneri_navn, kaffe_navn, land, metode_navn "
                   "FROM kaffe NATURAL JOIN kaffebrenneri NATURAL JOIN kaffeparti NATURAL JOIN gaard NATURAL JOIN foredlingsmetode "
                   "WHERE (land LIKE '%Rwanda%' OR  land LIKE '%Colombia%') AND metode_navn NOT LIKE '%vasket%'")
    rows = cursor.fetchall()
    print("Uvaskede kaffer fra Colombia og Rwanda: \n")

    if not rows:
        print("Finnes ingen kaffer som ikke er Vasket og som kommer fra Colombia eller Rwanda!")
    else:
        print("(Navn på brenneri, Navn på kaffe, Land, Foredlingsmetode)")
        for row in rows:
            print(row)
    con.close()
    print("")
    return


if __name__ == '__main__':
    brukerhistorie5()
