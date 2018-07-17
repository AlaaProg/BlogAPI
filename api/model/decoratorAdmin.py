from flask import request,jsonify,abort
from application import sql


class Required:
	def __init__(self,*args):
		self.args = args

	def __call__(self,**kw):

		fetch = sql.select("admin","user,password","user='%s' and password='%s' "%(
					request.headers.get('API-AdminUser'),request.headers.get('API-AdminPass')))


		if len(fetch) == 0:
			return jsonify({'Error':'Password/Username Not Correct'}),403


		return self.args[0](**kw)
