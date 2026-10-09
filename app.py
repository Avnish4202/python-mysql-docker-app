import os
import time
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    # Retry mechanism to wait for MySQL container to start up
    retries = 5
    while retries > 0:
        try:
            conn = mysql.connector.connect(
                host=os.environ.get('MYSQL_HOST', 'mysql_db'),
                user=os.environ.get('MYSQL_USER', 'user'),
                password=os.environ.get('MYSQL_PASSWORD', 'password'),
                database=os.environ.get('MYSQL_DATABASE', 'appdb')
            )
            return conn
        except mysql.connector.Error as err:
            retries -= 1
            time.sleep(3)
    raise Exception("Could not connect to MySQL database.")

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS visits (id INT AUTO_INCREMENT PRIMARY KEY, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
    conn.commit()
    cursor.close()
    conn.close()

@app.route("/")
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO visits () VALUES ();")
    conn.commit()
    cursor.execute("SELECT COUNT(*) FROM visits;")
    count = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return f"<h1>Hello from Python inside Docker!</h1><p>Total Visits Recorded in MySQL: <strong>{count}</strong></p>"

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)