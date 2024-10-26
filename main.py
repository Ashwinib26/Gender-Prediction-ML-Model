from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model (Assuming you have a pickle model named 'gender.pkl')
model = pickle.load(open('gender.pkl', 'rb'))

@app.route('/')
def index():
    # Renders the index.html page
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Collect data from the form
        long_hair = float(request.form['long_hair'])
        forehead_width_cm = float(request.form['forehead_width_cm'])
        forehead_height_cm = float(request.form['forehead_height_cm'])
        nose_wide = float(request.form['nose_wide'])
        nose_long = float(request.form['nose_long'])
        lips_thin = float(request.form['lips_thin'])
        distance_nose_to_lip_long = float(request.form['distance_nose_to_lip_long'])

        # Create an array for the model input (7 features)
        input_data = np.array([[long_hair, forehead_width_cm, forehead_height_cm, nose_wide, nose_long, lips_thin, distance_nose_to_lip_long]])
        
        # Make a prediction using the loaded model
        prediction = model.predict(input_data)[0]

        # Convert numerical prediction to human-readable output
        gender = 'Male' if prediction == 1 else 'Female'

        # Pass the prediction to the result template
        return render_template('result.html', prediction=gender)

@app.route('/result')
def results():
    # Just renders the result page, data is passed from 'submit' view function
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
