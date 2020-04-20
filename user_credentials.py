import random
import pyperclip
import string

# Global Variables
global users_list 
class User:
	'''
	A class for creating accounts and saving account info
	'''
	users_list = []
	def __init__(self,fname,lname,pwd):
		'''
		Creating method to define properties held by each user object
		'''

		#Variables
		self.fname = fname
		self.lname = lname
		self.pwd = pwd 

	def save_user(self):
		'''
		Takes new instances created by user and saves them
		'''
		User.users_list.append(self)

class Credential:
	'''
	Class for account credentials; passwords and saving info
	'''

	#Class_Variables
	credentials_list = []
	user_credentials_list = []
	@classmethod
	def check_user(cls,fname,pwd):
		'''
		To authenticate using matching entries for name and password saved
		'''

		current_user = ''
		for user in User.users_list:
			if (user.fname == fname and user.pwd == pwd):
				current_user = user.fname
		return current_user

	def __init__(self,u_name,s_name,acc_name,pwd):
		'''
		Defining properties held by each user object
		'''

		#Variables
		self.u_name = u_name
		self.s_name = s_name
		self.acc_name = acc_name
		self.pwd = pwd 
    #saving credentials
	def save_credentials(self):
		'''
		Saves new instances created by users
		'''
		Credential.credentials_list.append(self)
	#function to generate passwords
	def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
		'''
		Generate 8-char password as recommended for cc
		'''
		gen=''.join(random.choice(char) for _ in range(size))
		return gen

	@classmethod
	def display_credentials(cls,u_name):
		'''
		Display credentials saved
		'''
		user_credentials_list = []
		for credential in cls.credentials_list:
			if credential.u_name == u_name:
				user_credentials_list.append(credential)
		return user_credentials_list

	@classmethod
	def find_by_s_name(cls,s_name):
		user_credentials_list = []
		for credential in cls.credentials_list:
			if credential.u_name == u_name:
				user_credentials_list.append(credential)
		return user_credentials_list


	@classmethod
	def find_by_s_name(cls, s_name):
		'''
		Looking up credentials with the same site name
		'''
		for credential in cls.credentials_list:
			if credential.s_name == s_name:
				return credential

	@classmethod
	def copy_credential(cls,s_name):
		'''
		Method for copying credentials info
		'''
		find_credential = Credential.find_by_s_name(s_name)
		return pyperclip.copy(find_credential.pwd)

	@classmethod
	def delete_user_account(self):
		Credentials.users_list.remove(self)