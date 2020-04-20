#! /usr/bin/env python3
from user_credentials import User, Credential

def create_user(fname,lname,pwd):
	'''
	Function to create a new user account
	'''
	new_user = User(fname,lname,pwd)
	return new_user

def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_user(user)


def verify_user(fname,pwd):
	'''
	Function that verifies the pwd of the user before creating credentials
	'''
	checking_user = Credential.check_user(fname,pwd)
	return checking_userpwd

def generate_password():
	'''
	Function to generate a pwd automatically
	'''
	gen = Credential.generate_password()
	return gen

def create_credential(u_name,s_name,acc_name,pwd):
	'''
	Function to create a new credential
	'''
	new_credential=Credential(u_name,s_name,acc_name,pwd)
	return new_credential

def save_credential(credential):
	'''
	Function to save a newly created credential
	'''
	Credential.save_credentials(credential)

def display_credentials(u_name):
	'''
	Function to display credentials saved by a user
	'''
	return Credential.display_credentials(u_name)
	
def copy_credential(s_name):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credential.copy_credential(s_name)

def main():
	print(' ')
	print('Hello! Welcome to PyPasswordLocker.')
	while True:
		print(' ')
		print("-"*60)
		print('Use these codes to navigate: \n CA - Create an Account \n LI - Log In \n EX -Exit')
		short_code = input('Enter a navigation code: ').upper().strip()
		if short_code == 'EX':
			break

		elif short_code == 'CA':
			print("-"*60)
			print(' ')
			print('To create a new account:')
			fname = input('Enter your first name - ').strip()
			lname = input('Enter your last name - ').strip()
			pwd = input('Enter your password - ').strip()
			save_user(create_user(fname,lname,pwd))
			print(" ")
			print(f'New Account Created for: {fname} {lname} using password: {pwd}')
		elif short_code == 'LI':
			print("-"*60)
			print(' ')
			print('To login,please enter your account details:')
			u_name = input('Enter your first name - ').strip()
			pwd = str(input('Enter your password - '))
			user_exists = verify_user(u_name,pwd)
			if user_exists == u_name:
				print(" ")
				print(f'Welcome {u_name}. Please choose a navigation code to continue.')
				print(' ')
				while True:
					print("-"*60)
					print('Navigation codes: \n CC - Create a Credential \n DC - Display Credentials \n COPY - Copy pwd \n EX-Exit')
					short_code = input('Enter a navigation code: ').upper().strip()
					print("-"*60)
					if short_code == 'EX':
						print(" ")
						print(f'Session closed for {u_name}')
						break
					elif short_code == 'CC':
						print(' ')
						print('Enter your credential details:')
						s_name = input('Enter the site\'s name- ').strip()
						acc_name = input('Enter your account\'s name - ').strip()
						while True:
							print(' ')
							print("-"*60)
							print('Please choose a code for creating your password: \n EP - enter existing pwd \n GP - generate a pwd \n EX-exit')
							psw_choice = input('Enter a code: ').upper().strip()
							print("-"*60)
							if psw_choice == 'EP':
								print(" ")
								pwd = input('Enter your pwd: ').strip()
								break
							elif psw_choice == 'GP':
								pwd = generate_password()
								break
							elif psw_choice == 'EX':
								break
							else:
								print('Try another navigation code')
						save_credential(create_credential(u_name,s_name,acc_name,pwd))
						print(' ')
						print(f'Credential Created: Site Name: {s_name} - Account Name: {acc_name} - Password: {pwd}')
						print(' ')
					elif short_code == 'DC':
						print(' ')
						if display_credentials(u_name):
							print('Here is a list of saved credentials')
							print(' ')
							for credential in display_credentials(u_name):
								print(f'Site Name: {credential.s_name} - Account Name: {credential.acc_name} - Password: {credential.pwd}')
							print(' ')	
						else:
							print(' ')
							print("You don't seem to have any credentials saved yet")
							print(' ')
					elif short_code == 'COPY':
						print(' ')
						chosen_site = input('Enter the site name for the credential password to copy: ')
						copy_credential(chosen_site)
						print('')
					else:
						print('Try another navigation code')

			else: 
				print(' ')
				print('An error occurred. Please try again')		
		
		else:
			print("-"*60)
			print(' ')
			print('Wrong option entered. Please try again')
				






if __name__ == '__main__':
	main()

