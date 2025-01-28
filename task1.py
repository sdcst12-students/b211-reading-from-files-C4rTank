#!python3
'''
Read the data from the file task01.txt
Create a function called find().
Find will require 1 input parameter that is a string literal.
The return value is the line number (starting at 0) that the parameter to be found is on.

Example:
assert find('apple') == 0
assert find('fish') == 5
'''
def find(word):

    #print("What word would you like to find")
    #word = input(': ')
    

    filename = 'task01.txt'
    file = open(filename)
    DATA = file.read()

    myList = DATA.split('\n')

    #print(myList)

    num = -1

    for items in myList:
        num = num + 1
        if items == word:
            #print("success",num)
            break
    return num







    # find out what line the "word" is on and return it




#DONE


if __name__ == "__main__":
    assert find('apple') == 0
    assert find('fish') == 5