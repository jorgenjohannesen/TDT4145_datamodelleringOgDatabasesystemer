import brukerhistorie1
import brukerhistorie2
import brukerhistorie3
import brukerhistorie4
import brukerhistorie5

if __name__ == '__main__':
    brukerInput = str(input("Hvilken brukerhistorie vil du gjennomføre? "))
    running = True
    while running:
        if (brukerInput == '1'):
            brukerhistorie1()
        elif (brukerInput == '2'):
            brukerhistorie2()
        elif (brukerInput == '3'):
            brukerhistorie3()
        elif (brukerInput == '4'):
            brukerhistorie4()
        elif (brukerInput == '5'):
            brukerhistorie5
        elif (brukerInput == 'q'):
            running = False
        else:
            print("Could not read")
