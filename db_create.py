from application import application
from db import db

db.init_app(application)

@application.before_first_request
def create_tables():
    from models.admin import AdminModel
    db.create_all()
    if AdminModel.get_id() == None:  #Required for initial heroku deploymenyt, commented after that
        AdminModel().save_to_db()    #Required for initial heroku deploymenyt, commented after that

if __name__ == "__main__":
    application.run()

# from app import app
# from db import db
# from models.admin import AdminModel
#
# def create_app():
#     db.init_app(app)
#     return app
#
#
# @app.before_first_request
# def create_tables():
#     print("Function create tables")
#     db.create_all()
#     # if AdminModel.get_id() == None:  #Required for initial heroku deploymenyt, commented after that
#     AdminModel().save_to_db()    #Required for initial heroku deploymenyt, commented after that
#
# if __name__ == "__main__":
#     appl = create_app()
#     print("Executed create_app")
#     appl.app_context().push()
#     print("Executed push")
#     # db.create_all()
#     # AdminModel().save_to_db()
