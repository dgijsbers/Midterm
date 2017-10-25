from flask import Flask, render_template
from flask import request
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Required
import requests
import json

app = Flask(__name__)
app.debug = True 

# At least 3 different routes
	#At least one route should employ set_cookie and use the 
	#make_response function so a cookie is set in that request

class ProfileForm(FlaskForm):
	username = StringField('Enter a username:', validators=[Required()])
	description = fields.RadioField('What best describes you?', choices=['Parent on-the go', 'Student on a budget', 'Workaholic'])
	submit = SubmitField('Submit')

@app.route('/profile')
def profile_form():
	simpleForm = ProfileForm()
	return render_template('profile-form.html', form=simpleForm)

@app.route('/Profile', methods = ['GET', 'POST'])
def profile():
	form = ProfileForm(request.form)
	if request.method == 'POST' and form.validate_on_submit():
		username = form.username.data
		description = form.description.data
		return "Welcome {0}! I'm RecipeGenie and I'm here to help with meals that work around your schedule!".format(username)
	flash('All fields are required!')
	return redirect(url_for('index'))

#At least 1 written form, written with WTForms, with correct/reasonable
#action and method
	#data should be entered into this and submitted 
	#submitting data via the form should cause a visible result 
	# manipulating it in a way that's not just printing it out 

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

	#NOT REQUIRED BUT USEFUL:
		#redirects
		#the url_for function
		#template extensions







if __name__ == '__main__':
	app.run(debug = true)







