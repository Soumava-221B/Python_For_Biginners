import sys
def areaRectangle(length, breadth):
    '''
    Objective to compute the area of rectangle
    Input Parameters: length, breadth - numeric value
    Return Value: area - numeric value
    '''

    area = length * breadth
    return area

def main():
    '''
    Objective: To compute the area of rectangle based on user input
    taken as command line arguments
    Input Parameter: None
    Retrun Value: None
    '''

    if len(sys.argv)  == 3:
        lengthRect = int(sys.argv[1])
        breadthRect = int(sys.argv[2])
        areaRect = areaRectangle(lengthRect, breadthRect)
        print('Area of rectangle is ',areaRect)

if __name__ == '__main__':
    main()

print('\nEnd of Program')
