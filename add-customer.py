from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/customer")
def customer():
    return render_template("customer.html")

@app.route("/summary", methods=["POST"])
def summary():
    name = request.form["first_name"]
    surname = request.form["last_name"]
    full_name = name + " " + surname
    #customer_id = random.randint(100000,5000000)
    customer_id = 3235378

    return render_template("summary.html", name=full_name, customer_id=customer_id)

if __name__ == "__main__":
    #app.run(debug=False, host='0.0.0.0', port=int(os.getenv('PORT', '80')), threaded=True)
    app.run(debug=False, host='0.0.0.0', port='80', threaded=True)