def main():
    '''
    Objective: To compute percentage for marks entered in n
    subjective
    Input Parameter: None
    Return Value: None
    '''
    n = int(input('Enter the subjects: '))
    totalMarks = 0
    print('Enter marks')
    for i in range(1, n+1):
        marks = float(input('Subject '+str(i)+': '))
        if marks >= 0 and marks <= 100:
            totalMarks += marks
    percentage = totalMarks / n
    print('Percentage is: ', percentage)

if __name__ == '__main__':
    main()
