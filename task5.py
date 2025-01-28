"""
Read the data from the file task02.csv
Allow the user to search for a stock symbol.
If the stock symbol is found, display the name of the company
If a multiple stocks match the symbol, say there are multiple stocks available
If there is no match, say "no match found"

Example:
Enter stock symbol: AA
There are 21 stocks with that symbol
Enter stock symbol: AAPL
Apple Inc.
Enter stock symbol: YANG
No matches
"""

print("Look up a stock symbol")
SYMBOL = input( ': ' )

x = 0

filename = 'task5.csv'
file = open(filename,'rt')
DATA = file.readlines() 
  
#How many there are
for LINE in DATA:
    if SYMBOL in LINE:
        x = x + 1



#If there is 0. Type name
if x == 1:
    for LINE in DATA:
        if SYMBOL in LINE:
            LINE = LINE.replace(SYMBOL , "")
            LINE = LINE.replace("," , "")

            print("---")
            print("")
            print(LINE)
            print("---")


#there is none
if x == 0:

    print("---")
    print("No matches")
    print("---")

if x > 2:

    print("---")
    print("There are" ,x, "stocks with that symbol")
    print("---")

#DONE