import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)

# Function to get data from MySQL
def get_products():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='2006',
        database='mydb'
    )

    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT id, name, price FROM products")

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows

# Route
@app.route('/')
def home():
    data = get_products()
    return render_template('index.html', products=data)

# Run server
if __name__ == '__main__':
    app.run(debug=True)