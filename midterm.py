from flask import Flask, render_template, redirect, url_for, flash
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, fields, RadioField, IntegerField, SubmitField
from wtforms.validators import Required
import requests
import json
from flask_script import Manager, Shell
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'
app.config['HEROKU_ON'] = os.environ.get('HEROKU')

#app.debug = True
def make_shell_context():
    return dict(app=app)

# At least 3 different routes

class ProfileForm(FlaskForm):
	username = StringField('Enter a username:', validators=[Required()])
	choice = RadioField('Are you looking for recipes or food videos?', choices=[('Recipes!','Recipes!'), ('Videos!', 'Videos!')])
	submit = SubmitField('Submit')

@app.route('/profile', methods = ['GET', 'POST'])
def profile_form():
	simpleForm = ProfileForm()
	return render_template('profile-form.html', form=simpleForm)

@app.route('/result', methods = ['GET', 'POST'])
def profile():
	form = ProfileForm(request.form)
	if request.method == 'POST' and form.validate_on_submit():
		username = form.username.data
		choice = form.choice.data
		result = request.args
		base_url = "http://www.recipepuppy.com/api/"
		params = {}
		params['recipe'] = 'title'
		response = requests.get(base_url, params)
		data = json.loads(response.text)
		if choice == "Recipes!":
			return render_template('recipe_links.html', results = data["results"], username = username)
		if choice == "Videos!":
			return render_template('videos.html', username = username)
	flash('All fields are required!')
	#return redirect(url_for('profile'))

@app.route('/result/<ingredients>', methods = ['GET', 'POST'])
def spec_artist(ingredients):
	result = request.args
	base_url = "https://recipepuppy.com/api/"
	params = {} 
	params['recipe']='title'
	params['ingredients'] = ingredients
	response = requests.get(base_url, params)
	data = json.loads(response.text)
	#print(params)

	return render_template('more.html', results = data['results'])

#At least one route should employ set_cookie and use the 
#make_response function so a cookie is set in that request 

@app.route('/cookie')
def set_cookie(self, response): 
	redirect_to_profile = redirect('/profile')
	response = current_app.make_response(redirect_to_profile)
	response.set_cookie('cookie_name',value='values')
	return response

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500
#At least 2 dynamic links appearing inside template files (links to 
	#other pages within the application) that send data through the URL 
	#(Like itunes data, similar to data on Solange and Kendrick Lamar in HW3)

#At least 1 image saved in a static/ directory and rendered on a page 

#At least 3 different templates, using render_template
	#including:
		#1 jinja templating language for a loop (to show a list of things)
		#1 jinja templating conditional statement (to only show something 
		 	# in a certain case)
		#these 3 must not contain custom error messages 

#At least 2 custom error message templates/error handlers (did in section)
	#one should be a 404 error page
	# the other can be to handle any type of error you want, but it must 
	#be a genuinely possible error code (like 400 or 500, more in section materials)








if __name__ == '__main__':
#	app.run(debug = True)
	app.run







