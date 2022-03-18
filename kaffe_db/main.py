import sqlite3
from sqlite3 import DatabaseError


def brukerhistorie1():
    #Henter brenneri og sjekker at det finnes i databasen
    while True:
        try:
            brenneri = erValidBrenneri(input("Hvilket brenneri kommer kaffen fra? "))
        except DatabaseError:
            print("dette brenneriet finnes ikke!")
            continue
        else:
            break

    #Henter kaffe fra bruker og sjekker om den finnes hos brenneriet
    while True:
        try:
            kaffe = erValidKaffeFraBrenneri(input("Hva heter kaffen? "), brenneri)
        except DatabaseError:
            print("Brenneriet har ikke en kaffe som heter dette!")
            continue
        else:
            break

    while True:
        try:
            poeng = int(input("Hvor mange poeng vil du gi denne kaffen? (1-10) "))
        except ValueError:
            print("Poeng må være et heltall ")
            continue

        if poeng > 10 or poeng < 1:
            print("Vennligst oppgi et tall mellom 1 og 10")
        else:
            break

def erValidBrenneri(brenneri):
    connection = sqlite3.connect("coffee.db")
    cursor = connection.cursor()
    cursor.execute("SELECT navn FROM kaffebrenneri WHERE navn = ?", brenneri)
    row = cursor.fetchone()
    if len(row) <= 0:
        raise DatabaseError
    connection.close()

def erValidKaffeFraBrenneri(kaffe, brenneri):
    connection = sqlite3.connect("coffee.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * "
                   "FROM kaffe JOIN kaffebrenneri USING brenneriID"
                   " WHERE kaffe.navn = ? AND kaffebrenneri.navn = ?", (kaffe, brenneri))
    row = cursor.fetchone()
    if len(row) <= 0:
        raise DatabaseError
    connection.close()

if __name__ == '__main__':
    connection = sqlite3.connect("coffee.db")
    cursor = connection.cursor()



