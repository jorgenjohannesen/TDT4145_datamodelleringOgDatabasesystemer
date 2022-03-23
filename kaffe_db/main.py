import brukerhistorie1
import brukerhistorie2
import brukerhistorie3
import brukerhistorie4
import brukerhistorie5

if __name__ == '__main__':
    while True:
        brukerInput = str(input("Hvilken brukerhistorie vil du gjennomføre? \n"
                                "Tast 1 for å legge inn et smaksnotat på en kafffe \n"
                                "Tast 2 for å vise de brukerne som har smakt flest kaffer, sortert synkende \n"
                                "Tast 3 for å se den kaffen som gir deg mest for pengene ifølge KaffeDB sine brukere \n"
                                "Tast 4 for å vise den kaffen som inneholder 'floral' i beskrivelsen \n"
                                "Tast 5 for å vise de kaffene som er fra Rwanda eller Colombia som ikke er vaskede \n"
                                "Tast q for å avslutte \n"
                                "Skriv inn her: "))
        if (brukerInput == '1'):
            brukerhistorie1.brukerhistorie1()
        elif (brukerInput == '2'):
            brukerhistorie2.brukerhistorie2()
        elif (brukerInput == '3'):
            brukerhistorie3.brukerhistorie3()
        elif (brukerInput == '4'):
            brukerhistorie4.brukerhistorie4()
        elif (brukerInput == '5'):
            brukerhistorie5.brukerhistorie5()
        elif (brukerInput == 'q'):
            break
        else:
            print("Denne kommandoen finnes ikke!")
    print("Avsluttet programmet")