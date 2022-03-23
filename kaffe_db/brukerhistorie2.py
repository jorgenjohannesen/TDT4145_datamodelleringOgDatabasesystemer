import sqlite3
from datetime import date

def brukerhistorie2():
    year = date.today().year
    connection = sqlite3.connect("kaffe.db")
    cursor = connection.cursor()
    cursor.execute(f'''SELECT bruker.fullt_navn, COUNT(DISTINCT smakingID) as antall_typer
                   FROM bruker NATURAL JOIN kaffesmaking 
                   WHERE smaking_dato LIKE '%{year}%'
                   GROUP BY bruker.brukerID ORDER BY antall_typer DESC''')
    rows = cursor.fetchall()
    print("Brukere som har smakt flest unike kaffer i synkende rekkefølge: \n")
    print(rows)
    connection.close()
    return

if __name__ == '__main__':
    brukerhistorie2()