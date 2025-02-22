### Gender Prediction Web App using Machine Learning and Flask
#### This project is a web-based gender prediction system that uses machine learning to classify gender based on facial attributes. Built with Flask, it takes user inputs for features like long hair, forehead width, nose width, lips thinness, etc. and predicts whether the person is Male or Female using a pre-trained model.

#### Project workflow is as follows -
#### 1. Data Collection & Preprocessing:

#####     The dataset consists of various facial features labeled with gender.
#####   Features are normalized using StandardScaler for better model performance.
#### 2.Model Training :

#####   A Logistic Regression model was trained on the dataset.
#####   The trained model (gender.pkl) and scaler (scaler.pkl) were saved using pickle.
#### 3. Web Application Development :

#####   The app was developed using Flask, with an index page (index.html) for input and a result page (result.html) to display predictions.
#####   User inputs are preprocessed and passed through the model to generate predictions.

#### 4. Future Scope : 
#####   This project can be further enhanced by integrating deep learning models (CNNs) for image-based gender detection, improving UI, and deploying it online. 🚀
