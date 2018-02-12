from flask import render_template, redirect
from app import app
from flask import request
from app.forms import LoginForm

@app.route('/ttt/', methods=['GET','POST'])
def ttt():
	form = LoginForm()
	if form.validate_on_submit():
			print("Logged in!")
			return redirect('/play/')
	return render_template('login.html', title='Sign In', form=form)

@app.route('/play/')
def play():
	return "Play!"