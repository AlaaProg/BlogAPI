import time
from flask.views import MethodView
from flask       import request,jsonify,abort
from api.model.decoratorAdmin import Required
from application import sql


class AdminAPI(MethodView):
	"""docstring for AdminAPI"""

	decorators = [Required]
	

	# Get  AllPOST/PostById
	def get(self,Id=None):

		if Id:
			post    = sql.select("post","`postID`,`title`,`date`,`post`,`keys`",'`postID`=%s'%Id)
			command = sql.select("commande","`user`,`commedn`",'`postID`=%s'%Id)
			data = {"post":post[0] if post != [] else None,"command":command}
			return jsonify(data)

		posts = sql.select("post")
		return jsonify({"data":posts})
		
	# ADD POST 
	def post(self):

		try:

			data = request.form.to_dict()
			datatime = time.strftime("%d-%d-%Y", time.localtime())
			sql.insert("post",{'title':data['title'],'date':datatime,'post':data['post'],'keys':data['keys']})

		except KeyError as err:
			return jsonify({"error":'miss %s'%err})

		except Exception as err:
			return jsonify({"error":'%s'%err})

		return jsonify({"Successfuly":' add Post'})

	# UPDATE POST By Id 
	def put(self,Id):

		try:
			data = request.form.to_dict()
			datatime = time.strftime("%d-%d-%Y", time.localtime())
			data.update(date=datatime)
			fetch = sql.update("post",data,'`postID`=%s'%Id)

		except Exception as err:
			return jsonify({"error":'error %s'%err})

		return jsonify({"Successfuly":'Successfuly update Post %s'%Id})

	# DELETE POST By Id 
	def delete(self,Id):
		try:
			fetch = sql.delete("post",'`postID`=%s'%Id)
		except Exception as err:
			return jsonify({"error":'error %s'%err})

		return jsonify({"Successfuly":'Successfuly Reomve Post %s'%Id})


