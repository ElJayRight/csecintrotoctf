from flask import Flask, request,jsonify
import jwt, base64, json, os
from database import *
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
        return jsonify({"welcome message":"No source code, no dev artifacts and a stronger token. It has to be secure now",
                        "endpoints":{"login [POST]":"/login?username=&password=",
                        "create user [POST]":"/create?username=&password=",
                        "admin [GET]":"/admin"}}),200

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if 'username' in data and 'password' in data:
        username = data['username']
        password = data['password']
        if login_check(username, password) == True:
            with open("./secret_token",'r') as file:
                secret = file.readline.strip()
            token = jwt.encode(
                {'username':username}, str(secret),algorithm='HS256',headers={"kid":'./secret_token'}
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
    secret = get_secret(token)
    try:
        payload = jwt.decode(token, secret, algorithms=['HS256'])
        if payload['username'] == 'admin':
            with open('./flag.txt','r') as file:
                data = file.readlines()[0]
            return {'message': 'Admin access granted!',
                    'flag':data}, 200
        else:
            return {'error': 'Unauthorized access'}, 403
    except jwt.InvalidTokenError:
        return {'error': 'Invalid token'}, 401

def get_secret(token):
    header = token.split('.')[0]
    header = header + "=" * (4 - (len(header)%4))
    kid = json.loads(base64.b64decode(header).decode())['kid']
    with open(kid,'r') as file:
        secret = file.readline().strip()
    return secret
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2534)
