import sqlite3

def userStory4():
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute("SELECT roastedCoffee.name, coffeeRoastery.roasteryName "
                   "FROM review NATURAL JOIN roastedCoffee NATURAL JOIN coffeeRoastery "
                   "WHERE reviewNote LIKE '%floral%' OR roastedCoffee.description LIKE '%floral%' GROUP BY roastedCoffee.roastedCoffeeID")
    rows = cursor.fetchall()
    print("Hver kaffe som har en anmeldelse eller beskrivelse som er beskrevet som 'Floral: \n ")
    print(rows)
    con.close()