import sqlite3

def brukerhistorie4():
    connection = sqlite3.connect("kaffe.db")
    cursor = connection.cursor()
    cursor.execute("SELECT brenneri_navn, kaffe_navn "
                   "FROM kaffesmaking NATURAL JOIN kaffe NATURAL JOIN kaffebrenneri "
                   "WHERE notater LIKE '%floral%' GROUP BY kaffeID "
                   "UNION "
                   "SELECT brenneri_navn, kaffe_navn "
                   "FROM kaffe NATURAL JOIN kaffebrenneri "
                   "WHERE kaffe_beskrivelse LIKE '%floral%' GROUP BY kaffeID ")

    rows = cursor.fetchall()
    print("Hver kaffe som har en anmeldelse eller beskrivelse som er beskrevet som 'Floral': \n ")
    for row in rows:
        print(row)
    connection.close()
    return

if __name__ == '__main__':
    brukerhistorie4()