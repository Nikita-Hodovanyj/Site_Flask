import flask_login
from .settings import project
from user.models import Users

project.secret_key = 'MBj9fhzsP9KfPpriVGEtt2ZNwYqTmzH0K'

login_manager = flask_login.LoginManager(app = project)

login_manager.init_app(project)

@login_manager.user_loader
def load_user(id):
    return Users.query.get(id)