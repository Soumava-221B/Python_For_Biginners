def maximum3(n1, n2, n3):
    '''
    Objective: To find maximum of three numbers
    Input Parameters: n1, n2, n3 - numeric values
    Return Value: maxNumber - numeric value
    '''
    if n1 > n2:
        if n1 > n3:
            maxNumber = n1
        else:
            maxNumber = n3
    elif n2 > n3:
        maxNumber = n2
    else:
        maxNumber = n3
    return maxNumber

def main():
    '''
    Objective: To find maximum of three numbers provided as input
    by user
    Input Parameter: None
    Return Value: None
    '''
    print('Enter three numbers to find which one is Maximum \n')
    n1 = int(input('Enter the first number '))
    n2 = int(input('Enter the second number '))
    n3 = int(input('Enter the third number '))
    maximum = maximum3(n1,n2, n3)
    print('Maximum number is ', maximum)

if __name__ == '__main__':
    main()
