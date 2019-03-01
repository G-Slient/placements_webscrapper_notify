from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import SubmitField, validators, IntegerField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

##############################################

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app ,db)

app.config['SECRET_KEY'] = 'mysecretkey'

################################################

class mail_info(db.Model):

	__tablename__ = 'student'

	num = db.Column(db.Integer, primary_key=True)
	regid = db.Column(db.Integer)
	id = db.Column(db.Text)

	def __init__(self, regid, id):
		self.regid = regid
		self.id = id

	def __repr__(self):
		return f"{self.regid} and {self.id}"

class InfoForm(FlaskForm):

	reg_id = IntegerField('Registration Number:', [validators.required(), validators.NumberRange(min=10000, max=99999)])
	email = EmailField('Email Address', validators=[DataRequired()])
	submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
	form = InfoForm()
	if form.validate_on_submit():
		reg_id = form.reg_id.data
		email = form.email.data
		form.reg_id.data = ''
		form.email.data = ''

		sam = mail_info(reg_id,email)
		db.session.add(sam)
		db.session.commit()

		print(reg_id, email)
		return redirect(url_for('thankyou'))
	elif request.method == 'POST' and not form.validate_on_submit():
		return redirect(url_for('error'))

	return render_template('index.html', form=form)

@app.route('/thankyou')
def thankyou():
	return render_template('thankyou.html')

@app.route('/error')
def error():
	return render_template('error.html')

if __name__=='__main__':
	app.run(debug=True)
