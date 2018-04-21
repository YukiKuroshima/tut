from flask import Flask
from flask_mail import Mail, Message

mail = Mail()

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')

# mail = Mail(app)
print(app.config)
mail.init_app(app)

@app.route("/")
def index():
    print('Sending email')
    msg = Message('Tutorial point3', sender = '@gmail.com', recipients = ['@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail "
    mail.send(msg)
    return "Sent"

if __name__ == '__main__':
    app.run()
