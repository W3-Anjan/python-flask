from flask import Flask, request, jsonify, make_response, render_template, session # importing Flask package in the File
import jwt
from datetime import datetime, timedelta
from functools import wraps


# create an object of the flask class
# We send the following argument to the default constructor `__name__`,
# this will help Flask look for template and static files
app = Flask(__name__)
app.config['SECRET_KEY'] = 'aed28d4f894f476b9435456281f8e399'

# A decorator is a function that 
# 1. takes a function to be wrapped as its only parameter and
# 2. returns a wrapping function

def token_required(func):

    # When you are using a decorator, you are replacing wrapped function with wrapping function signature.
    #
    # functools.wraps() helps to keep the signature of the wrapped function i.e: _name_, __doc__
    # instead of wrapping function.

    @wraps(func) # functools.wraps() keeps the signature of the wrapped function.
    def decorated(*args, **kwargs): # it takes positional arguments and keyword arguments
        token = request/args.get('token') 
        if not token:
            return jsonify({'Alert!':'Token is missing!'})
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'])   
        except:
            return jsonify({'Alert': 'Invalid Token!'})    

    return decorated        


# Next, we use the route decorator to help define which 
# routes should be navigated to the following function.

# Home
@app.route('/')
def home():
    # if user is not loggedin then redirect or render a page called login else loggedin currently
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        # return 'Logged in currently!' 
        return render_template('login.html')  

# Public
@app.route('/public') 
def public():
    return 'For Public'   


# Authenticated decorator
@app.route('/auth')
@token_required
def auth():
    return 'JWT is verified. Welcome to your dashboard!'



@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] and request.form['password'] == '123456':
        session['logged_in'] = True # set this List index True
        # create a JWT token with the combination of username + expiry time + SERVER_SECRET_KEY
        token = jwt.encode({
            'user':request.form['username'],
            'expiration': str(datetime.utcnow() + timedelta(seconds=120)) # expired in 2 min
        },app.config['SECRET_KEY']) 

        return jsonify({'token': token})   
    else:
        return make_response('Unable to verify', 403, {'WWW-Authenticate' : 'Basic realm: "Authentication Failed!"'})    


if __name__ == "__main__":
    app.run(debug=True)    
