from flask.views import MethodView
from flask import request,jsonify,abort
from application import  sql



class UserAPI(MethodView):
	"""docstring for API"""

	def get(self,ID):

		if ID:
			post    = sql.select("post","`postID`,`title`,`date`,`post`",'`postID`=%s'%ID)#.to_dict()
			command = sql.select("commande","`user`,`commedn`",'`postID`=%s'%ID)#.to_dict()
			data = {"post":post[0],"command":command}
			return jsonify(data)

		posts = sql.select("post","`postID`,`title`,`date`,`post`")#.to_dict()
		return jsonify({"data":posts})
		


	# Add Command 
	def post(self,ID):
		data = request.form.to_dict()

		try:

			fetch = sql.insert('commande',{
				'user'    :data['mail'],
				'postID'  :ID,
				'commedn' :data['command']
			})

		except Exception as err:
			return jsonify({"msg":'error %s'%err})


		return jsonify({"msg":'seccussfly True'})