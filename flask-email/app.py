from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config.update(
        DEBUG=True,
        #EMAIL SETTINGS
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=465,
        MAIL_USE_SSL=True,
        MAIL_USERNAME = 'testbyyuuki@google.com',
        MAIL_PASSWORD = 'fgrlspuehhaxlhey'
        )

mail=Mail(app)

@app.route("/")
def index():
    msg = Message('Snippet', sender = 'testbyyuuki@gmail.com', recipients = ['k.yuuki3327@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"


if __name__ == "__main__":
    app.run()
