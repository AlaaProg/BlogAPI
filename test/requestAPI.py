import requests as req 
import json 



class UserBlog:

	def __init__(self,url="http://127.0.0.1:8010/api/user/"):
		self.url = url

	def GetPost(self,Id=None):
		if Id:
			self.url = self.url+str(Id)

		blog = req.get(self.url)
		blog = blog.json()
		return blog

	def AddCommand(self,Id,email,command):
		blog = req.post(self.url+str(Id),data={"mail":email,'command':command})
		blog = blog.json()
		return blog


class AdminBlog():

	def __init__(self,username,password):
		self.url =  "http://127.0.0.1:8010/api/admin/"

		self.Session = req.Session()

		self.Session.headers.update({
			'API-AdminUser':username,
			'API-AdminPass':password
		})



	def getPost(self,PostId:int = None):
		if PostId:
			self.url = self.url+str(PostId)
		data = self.Session.get(self.url)
		return data.json()



admin = UserBlog()

print ( admin.GetPost(15) )

