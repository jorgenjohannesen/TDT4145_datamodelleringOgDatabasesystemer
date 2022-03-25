import sqlite3
from datetime import date
# Brukerhistorie 2
def brukerhistorie2():
    year = date.today().year
    connection = sqlite3.connect("kaffe.db")
    cursor = connection.cursor()
    cursor.execute(f'''SELECT fullt_navn, COUNT(DISTINCT kaffeID) as antall_typer
                   FROM bruker NATURAL JOIN kaffesmaking 
                   WHERE smaking_dato LIKE '%{year}%'
                   GROUP BY brukerID ORDER BY antall_typer DESC''')
    rows = cursor.fetchall()
    print("Disse brukerne har smakt flest unike kaffer så langt i år: \n")
    print("(Brukers fulle navn, antall unike kaffer smakt i år)")
    for row in rows:
        print(row)
    connection.close()
    return

if __name__ == '__main__':
    brukerhistorie2()