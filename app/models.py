from app import DB

class User(DB.Model):
	""" User class """

	__tablename__ = "users"
	id = DB.Column(DB.Integer, primary_key=True)
	name = DB.Column(DB.String(64))

	def __init__(self, name=None):
		self.name = name