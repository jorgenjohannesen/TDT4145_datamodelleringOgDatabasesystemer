import sqlite3
# Brukerhistorie 3
def brukerhistorie3():
    connection = sqlite3.connect("kaffe.db")
    cursor = connection.cursor()
    cursor.execute("SELECT kaffe_navn , brenneri_navn , avg(poeng) as gjennomsnittsPoeng, kiloprisINOK "
                   "FROM kaffesmaking NATURAL JOIN kaffe NATURAL JOIN kaffebrenneri "
                   "GROUP BY kaffe.kaffeID ORDER "
                   "BY (gjennomsnittsPoeng / kiloprisINOK) DESC ")
    rows = cursor.fetchall()
    print("Hver kaffe og dens brenneri med gjennomsnittspoeng delt på kilopris i synkende rekkefølge: \n  ")
    for row in rows:
        print(row)
    connection.close()
    return
if __name__ == '__main__':
    brukerhistorie3()