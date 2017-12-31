from flask import Flask
from flask_mail import Mail, Message

# mail = Mail()

app =Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'testbyyuuki@gmail.com'
app.config['MAIL_PASSWORD'] = 'fgrlspuehhaxlhey'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
print(app.config)
# mail.init_app(app)
mail = Mail(app)

@app.route("/")
def index():
    msg = Message('Tutorial point3', sender = 'testbyyuuki@gmail.com', recipients = ['k.yuuki3327@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail "
    mail.send(msg)
    return "Sent"

if __name__ == '__main__':
    app.run(debug = True)
