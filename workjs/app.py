from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="2006",
        database="mydb"
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/products")
def api_products():

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(products)


if __name__ == "__main__":
    app.run(debug=True)