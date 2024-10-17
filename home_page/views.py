import flask
from flask_mail import Message
from .models import Data
from main.settings import DB
from .mail import mail
def render_home():
    if flask.request.method == "POST":
        data = Data(
            name = flask.request.form["name"],
            email = flask.request.form['email'],
            review = flask.request.form["review"]
        )
        DB.session.add(data)
        DB.session.commit()

        msg = Message(
            subject = f'Клієнт {data.name}',
            recipients = [flask.request.form["email"]],
            body = f'Клієнт {data.name} залишив/ла Відгук{data.review}' 
        )
        # mail.send(msg)
        try:
            mail.send(msg) 
        except:
            print("Ошибка при отправке email")
    return flask.render_template(template_name_or_list = 'home.html' )