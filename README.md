

# **🚀 Gender Prediction Web App using Machine Learning and Flask**  

## **📌 Project Overview**  
This project is a **web-based gender prediction system** that utilizes **Machine Learning** to classify gender based on **facial attributes**. Built with **Flask**, it takes user inputs for features like **long hair, forehead width, nose width, lips thinness, etc.** and predicts whether the person is **Male** or **Female** using a machine learning model.  

---

## **📌 Project Workflow**  

### **1️⃣ Data Collection & Preprocessing**  
✔️ The dataset consists of various **facial features labeled with gender**.  
✔️ Features are **normalized** using `StandardScaler` for **better model performance**.  

### **2️⃣ Model Training**  
✔️ A **Logistic Regression** model was trained on the dataset.  
✔️ The trained model (`gender.pkl`) and **scaler** (`scaler.pkl`) were **saved** using `pickle`.  

### **3️⃣ Web Application Development**  
✔️ Developed using **Flask** with:  
   - 📌 **`index.html`** – Input form for user data.  
   - 📌 **`result.html`** – Displays the predicted gender.  
✔️ **User inputs** are preprocessed and passed through the model to generate predictions.  

---

## **🌟 Future Scope**  
🚀 Enhance the project by integrating **Deep Learning models (CNNs)** for **image-based gender detection**.  
🎨 Improve the **UI/UX** for a more interactive experience.  
🌍 Deploy the model **online** for public use.  

---

💡 **Contributions and suggestions are welcome!** Feel free to fork, star ⭐, and improve this project.  

---
