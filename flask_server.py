from flask import Flask, json
import requests
cities = [
    {'id': 1, 'name': 'Arc'},
    {'id': 2, 'name': 'Moscow'},
    {'id': 3, 'name': 'Nizhniy Novgorod'}
]


app = Flask(__name__)

@app.route('/fib/<int:data>', methods=['GET'])
def fibonacci(data):
    data -= 2
    fib1 = 1
    fib2 = 1
    while data > 0:
        fib1, fib2 = fib2, fib1 + fib2
        data -= 1
    return json.dumps(fib2, indent=4)


@app.route('/cities', methods=['GET'])
def get_cities():
    return json.dumps(cities, indent=4)


@app.route("/")
def main_page():
    return "<p>Welcome to Flask!</p>"

if __name__ == '__main__':
    app.run(debug=True, port=9999)