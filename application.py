import os
from flask import Flask
from flask_restful import Api
from resources.users import UserRegister, UserDelete
from resources.titles import Browse, AddToList, DeleteFromList, ViewList
from resources.sessions import Login, Logout
from db import db
import json

application = Flask(__name__)

db.init_app(application)

# app.config['DEBUG'] = True   # required for local testing to create db, commented for cloud hosting

# App configuration: Get config from configuration file
with open("/tmp/beanstalk-database.json") as json_file:
    data = json.load(json_file)
    db_url = data['connection']

application.config['SQLALCHEMY_DATABASE_URI'] = db_url
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.secret_key = data['app_secret_key']
api = Api(application)

# Specify End-Points
# Endpoint: Home
@application.route('/')
def home_endpoint():
    text = 'Welcome to World TV Database. Browse your favrourite TV shows and movies. Sign up and save your watchlist.\
     More features coming up. Use service endpoints to use our services'
    return text, 200
# Main services endpoints
api.add_resource(UserRegister, '/register')
api.add_resource(Browse, '/browse/<title>')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(AddToList, '/add-to-list')
api.add_resource(DeleteFromList, '/delete-from-list')
api.add_resource(UserDelete, '/delete-user')
api.add_resource(ViewList, '/view-list')

if __name__ == '__main__':
    application.run()

