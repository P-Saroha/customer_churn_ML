# app.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load reference data and model
df_1 = pd.read_csv("first_telc.csv")
model = pickle.load(open("customer_churn.sav", "rb"))

# Tenure grouping
tenure_labels = ["{0} - {1}".format(i, i + 11) for i in range(1, 72, 12)]

@app.route("/")
def loadPage():
    return render_template("home.html", query="")

@app.route("/", methods=["POST"])
def predict():
    try:
        input_data = [
            request.form['query1'],  # SeniorCitizen
            request.form['query2'],  # MonthlyCharges
            request.form['query3'],  # TotalCharges
            request.form['query4'],  # gender
            request.form['query5'],  # Partner
            request.form['query6'],  # Dependents
            request.form['query7'],  # PhoneService
            request.form['query8'],  # MultipleLines
            request.form['query9'],  # InternetService
            request.form['query10'], # OnlineSecurity
            request.form['query11'], # OnlineBackup
            request.form['query12'], # DeviceProtection
            request.form['query13'], # TechSupport
            request.form['query14'], # StreamingTV
            request.form['query15'], # StreamingMovies
            request.form['query16'], # Contract
            request.form['query17'], # PaperlessBilling
            request.form['query18'], # PaymentMethod
            request.form['query19']  # tenure
        ]

        # Build input DataFrame
        columns = ['SeniorCitizen', 'MonthlyCharges', 'TotalCharges', 'gender', 'Partner', 'Dependents',
                   'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
                   'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract',
                   'PaperlessBilling', 'PaymentMethod', 'tenure']
        new_df = pd.DataFrame([input_data], columns=columns)

        # Convert numeric columns to appropriate types
        new_df['SeniorCitizen'] = new_df['SeniorCitizen'].astype(int)
        new_df['MonthlyCharges'] = new_df['MonthlyCharges'].astype(float)
        new_df['TotalCharges'] = pd.to_numeric(new_df['TotalCharges'], errors='coerce')
        new_df['tenure'] = new_df['tenure'].astype(int)

        # Combine with reference data for consistent encoding
        combined_df = pd.concat([df_1, new_df], ignore_index=True)

        # Create tenure_group
        combined_df['tenure_group'] = pd.cut(
            combined_df['tenure'].astype(int), bins=range(1, 80, 12), right=False, labels=tenure_labels)
        combined_df.drop(columns=['tenure'], inplace=True)

        # Get dummies
        dummy_df = pd.get_dummies(combined_df[
            ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService',
             'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
             'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
             'Contract', 'PaperlessBilling', 'PaymentMethod', 'tenure_group']
        ])

        # Align input with model columns
        final_input = dummy_df.tail(1).reindex(columns=model.feature_names_in_, fill_value=0)

        # Predict
        prediction = model.predict(final_input)[0]
        probability = model.predict_proba(final_input)[0][1]

        if prediction == 1:
            o1 = "This customer is likely to be churned!!"
        else:
            o1 = "This customer is likely to continue!!"

        o2 = "Confidence: {:.2f}%".format(probability * 100)

        return render_template('home.html',
                               output1=o1,
                               output2=o2,
                               **request.form)

    except Exception as e:
        return f"Internal Server Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
