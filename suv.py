from flask import Flask, render_template, jsonify, request
import requests
import numpy as np

import import_ipynb
from suv_purchase import Logreg
import torch
from sklearn.preprocessing import PolynomialFeatures



model = Logreg(20, 1)
model.load_state_dict(torch.load('suv_predictor.pt'))
model.eval()

poly = PolynomialFeatures(degree=3)


app = Flask(__name__)


@app.route('/')
def main():

    return render_template("index.html")

@app.route('/call', methods=["GET"])
def get_weather():

    gender = request.args.get("gender")
    age = request.args.get("age")
    salary = request.args.get("salary")

    gender = gender.lower()
    if gender == 'male':
        gender = 0
    elif gender == 'female':
        gender = 1
    elif gender == 'other':
        gender = 1
    else:
        return jsonify({"code": 500, "msg": "Invalid Gender"})


    try:
        age = int(age)
    except ValueError:
        return jsonify({"code": 500, "msg": "Invalid Age"})

    
    try:
        salary = int(salary)
    except ValueError:
        return jsonify({"code": 500, "msg": "Invalid salary"})



    inputs_raw = np.array([[age, salary, gender]])
    inputs_poly = poly.fit_transform(inputs_raw)

    inputs = torch.from_numpy(inputs_poly).float()

    pred = model(inputs).item()
    result = "YES"
    if pred < 0.5:
        result = "NO"
    

   
    return jsonify({"code": 200, "msg": result})


if __name__ == "__main__":
    app.run(debug=True)