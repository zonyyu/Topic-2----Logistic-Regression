from flask import Flask, render_template, jsonify, request
import requests

# import all of these modules
import numpy as np
import torch
from sklearn.preprocessing import PolynomialFeatures



model = torch.jit.load('suv_predictor.pt')
model.eval() # set it to eval mode

# We need to convert 3 input features into the 20 polynomial features
# that the model can accept
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

    # Convert gender to lower case, and handle invalid inputs
    gender = gender.lower()
    if gender == 'male':
        gender = 0
    elif gender == 'female':
        gender = 1
    elif gender == 'other':
        gender = 1
    else:
        return jsonify({"code": 500, "msg": "Invalid Gender"})


    # Age must be integer
    try:
        age = int(age)
    except ValueError:
        return jsonify({"code": 500, "msg": "Invalid Age"})

    
    # Salary must be integer
    try:
        salary = int(salary)
    except ValueError:
        return jsonify({"code": 500, "msg": "Invalid salary"})


    # form input variables into a 1x20 torch.tensor
    inputs_raw = np.array([[age, salary, gender]])
    inputs_poly = poly.fit_transform(inputs_raw)
    inputs = torch.from_numpy(inputs_poly).float()

    # make prediction
    pred = model(inputs).item() #.item() gets the value from the tensor
    result = "YES"
    if pred < 0.5:
        result = "NO"

    print(result)
    

   
    return jsonify({"code": 200, "msg": result})


if __name__ == "__main__":
    app.run(debug=True)