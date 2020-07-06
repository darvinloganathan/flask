from flask import *
from flask_mail import *
from random import *
app = Flask(__name__)
app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'vishnuloganathan1999@gmail.com'
app.config['MAIL_PASSWORD'] = '22471278'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
otp = randint(0000, 9999)
mail = Mail(app)
@app.route('/')
def index():
    return render_template("mail_index.html")
@app.route('/verify', methods=["POST"])
def verify():
    email = request.form["email"]
    msg = Message('OTP', sender='vishnuloganathan1999@gmail.com', recipients=[email])
    msg.body = str(otp)
    mail.send(msg)
    return render_template('verify.html')
@app.route('/validate', methods=["POST"])
def validate():
    user_otp = request.form['otp']
    if otp == int(user_otp):
        return "success"
    return "failure"
if __name__ == '__main__':
    app.run(host='127.0.0.40',debug=True)
