# ChurnGuard - Customer Churn Prediction Web Application

ChurnGuard is a machine learning-powered web application designed to help businesses predict customer churn. By analyzing various customer attributes, this tool estimates the likelihood of a customer leaving the service. Early identification of at-risk customers allows businesses to take preventive measures and improve retention rates.

## 🚀 Features

- User-friendly interface built with Bootstrap 4
- Predicts customer churn using a trained ML model
- Takes multiple customer inputs such as gender, tenure, services used, contract type, and payment method
- Instant prediction with probability and churn risk level
- Fully responsive and clean UI
- Python Flask backend for handling model and logic

## 🧠 Tech Stack

- **Frontend**: HTML, CSS, Bootstrap 4, FontAwesome
- **Backend**: Python, Flask
- **ML Model**: Trained using scikit-learn (or similar)
- **Deployment**: Flask local server (can be extended to Heroku, Render, etc.)

## 🧾 Requirements

- Python 3.x
- Flask
- scikit-learn
- pandas
- numpy
- joblib (for model loading)

Install dependencies using:
```bash
pip install -r requirements.txt
```

## 📂 Project Structure

```
churnguard/
│
├── static/
│   └── styles.css              # Custom CSS styling
│
├── templates/
│   └── index.html              # Main form and layout
│   └── result.html             # Result display page
│
├── model/
│   └── churn_model.pkl         # Pre-trained ML model (scikit-learn joblib format)
│
├── app.py                      # Main Flask application
├── requirements.txt            # Required Python packages
└── README.md                   # Project documentation
```

## ⚙️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/yourusername/churnguard.git
cd churnguard
```

2. Activate your virtual environment (optional but recommended)

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Place your trained model in the model folder as `churn_model.pkl`

5. Run the application:
```bash
python app.py
```

6. Open your browser and go to:
```
http://127.0.0.1:5000/
```

## 📊 Model Info

The ML model is trained using logistic regression (or other suitable algorithm) on a customer churn dataset. You should preprocess the input features to match the model expectations (label encoding, scaling, etc.).

## ✅ Sample Input Fields

- Gender (Male/Female)
- Senior Citizen (Yes/No)
- Partner (Yes/No)
- Dependents (Yes/No)
- Tenure
- Phone Service (Yes/No)
- Internet Service (DSL/Fiber optic/No)
- Online Security (Yes/No/No internet service)
- Contract Type (Month-to-month/One year/Two year)
- Payment Method (Electronic check/Credit card/etc.)
- Monthly Charges
- Total Charges

## 🧪 Demo Screenshot

[You can add a screenshot of your form and prediction result page here.]

## 🧑‍💻 Author

- Parveen Saroha
- [LinkedIn](#)
- [GitHub](#)

## 📄 License

This project is licensed under the MIT License. Feel free to use and modify it for personal or commercial purposes.

---

**ChurnGuard – Predict, Prevent, Prosper.**
