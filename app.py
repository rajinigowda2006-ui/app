from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="2006",
        database="mydb"
    )


# Show products
@app.route("/")
def home():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM productss")

    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "index.html",
        products=products
    )


# Add product
@app.route("/add_product", methods=["POST"])
def add_product():

    name = request.form["name"]
    price = request.form["price"]
    quantity = request.form["quantity"]


    conn = get_connection()
    cursor = conn.cursor()


    sql = """
    INSERT INTO productss(name, price, quantity)
    VALUES(%s,%s,%s)
    """


    cursor.execute(
        sql,
        (name, price, quantity)
    )


    conn.commit()


    cursor.close()
    conn.close()


    # After inserting, reload the page
    return home()



if __name__ == "__main__":
    app.run(debug=True)