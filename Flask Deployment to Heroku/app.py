import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
import joblib

app = Flask(__name__)
model = joblib.load('xgb.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(pd.DataFrame(final_features, columns= ['brand', 'model', 'speed', 'timetilend', 'current bid count',
                                                                                'stand over height', 'gear shifter brand', 'front derailleur brand',
                                                                                'rear derailleur brand', 'brake lever brand', 'crank set brand',
                                                                                'brake type']))

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Bike price should be $ {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)