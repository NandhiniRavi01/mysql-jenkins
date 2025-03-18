from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS
import bcrypt

app = Flask(__name__)
CORS(app)

# MySQL Configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "nandhu01",
    "database": "user_db"
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data['username']
    password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        return jsonify({"message": "User registered successfully!"}), 201
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 400
    finally:
        cursor.close()
        conn.close()

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password'].encode('utf-8')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if user and bcrypt.checkpw(password, user[0].encode('utf-8')):
        return jsonify({"message": f"Welcome, {username}!"})
    else:
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
     app.run(host="0.0.0.0", port=5000, debug=True)


