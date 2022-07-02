def areaRectangle(length, breadth):
    '''
    Objectives: To compute the area of rectangle
    Input Parameters: length, breadth - numeric value
    Return Value: area - numeric value
    '''
    area = length * breadth
    return area

def main():
    '''
    Objectives: To compute the area of rectangle based on user input
    Input Parameter: None
    Return Value: None
    '''

    print('Enter the following values for rectangle:')
    lengthRect = int(input('Length: integer value: '))
    breadthRect = int(input('Breadth: integer value: '))
    areaRect = areaRectangle(lengthRect, breadthRect)
    print('Area of rectangle is', areaRect)

if __name__=='__main__':
    main()
print('\nEnd of Program')
