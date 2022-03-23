import sqlite3

def userStory5():
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute("SELECT roastedCoffee.name, coffeeRoastery.roasteryName "
                   "FROM roastedCoffee NATURAL JOIN coffeeRoastery NATURAL JOIN batch JOIN farm f on batch.farmID = "
                   "f.farmID JOIN processingMethod pM on batch.processingMethodID = pM.processingMethodID WHERE(NOT("
                   "pM.name == 'Vasket')) AND (f.country == 'Colombia') OR (f.country == 'Rwanda') ")
    rows = cursor.fetchall()
    print("Kaffer og dens brennerier som ikke er 'Vasket', men kommmer fra Colombia eller Rwanda: \n")
    print(rows)
    con.close()