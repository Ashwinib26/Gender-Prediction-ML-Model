from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

scaler = pickle.load(open('scaler.pkl', 'rb'))
model = pickle.load(open('gender.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        long_hair = float(request.form['long_hair'])
        forehead_width_cm = float(request.form['forehead_width_cm'])
        forehead_height_cm = float(request.form['forehead_height_cm'])
        nose_wide = float(request.form['nose_wide'])
        nose_long = float(request.form['nose_long'])
        lips_thin = float(request.form['lips_thin'])
        distance_nose_to_lip_long = float(request.form['distance_nose_to_lip_long'])

        input_data = np.array([[long_hair, forehead_width_cm, forehead_height_cm, nose_wide, nose_long, lips_thin, distance_nose_to_lip_long]])
        
        input_data = scaler.transform(input_data)  
        prediction = model.predict(input_data)[0]

        gender = 'Male' if prediction == 1 else 'Female'

        return render_template('result.html', prediction=gender)

@app.route('/result')
def results():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
