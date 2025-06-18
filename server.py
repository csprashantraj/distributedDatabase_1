from flask import Flask, jsonify, request
from enc import encrypt_data
from dec import decrypt_data
import db
from decimal import Decimal, getcontext

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True, port=8000)
