from flask import Flask, render_template, request
import requests
import csv

app = Flask(__name__)


def load_data():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    return response.json()


def save_data(data):
    with open('data.csv', 'w', newline='') as csvfile:
        csvfile.truncate()  # clear file

        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(['currency', 'code', 'bid', 'ask'])

        for exchange in data[0]['rates']:
            writer.writerow([exchange['currency'], exchange['code'], exchange['bid'], exchange['ask']])



@app.route("/", methods=['GET', 'POST'])
def index():
    data = load_data()
    save_data(data)

    rates = {}
    for rat in data[0]['rates']:
        code = rat['code']
        price = rat['ask']

        rates[code] = price

    app.logger.debug(rates)

    result = None

    if request.method == 'POST':
        currency = request.form['currency']
        amount = request.form['amount']
        price = rates[currency]

        app.logger.debug(f"{amount} {currency} {price}")

        result = float(amount) * float(price)

    return render_template("index.html",
                           title="Currency Calculator (PLN)",
                           rates=rates,
                           result=result)


if __name__ == '__main__':
    app.run(debug=True)