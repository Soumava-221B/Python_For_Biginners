'''
Objective: To find the sum of n numbers using while loop
'''
def main():
    total = 0
    number = int(input('Enter a number: '))
    while number != '':
        total += int(number)
        number = int(input('Enter a number: '))
    print('Sum of all input numbers is: ',total)

if __name__ == '__main__':
    main()

print('\nEnd of Program----------------------')
