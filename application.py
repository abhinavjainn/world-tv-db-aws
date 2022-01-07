# import os
from flask import Flask
from flask_restful import Api
from resources.users import UserRegister, UserDelete
from resources.titles import Browse, AddToList, DeleteFromList, ViewList
from resources.sessions import Login, Logout

app = Flask(__name__)

# app.config['DEBUG'] = True   # required for local testing to create db, commented for cloud hosting

# App configuration: Database and app secret key
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:myflaskapp@worldtv.clpbmthmix50.eu-west-2.rds.amazonaws.com" # For Heroku, comment for local execution #Updated for AWS
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'QMUL_CC_T12'
api = Api(app)

# Specify End-Points
# Endpoint: Home
@app.route('/')
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
    app.run()

