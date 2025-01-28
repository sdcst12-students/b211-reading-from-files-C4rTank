"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  
Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, 
and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""

filename = 'task02a.txt'
file = open(filename,'r')
data = file.readlines()


def Pythagorean(data):

    Pythagorean_Triples = 0
    NOT_Pythagorean_Triples = 0

    a = 0
    b = 1
    c = 2

    while a < 1200:

        NUM_1 = (data[a]) 
        NUM_2 = (data[b])
        NUM_3 = (data[c])  

        NUM_1 = int(NUM_1)
        NUM_2 = int(NUM_2)
        NUM_3 = int(NUM_3)

        if (NUM_1^2) * (NUM_2^2) == NUM_3^2:
            Pythagorean_Triples = Pythagorean_Triples + 1
        else:
            NOT_Pythagorean_Triples = NOT_Pythagorean_Triples + 1

        a = a + 4
        b = b + 4
        c = c + 4

        print(Pythagorean_Triples)
        print(NOT_Pythagorean_Triples)

    print("There are" ,Pythagorean_Triples, "Pythagorean Triples")

    
Pythagorean(data)

#DONE