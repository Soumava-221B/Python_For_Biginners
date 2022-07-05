'''
Program to display the multiplication table
Using for loop
'''
n = int(input('Enter the number till which you want the table: '))
number = int(input('Enter the nuber of which the user wants to print the multiplication table: '))
print('The Multiplication Table of: ', number)
for count in range(1, n+1):
    print(number, 'x', count, '=', number*count)
