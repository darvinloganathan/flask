from flask import *
from flask_mail import *

app = Flask(__name__)

app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'er.kalaiselvan111@gmail.com'
app.config['MAIL_PASSWORD'] = '*!@#$%^&&'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route("/")
def index():
    msg = Message(subject="hello",body="hello",sender='er.kalaiselvan111@gmail.com',recipients=['er.kalaiselvan111@gmail.com'])
    #The with statement closes the resource automatically when the work is done\
    with app.open_resource(r"C:\Users\ADMIN\Desktop\Kalaiselvan_WFH_HOL\SS\Data_visualisation_1.png") as fp:
        msg.attach("Data_visualisation_1.png", "image/png", fp.read())
        mail.send(msg)
    return "sent"

if __name__ == "__main__":
    app.run(host='127.0.0.22',debug=True)