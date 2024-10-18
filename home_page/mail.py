import flask_mail

from main.settings import project



project.config['MAIL_SERVER'] = 'smtp.gmail.com'
project.config['MAIL_PORT'] = 587
project.config['MAIL_USE_TLS'] = True
project.config['MAIL_USE_SSL'] = False
project.config['MAIL_USERNAME'] = "nikitagodovanyj@gmail.com"
project.config['MAIL_PASSWORD'] = 'uxeb xfxi rhhh vjrv'
project.config['MAIL_DEFAULT_SENDER'] = "nikitagodovanyj@gmail.com"

mail = flask_mail.Mail(app = project)