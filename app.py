##############################################################
# Chelsey H. 12/19/20
# Python for Data Science Program 1
#
# Program: Import & process a dataset provided by Nasa.
# Manipulate and display data for Calculus education purposes.
#
# File: app.py: Main file for site, renders templates.
##############################################################

# Tip: You can use multiple decorators on the same function,
# one per line, depending on how many different routes you want
# to map to the same function.

# Tip: If you want to use a different filename than app.py,
# define an environment variable named FLASK_APP and set its
# value to your chosen file.

##############################################################

# Imports
# Import Flask and create an instance of the Flask object.
from flask import Flask, render_template, flash, request
from datetime import datetime
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms.widgets import TextArea
app = Flask(__name__)

# Not very secret, secret_key
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

# Class - HomePage
class HomePage(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=1, max=35)])
    favorite = TextField('Favorite:', validators=[validators.required(), validators.Length(min=1, max=35)])
    suggest = StringField('Suggestion:', widget=TextArea(), validators=[validators.required()])

    # Site Page 1: Function 'home' - Obtain form data, validate then print output to file.
    # Flask's app.route decorator used to map the URL route '/' to this Function.
    @app.route("/", methods=['GET', 'POST'])
    def home():
        # Assign form data to a form
        # Request form data, print errors if any
        form = HomePage(request.form)
        print (form.errors)
        if request.method == 'POST':
            name=request.form['name']
            favorite=request.form['favorite']
            email=request.form['email']
            suggest=request.form['suggest']

            # Write form to file
            entry=(str(name)) + ', ' + (str(email)) + ', ' + (str(favorite)) + ', ' + (str(suggest))
            with open('outputfile.txt', 'w') as f:
                f.write(f'\n{entry}')
            #    f.write(str(name))
            #    f.write(str(favorite))
            #    f.write(str(email))
            #    f.write(str(suggest))

        # If form was filled properly and successfully retrieved, display success message.             
        if form.validate():
            flash('Thank you!')
        # Else, display error message.
        else:
            flash('Error: All the form fields are required.')

        # Return content
        return render_template(
            "home.html",
            date=datetime.now(),
            form=form
        )

# Site Page 2: Function 'questions' 
@app.route("/questions/")
def questions():
    # Return content, get footer info
    return render_template(
        "questions.html",
        date=datetime.now()
    )

# Site Page 3: Function 'calculations' 
@app.route("/calculations/")
def calculations():
    # Return content, get footer info
    return render_template(
        "calculations.html",
        date=datetime.now()
    )

# Site page 4 - Function 'blank
@app.route("/blank/")
def blank():
    # Return content, get footer info
    return render_template(
        "blank.html",
        date=datetime.now()
    )