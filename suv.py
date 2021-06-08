from flask import Flask, render_template, jsonify, request
import requests




app = Flask(__name__)


@app.route('/')
def main():

    return render_template("index.html")

@app.route('/call', methods=["GET"])
def get_weather():

    gender = request.args.get("gender")
    age = request.args.get("age")
    salary = request.args.get("salary")



   
    return jsonify({"code": 200, "msg": None})


if __name__ == "__main__":
    app.run(debug=True)