#!python3
# Advanced Dungeons and Dragons

"""
the file task04.txt contains a matrix of values
The row indicates the level of fighter. Row 1 is for a level 1 fighter, row 2 is for a level 2 fighter and so on

In each row, the numbers indicate the target number needed out of 20 to land a hit on a specific Armor Class, 
starting with
10 on the left, followed by 9, then 8, all the way to -10 on the far right.

Create a function that reads the specific value for a 
specific level and an armor class, and prints the target number needed.

"""


def target(lvl,ac):
    
    x = 0
    o = 0

    filename = 'task04.txt'

    with open(filename, 'r') as file_data: 
        for line in file_data: 
            data = line.split() 
            x = x + 1
    #finding lvl
            if x == lvl:
                break
    #finding ac


    for a in data:
        o = o + 1

    o = o/2
    o = o - ac
    o = int(o)

    A = (data[o])
    A = int(A)

    return A
   
    #-10 to 10 in rows



def tests():
                #(y, x)
    assert target(3,7) == 11
    assert target(9,-1) == 13
    assert target(13,-10) == 20
if __name__=="__main__":
    tests()

#DONE