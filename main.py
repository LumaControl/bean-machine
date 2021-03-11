

def decToBin():
    print("Typ hier uw decimale nummer in (integraal)")
    decimalInput = int(input())

    binary = []
     # function converts decimal to binary by dividing by 2 and checking for remainders. 
    while decimalInput != 0:
        if decimalInput % 2 == 0:
            decimalInput = decimalInput / 2
            binary.insert(0,0)
        else:
            decimalInput = (decimalInput - 1) / 2
            binary.insert(0,1)
    print(binary)

# Start script

while True:
    print("Binair naar decimaal of decimaal naar binair?")
    print ("A=Dec-bin B=Bin-dec C=Programma verlaten")
    # User input to choose converting method or to quit
    
    opt = input()
    if opt == "A" or opt == "a":
        print(" ")
        decToBin()
        print(" ")

    elif opt == "B" or opt == "b":
        print(" ")
        print("Deze functie is nog niet beschikbaar")
        print(" ")
    
    elif opt == "C" or opt == "c":
        print(" ")
        print("Dag!")
        break
    else:
        print(" ")
        print("Selecteer \"a\" of \"b\" a.u.b")
        print(" ")
