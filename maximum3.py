def max3(n1, n2, n3):
    '''
    Objective: To find maximum of two numbers
    Input Parameters: n1, n2, n3 - numeric values
    Return Values: number - numeric value
    '''
    def max2(n1, n2):
        '''
        Objective: To find maximum of two numbers
        Input Parameters: n1, n2 - numeric values
        Return Value: maximum of n1, n2 - numneric value
        '''
        if n1 > n2:
            return n1
        else:
            return n2
    return max2(max2(n1, n2), n3)

def main():
    '''
    Objective: To find maximum of three numbers provided as input
    by user
    Input Parameter: None
    Return Value: None
    '''
    n1 = int(input('Enter the first number '))
    n2 = int(input('Enter the second number '))
    n3 = int(input('Enter the third number '))
    maximum = max3(n1,n2,n3)
    print('Maximum number is ', maximum)

if __name__ == '__main__':
    main()
