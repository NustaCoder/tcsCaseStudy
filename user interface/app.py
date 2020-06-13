from flask import Flask,render_template

app = Flask(__name__)

# for executive
@app.route("/")
def layout():
    return render_template("Customer/home.html")

#customer management
@app.route("/create_screen/")
def screen():
    return render_template("Customer/customer_screen.html")

@app.route("/customer_search/")
def search():
    return render_template("Customer/customer_search.html")

#account management
@app.route("/create_account/")
def create():
    return render_template("Customer/create_account.html")
@app.route("/account_search/")
def acc_search():
    return render_template("Customer/account_search.html")

# status
@app.route("/customer_status/")
def cus_status():
    return render_template("Customer/cust_account_statement.html")
@app.route("/account_status/")
def acc_status():
    return render_template("Customer/account_statement.html")


# transfer
@app.route("/transfer/")
def transfer():
    return render_template("Customer/transfer_money.html")


if __name__ == "__main__":
    app.run(debug=True)