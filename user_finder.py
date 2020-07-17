#this function is for making an account.
def user_signup():
    creat_user_name = input('Enter a username:  ')  #asking user to enter a username of their choice for making an account
    creat_user_pass = input('Enter a password:  ')  #asking user to enter a password of their choice for making an account
    confrm_pass = input('Enter your password again: ')  #confirming the previously entered password.
    
    #this loop help to tell the user that the password they entered in the confirm password field
    #is wrong an they have to re enter it again.
    while confrm_pass != creat_user_pass:
        print('Please enter the correct password')
        confrm_pass = input('Enter your password again: ')
    
    else:
        print("Your account is successfully created!!")
    
    user_dict[creat_user_name] = creat_user_pass

    sign_in = input('Do you want to log in to your account:  ')
    if sign_in == 'yes':
        user_login()
    
    else:
        pass


#this function is for logining in to the account.
def user_login():
    
    while True:
        try:
            login_user = input('Please enter your username:  ')
            login_pass = input('Please enter your password:  ')
            
            if user_dict[login_user] == login_pass:
                print('Welcome')
                return False
            else:
                print('UserName and PassWord do not matches')
        
        except KeyError:    #if the password do not matches then it raises keyword error.
            print('UserName and PassWord do not matches')



user_dict = {}
user_consent = input('Do you want to make an account? ')

if user_consent == 'yes':
    user_signup()

elif user_consent == 'no':
    login_cnsent = input('Do you want to log in??  ')
    
    if login_cnsent == 'yes':
        user_login()
    
    elif login_cnsent == 'no':
        ag_signup = input('Do you have an account')
        
        if ag_signup == 'yes':
            user_signup()
        
        else:
            print('Then what are you doing here.... \nGet Lost')
            pass




