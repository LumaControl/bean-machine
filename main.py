print("Typ hier uw decimale nummer in")

decimal = int(input())

binary = []
 # function converts decimal to binary by dividing by 2 and checking for remainders. 
while decimal != 0:
    if decimal % 2 == 0:
        decimal = decimal / 2
        binary.insert(0,0)
    else:
        decimal = (decimal - 1) / 2
        binary.insert(0,1)