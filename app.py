from flask import Flask, render_template, redirect, flash, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'bumblebee'


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'Buderimpropertyservices@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_app_specific_password'
app.config['MAIL_DEFAULT_SENDER'] = 'Buderimpropertyservices@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    msg = Message(subject, sender=email, recipients=['recipient@example.com'])
    msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    try:
        mail.send(msg)
        flash('Email sent successfully!', 'success')
    except Exception as e:
        flash(str(e), 'error')

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
