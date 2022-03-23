import sqlite3
from sqlite3 import DatabaseError

def erValidEpostadresse(epostadresse):
    connection = sqlite3.connect("kaffe.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM bruker WHERE epostadresse = ?", (epostadresse,))
    row = cursor.fetchone()
    if not row:
        raise DatabaseError
    connection.close()
    return row[0], row[3]


def loggInn():
    while True:
        try:
            brukerID, passord = erValidEpostadresse(input("Skriv inn epostadresse: "))
        except DatabaseError:
            print("Denne epostadressen finnes ikke!")
            continue
        else:
            break
    while True:
        passordSkrevetInn = input("Skriv inn passord: ")
        if passord == passordSkrevetInn:
            break
        else:
            print("Dette passordet passer ikke til epostadressen!")
            continue
    return brukerID


def erValidBrenneri(brenneri):
    connection = sqlite3.connect("kaffe.db")
    cursor = connection.cursor()
    cursor.execute("SELECT brenneriID FROM kaffebrenneri WHERE navn = ?", (brenneri,))
    row = cursor.fetchone()
    if not row:
        raise DatabaseError
    connection.close()
    return row[0]


def erValidKaffeFraBrenneri(kaffe, brenneriID):
    connection = sqlite3.connect("kaffe.db")
    cursor = connection.cursor()
    cursor.execute('''SELECT kaffeID 
    FROM kaffe  
    WHERE navn = ? AND brenneriID = ?''', (kaffe, brenneriID))
    row = cursor.fetchone()
    if not row:
        raise DatabaseError
    connection.close()
    return row[0]


def brukerhistorie1():
    brukerID = loggInn()

    # Henter brenneri og sjekker at det finnes i databasen

    while True:
        try:
            brenneriID = erValidBrenneri(input("Hvilket brenneri kommer kaffen fra? "))
        except DatabaseError:
            print("dette brenneriet finnes ikke!")
            continue
        else:
            break
        # Henter kaffe fra bruker og sjekker om den finnes hos brenneriet
    while True:
        try:
            kaffeID = erValidKaffeFraBrenneri(input("Hva heter kaffen? "), brenneriID)
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

    notater = input("Skriv inn smaksnotatet: ")
    dato = input("Skriv inn dato (dd.mm.åååå) : ")

    connection = sqlite3.connect("kaffe.db")
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO kaffesmaking(notater, poeng, dato, brukerID, kaffeID) 
    VALUES (?,?,?,?,?) ''', (notater, poeng, dato, brukerID, kaffeID))
    connection.commit()
    connection.close()

    print("Du har lagt til en smaking!")
    print(notater)
