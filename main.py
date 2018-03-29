from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('user-form.html')

@app.route('/', methods=['POST'])
def validate_username():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify-password']
    email = request.form['email']


#if user enters nothing in box and tries to submit it.
    if username == "":
        username_error = "You must enter a Username."
        username = ""
    #else: #if username is less than 3 characters  or more than 20
        #if len(username) < 3 or len(username) > 20:
            #username_error = "That is not a valid username."
            #username = ""
        


    if password == "":
        error = "You must enter a Password."
        return redirect("/?error=" + error)
    if verify_password == "":
        error = "Passwords don't match."
        return redirect("/?error=" + error)

#if all user info is correct:
@app.route('/all-valid')
def all_valid():
    username = request.args.get('username')
    return '<h1>Welcome, {0}!</h1>'.format(username)


app.run()
