import mysql.connector as sql 

class MySQL():

	# Start MySQL
	def __init__(self,**config):
		try:
			self.sql = sql.connect(**config)
			#  (
			#      buffered=None, raw=None, prepared=None, 
			#      cursor_class=None, dictionary=None, named_tuple=None
			# )
			self.cur = self.sql.cursor(dictionary=True)
		except sql.Error as er:
			print(er)
	

	def select(self,table,col="*",where="1=1",limit=100):
		self.cur.execute("SELECT %s FROM %s WHERE %s LIMIT %d"%(col,table,where,limit))

		return self.cur.fetchall()

	def insert(self,table,data):

		cols   = ",".join([ '`'+i+'`' for i in data.keys()])
		values = str(tuple(data.values()))


		self.cur.execute("INSERT INTO %s (%s) VALUES %s"%(table,cols,values))
		self.sql.commit()


	def delete(self,table,where):
		# DELETE FROM `post` WHERE `post`.`postID` = 8

		self.cur.execute("DELETE FROM `%s` WHERE %s "%(table,where))
		self.sql.commit()

	def update(self,table,data,where):
		# UPDATE `post` SET `postID` = '1' WHERE `post`.`postID` = 11;

		cols = ['`%s` ="%s"'%(v,k) for v,k in data.items()]
		cols = ','.join(cols)

		self.cur.execute("UPDATE `%s` SET %s WHERE %s"%(table,cols,where))
		self.sql.commit()

