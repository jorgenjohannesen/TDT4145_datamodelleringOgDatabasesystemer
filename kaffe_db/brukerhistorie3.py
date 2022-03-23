import sqlite3

def brukerhistorie3():
    connection = sqlite3.connect("kaffe.db")
    cursor = connection.cursor()
    cursor.execute("SELECT kaffe.navn AS kaffe_navn, kaffebrenneri.navn AS brenneri_navn, avg(poeng) as gjennomsnittsPoeng, kiloprisINOK "
                   "FROM kaffesmaking JOIN (kaffe JOIN kaffebrenneri USING(brenneriID)) ON (kaffe.kaffeID) "
                   "GROUP BY kaffe.kaffeID ORDER "
                   "BY (gjennomsnittsPoeng / kiloprisINOK) DESC ")
    rows = cursor.fetchall()
    print("Hver kaffe og dens brenneri med gjennomsnittspoeng delt på kilopris i synkende rekkefølge: \n  ")
    for row in rows:
        print(row)
        print('\n')
    connection.close()

if __name__ == '__main__':
    brukerhistorie3()