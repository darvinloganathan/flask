from flask import *
from flask_mail import *
app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'vishnuloganathan1999@gmail.com'
app.config['MAIL_PASSWORD'] = '22471278'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

users = [{'name': 'dare','email':'darvinloganathan@gmail.com'},
         {'name': 'vishnu', 'email':'vishnuloganathan@gmail.com'}]
mail = Mail(app)

@app.route("/")
def index():
    with mail.connect() as con:
        for user in users:
            msgs = Message(recipients=[user['email']],
                           body='auto generated mail using flask ',
                           subject='flask mail ext',
                           sender='er.kalaiselvan111@gmail.com')
            con.send(msgs)
    return " message sent"

if __name__ == "__main__":
    app.run(host='127.0.0.20',debug=True)