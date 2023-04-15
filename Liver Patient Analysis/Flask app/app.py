from flask import Flask, render_template, request
 import numpy as np
import pickle
app=Flask( name ) 
@app.route('/')
def home():
return render_template('home.html') 
@app.route('/predict')
def index():
return render_template("index.html")
@app.route('/data_predict', methods=['POST']) 
def predict():
    data = [[float(age), float(gender), flot(tb), float(db), float(ap), float(aa1), float(aa2), 
         float(tp),
         model =pickle.load(open('liver_analysis.pkl', 'rb'))
         prediction= model.predict(data)[0] 
if (prediction == 1):
return render_template('noChance.html', prediction='you have a liver desease problem,you must and:)
else:
return render_template('Chance.html', prediction='you dont have a liver desease problem')
if name == ' main ': app.run()