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