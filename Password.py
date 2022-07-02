def authenticateUser(password):
    '''
    Objective to authenticate user and allow access to system
    Input parameter: password - string
    Return Value: message - string
    '''
    if password == 'magic':
        message = 'Login Successful!!\n Welcome to System.'
    if password != 'magic':
        message = 'Password mismatch!!\n'
    return message

def main():
    '''
    Objective: To authenticate user
    Input Parameter: None
    Return Value: None
    '''

    print('\t LOGIN SYSTEM')
    print('===================')
    password = input('Enter Password:')
    message = authenticateUser(password)
    print(message)

if __name__=='__main__':
    main()
