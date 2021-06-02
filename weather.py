from flask import Flask, render_template, jsonify, request
import requests

API_KEY = "f12232d12cec76017908394e18223b48"
CITY = "Edmonton"


app = Flask(__name__)


@app.route('/')
def main():
    api_call = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}")
    print("print", jsonify(api_call.text))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)