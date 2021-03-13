

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


def binToDec():

    arrayCounter = 0
    #  TODO: make even numbers output the correct value too.
    strInput = input()

    # Separates the string into separate digits in an array and defines the length of it
    convertedArray = [int(d) for d in str(strInput)]
    arrayLength = len(convertedArray)
    
    # just some base variable declarations
    power  = 0
    decResult  = 0
    counter = 0

    
    while arrayLength != 0:
        decResult = decResult + convertedArray[counter] * 2 ** power
        counter = counter + 1
        power = power + 1
        arrayLength = arrayLength - 1
    
    print(decResult)



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
        binToDec()
        print(" ")
    
    elif opt == "C" or opt == "c":
        print(" ")
        print("Dag!")
        break
    else:
        print(" ")
        print("Selecteer \"a\" of \"b\" a.u.b")
        print(" ")
