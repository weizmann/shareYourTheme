import torndb

def singleton(cls, *args, **kw):
	instances = {}
	def _singleton():
		if cls not in instances:
			instances[cls] = cls(*args, **kw)
		return instances[cls]
	return _singleton

@singleton
class DatabaseManager(object):	
	def __init__(self):
		self.__db = torndb.Connection(host = "localhost", 
										database = "share_theme", 
										user = "root",
										password = "")

	def query(self, query):
		self.__db.query(query)

	def execute(self, query):
		self.__db.execute(query)

	def close_connection(self):
		self.__db.close()

