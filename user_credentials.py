class User:
	'''
	A class for creating accounts and saving account info
	'''
	users_list[]
	def __init__(self,fname,lname,pwd)
		'''
		Creating method to define properties held by each user object
		'''

		#Variables
		self.fname = fname
		self.lname = lname
		self.pwd = pwd 

	def save_user(self)
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
	def check_user(cls,fname,pwd)
		'''
		To authenticate using matching entries for name and password saved
		'''

		current_user = ''
		for user in User.users_list:
			if (user.fname == fname and user.pwd == pwd):
				current_user = user.fname
		return current_user

	def __init__(self,u_name,s_name,acc_name,pwd)
		'''
		Defining properties held by each user object
		'''

		#Variables
		self.u_name = u_name
		self.s_name = s_name
		self.acc_name = acc_name