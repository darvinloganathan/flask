from flask import *
from flask_mail import *
app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'vishnuloganathan1999@gmail.com'
app.config['MAIL_PASSWORD'] = '22471278'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def index():
    msg = Message('mail using flask', sender='vishnuloganathan1999@gmail.com',
                  recipients=['darvinloganathan@gmail.com'])
    msg.body = 'flask mail extension trail'
    mail.send(msg)
    return "message sent"

if __name__ == '__main__':
    app.run(host='127.0.0.10',debug=True)