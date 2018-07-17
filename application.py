from flask    import Flask
from model.MySQLModel import MySQL

sql = MySQL(user="root",db="blog")


def createApp():

	app = Flask(__name__)
	
	# set Configer
	app.config.from_pyfile("setting.py")


	from api import api

	app.register_blueprint(api,url_prefix='/api/')

	return app


if __name__ == '__main__':

	# Run WSGI Server with localhost and port 8010
	app = createApp()
	app.run(
		host=app.config.get("HOST"),
		port=app.config.get("PORT")
	)