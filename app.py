from flask import Flask, jsonify, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return "Welcome to the Placement Prediction API!"

@app.route('/contact')
def contact():
    return "Welcome to the Contact Page!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [[data['cgpa'], data['aptitude'], data['communication'], data['projects']]]
    
    prediction = model.predict(features)[0]
    
    return jsonify({'prediction': int(prediction)})

import os
if __name__ == '__main__':
    port=int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port, debug=True)