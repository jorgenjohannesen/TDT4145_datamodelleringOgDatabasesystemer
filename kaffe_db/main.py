
import sqlite3


con = sqlite3.connect("coffee.db")

cursor = con.cursor()
cursor.execute("INSERT into bruker VALUES (1, 'jrgen@test.no', 'Jørgen Johannesen' , 'testpassord')")
cursor.execute("INSERT into bruker VALUES (2, 'jrgen@test.no', 'Jørgen Johannesen' , 'testpassord')")

cursor.execute("SELECT brukerID FROM bruker")
row = cursor.fetchall()
print(row)
