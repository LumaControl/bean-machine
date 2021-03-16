# Bean machine: Binary converter

This "binary machine" turns decimal numbers into binary numbers and vice versa.


The decimal to binary function uses division by 2 with remainders to define the length and value of the binary output. it puts this into an array.

Binary to decimal converter checks if the input consists of {1,0} and nothing else. Program will return to main function if this is not the case. If it is, the input will become an array which will be checked in length, to multiply each bit by the correct power and add them together.
