from flask import Flask, request,jsonify
import jwt, base64
from database import *
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
        return jsonify({"welcome message":"Welcome to my API!! Currently you can only create and view users.",
                        "endpoints":{"login [POST]":"/login?username=&password=",
                        "create user [POST]":"/create?username=&password=",
                        "admin [GET]":"/admin"}}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if 'username' in data and 'password' in data:
        username = data['username']
        password = data['password']
        if login_check(username, password) == True:
            token = jwt.encode(
                {'username':username}, '',algorithm='HS256'
                )
            return {'token':token}, 200
        else:
            return {'error':"Invalid username or password"},401
    else:
        return {'error':'Username and password are required'}, 400  
    

@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    if 'username' in data and 'password' in data:
        username = data['username']
        password = data['password']
        if check_user(username) == True:
             return {'error': 'Username already registered.'}, 401
        add_account(username, password)
        return {'message': 'User registered successfully'}, 201
    else:
        return {'error': 'Username and password are required'}, 400

@app.route('/admin', methods=['GET'])
def admin():
    if 'Authorization' not in request.headers:
        return {'error': 'No authentication header given'}, 403 
    token = request.headers.get('Authorization', '').split()[1]
    try:
        payload = jwt.decode(token, '', algorithms=['HS256'])
        if payload['username'] == 'admin':
            return {'message': 'Admin access granted!',
                    'flag':'CSEC{J50n_w3b_t0k3n5_fTw!}'}, 200
        else:
            return {'error': 'Unauthorized access'}, 403
    except jwt.InvalidTokenError:
        return {'error': 'Invalid token'}, 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2532)
