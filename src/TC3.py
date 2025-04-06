

class UserManager:
	def __init__(self):
		super(UserManager, self).__init__()
		self.users = {}
		

	def add_user(self, username, email):
		if username in self.users:
			raise ValueError("User already exists")		
		self.users[username] = email
		return True

	def get_user(self, username):
		return self.users.get(username)
		# return self.users.get(username, None)