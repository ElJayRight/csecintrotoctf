from flask import Flask, request, jsonify, render_template
import sqlite3
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    try:
        username = request.args.get('username')
        password = request.args.get('password')

        if username and password:
            conn = sqlite3.connect("file:./vulnerable.db?mode=ro", uri=True)
            cursor = conn.cursor()
            query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
            cursor.execute(query)
            user = cursor.fetchone()
            conn.close()

            if user:
                with open("read_this.txt", "r") as file:
                    flag = file.read()
                return jsonify({'message': 'Login successful ' + str(flag)})
            else:
                return jsonify({'message': 'Invalid credentials'})
        else:
            return jsonify({'message': 'Username and password are required'})
    except:
        return jsonify({"message": "error"})



if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=2531)
