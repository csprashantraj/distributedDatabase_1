from flask import Flask, jsonify, request
from flask_cors import CORS
from enc import encrypt_data
from dec import decrypt_data
import db
from decimal import Decimal, getcontext

app = Flask(__name__)

# Configure CORS to allow requests only from a specific origin
ALLOWED_ORIGIN = "https://multi-party-voting.onrender.com/"  # Replace with your actual website URL
cors = CORS(app, resources={r"/api/*": {"origins": ALLOWED_ORIGIN}})

# Set precision to handle very large numbers
getcontext().prec = 50

@app.route('/api', methods=['GET'])
def home():
    return "Welcome to the Crypto Project Distibuted System 1 API!"

@app.route('/api/store', methods=['POST'])
def store():
    data = request.get_json()
    id = data['id']
    x = data['x']
    y = data['y']

    # insert these values into table 
    db.cur.execute("""
        INSERT INTO keys (id, x, y)
        VALUES (%s, %s, %s)
    """, (id, x, y))
    db.conn.commit()
    return jsonify({'message': 'Data stored successfully'}), 200


@app.route('/api/retrieve', methods=['GET'])
def retrieve():
    data = request.get_json()
    id = data['id']

    db.cur.execute("""
        SELECT x, y FROM keys WHERE id = %s
    """, (id,))
    rows = db.cur.fetchall()

    result = [{'x': row[0], 'y': row[1]} for row in rows]

    return jsonify(result), 200

# Add error handler for invalid endpoints
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "This is an invalid endpoint"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=8000)
