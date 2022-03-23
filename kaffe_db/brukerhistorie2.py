import sqlite3

def brukerhistorie2():
    connection = sqlite3.connect("kaffe.db")
    cursor = connection.cursor()
    cursor.execute("SELECT bruker.fullt_navn, COUNT(DISTINCT smakingID) as antall_typer FROM bruker NATURAL JOIN "
                   "kaffesmaking GROUP BY bruker.brukerID ORDER BY antall_typer DESC")
    rows = cursor.fetchall()
    print("Brukere som har anmeldt flest unike kaffer i synkende rekkefølge: \n")
    print(rows)
    connection.close()


if __name__ == '__main__':
    brukerhistorie2()