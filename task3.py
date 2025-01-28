#!python
# Sum of Values

"""
The file task03.txt contains a lot of data.  
Each cluster of data is the number of points for that particular group.  
Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787
"""

filename = 'task03.txt'
file = open(filename,'r')
DATA = file.readlines()

def MAX(DATA):
    
    x = 0
    myList = []


    while x < 2236:

        NUMBER = (DATA[x]) 

        try:
            NUMBER = int(NUMBER)

            myList.append(NUMBER)

        except:
            NOT_NUMBER = NUMBER



        print(NUMBER)

        x = x + 1
    
    myList.sort(reverse = True)
    print(myList)
    print("")
    max_NUMBER = (myList[0])
    print("The largest value in the text file is", max_NUMBER,)


#DONE

def find(DATA):
    for x in DATA:
        if x == '68787':
            print("founded")
        else:
            print("Number does not exist")
    
MAX(DATA)