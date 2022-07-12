def printTable(nTables = 10, nMultiples = 10):
    '''
    Objective: To print multiplication table of numbers in range
    [1,nTables], comprising of first nMultiples
    Input Parameters:
        nTables: numeric - number of tables to be printed
        nMultiples: numeric - number of multiples of a number
                    to be printed
        Output: Multiplication tables of numbers, beginning 1 ending
                nTables
        Return Value: None
    '''
    for multiple in range(1, nMultiples + 1):
        # Print a row of multiples of each number num
        for num in range(1, nTables + 1):
            print('{0: >2}'.format(num), '*', \
                  '{0: >2}'.format(multiple), '=', \
                  '{0: >3}'.format(num*multiple),'\t', end = '')
        print()

def main():
    '''
    Objective: To display table of numbers in range [1, nTables]
    comprising of first 10 multiples
    Input Parameters: None
    Return Value: None
    '''
    nTables = int(input('Enter number of multiplication tables: '))
    printTable(nTables)
if __name__=='__main__':
    main()
