from flask import Flask, render_template,jsonify,request

import config

from Project_app.utils import MedicalInsurance

app = Flask(__name__)

############################################ Base API #########################################################

@app.route("/")
def hello_flask():
    print("Hello i am sameer learn flask")
    return "we are creating flack for Mediacl Isurance model"

########################################## Model predicted Insurance API #########################################

@app.route("/Predicted_insurance")
def get_insurance_charges():
    age = 31
    sex ='male'
    bmi = 20.5
    children = 2
    smoker  = 'no'
    region = 'northeast'

    med_ins = MedicalInsurance(age,sex, bmi,children,smoker,region)
    charges = med_ins.get_predicted_insurance()

    return jsonify ({"Result": f"Predicted medical insurance charges are:{charges}"})

if __name__ == "__main__":
    app.run()