import time 
import os
login = 123456781
password = 123456789

def check_amount_of_thing(attempts):
    return 'attempts' if attempts > 1 else "attempt"
attempts = 3
while True:
    enter_login = input("Enter your login: ")
    enter_password = input("Enter your password: ")

    enter_login = int(enter_login)
    enter_password = int(enter_password)

    if enter_login == login and enter_password == password:
        print(f'Your login and password are writed correctly.')
        break
    elif attempts > 1:
        attempts -= 1 
        print(f'Try it again. You have {attempts} {check_amount_of_thing(attempts)}')  
    else:
        print("You have used your all attempts. Please wait for 5 seconds...")
        time.sleep(5)
        attempts = 3
        os.system('cls')

