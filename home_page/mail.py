import flask_mail

from main.settings import project



project.config['MAIL_SERVER'] = 'smtp.gmail.com'
project.config['MAIL_PORT'] = 587
project.config['MAIL_USE_TLS'] = True
project.config['MAIL_USE_SSL'] = False
project.config['MAIL_USERNAME'] = "flasksite050807@gmail.com"
project.config['MAIL_PASSWORD'] = 'bzfs ydzf fdnf kfpe'
project.config['MAIL_DEFAULT_SENDER'] = "flasksite050807@gmail.com"

mail = flask_mail.Mail(app = project)