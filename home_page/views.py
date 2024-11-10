import flask
from flask_mail import Message
from .models import Data
from main.settings import DATABASE
from .mail import mail
def render_home():
    if flask.request.method == "POST":
        data = Data(
            name = flask.request.form["name"],
            email = flask.request.form['email'],
            review = flask.request.form["review"]
        )
        DATABASE.session.add(data)
        DATABASE.session.commit()
        admin = "nikitagodovanyj@gmail.com"
        msg = Message(
            subject = f'Клієнт {data.name} {data.email}',
            recipients = [admin],
            body = f'Клієнт {data.name} залишив/ла Відгук: \n\n\n{data.review}' 
        )
        # mail.send(msg)
        # 
        # try:
        mail.send(msg) 
        # except:
        #     return "Error sending email"
    return flask.render_template(template_name_or_list = 'home.html' )