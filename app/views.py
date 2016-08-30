from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Chuckie' } # fake user
    posts = [
    	{
    		'author': { 'nickname':'Chuckie'},
    		'body': 'Beautiful day in Portland'
    	},
    	{
    		'author':{ 'nickname':'Peter'},
    		'body':'The Avengers movie was so cool!'
    	}
    ]
    return render_template("index.html", 
    	title='Home' ,
    	user = user  ,
    	posts = posts
    	)

@app.route('/login', methods = ['GET', 'POSE'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="' + form.Openid.data+ '", remember_me=' +str(form.remember_me.data))
		return redirect('/index')
	return render_template("login.html",
		title = 'Sign in',
		form = form
		)
