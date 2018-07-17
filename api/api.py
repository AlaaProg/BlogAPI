from flask  import Blueprint
from .views.user  import UserAPI
from .views.admin import AdminAPI

api = Blueprint("UserAPI",__name__) 


# UserAPI  
userApi = UserAPI.as_view('UserAPI') 
api.add_url_rule("/user",defaults={'ID':None},view_func=userApi)
api.add_url_rule("/user/<int:ID>",view_func=userApi,methods={'GET','POST'})


adminApi = AdminAPI.as_view('AdminAPI')
api.add_url_rule("/admin/",view_func=adminApi,methods={"GET",'POST'})
api.add_url_rule("/admin/<int:Id>",view_func=adminApi,methods={'GET','DELETE','PUT'})