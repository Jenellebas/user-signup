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

    username_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""

    #if username is blank
    if username == "":
        username_error = "You must enter a username."
        username = ""

    #if username is less than 3 characters or more than 20
    if len(username) < 3 or len(username) > 20:
        username_error = "That is not a valid username."
        username = ""

    #if username has a space
    for char in username:
        if char == " ":
            username_error = "That is not a valid username."
            username = ""    

    #if password is blank
    if password == "":
        password_error = "You must enter a password."
        password = ""

    #if password is less than 3 characters or more than 20
    if len(password) < 3 or len(password) > 20:
        password_error = "That is not a valid password."
        password = ""

    #if password has a space
    for char in password:
        if char == " ":
            password_error = "That is not a valid password."
            password = ""    
    
    #if verify password is blank
    if verify_password == "":
        verify_password_error = "Passwords don't match."
        verify_password = ""

    #if password and verify password don't match
    if password != verify_password:
        verify_password_error = "Passwords don't match."
        verify_password = ""
        password = ""

    #if email is not between 3 and 20 characters long
    if len(email) != 0 and len(email) < 3 or len(email) > 20:
        email_error = "That is not a valid email."
        email = ""

    #if email has a space
    for char in email:
        if char == " ":
            email_error = "That is not a valid email."
            email = ""   
    
    #if email has more than 1 @
    char_count = 0
    for char in email:
        if char == "@":
            char_count += 1
            if char_count > 1:
                email_error = "That is not a valid email."
                email = ""
    
    #if email has more than 1 .
    char_count = 0
    for char in email:
        if char == ".":
            char_count += 1
            if char_count > 1:
                email_error = "That is not a valid email."
                email = ""
      


#check to see if any errors 
    if not username_error and not password_error and not verify_password_error and not email_error:
        username = username
        return redirect('/all-valid?username={0}'.format(username))
    else:
        return render_template('user-form.html', username=username, email=email, username_error=username_error, password_error=password_error, verify_password_error=verify_password_error, email_error=email_error)

#if all user info is correct:
@app.route('/all-valid')
def all_valid():
    username = request.args.get('username')
    return render_template('all-valid.html', username=username)

app.run()
