# app.py - Tobacco Mortality Risk Prediction as Gradio Web App
import gradio as gr
import pickle
import numpy as np

# Load model, scaler and features
with open("rf_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("features.pkl", "rb") as f:
    features = pickle.load(f)

def predict_mortality_risk(
    total_admissions,
    smoking_prevalence,
    affordability_index,
    tobacco_price_index,
    expenditure_pct,
    prescriptions
):
    # Prepare input
    input_data = np.array([[
        total_admissions,
        smoking_prevalence,
        affordability_index,
        tobacco_price_index,
        expenditure_pct,
        prescriptions
    ]])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0]

    risk_label = "HIGH Mortality Risk" if prediction == 1 else "LOW Mortality Risk"
    confidence = probability[prediction] * 100

    return (
        f"Prediction: {risk_label}\n"
        f"Confidence: {confidence:.1f}%\n\n"
        f"High Risk Probability : {probability[1]*100:.1f}%\n"
        f"Low Risk Probability  : {probability[0]*100:.1f}%"
    )

# Build Gradio interface
with gr.Blocks(title="Tobacco Mortality Risk Predictor") as app:
    gr.Markdown("""
    # Tobacco Use and Mortality Risk Predictor
    **Healthcare Analyst Internship at Unified Mentor**
    
    This tool predicts whether a given year's tobacco-related indicators 
    correspond to HIGH or LOW smoking-related mortality risk in England.
    Enter the values below and click Predict.
    """)

    with gr.Row():
        with gr.Column():
            total_admissions = gr.Slider(
                minimum=1000000, maximum=2000000, value=1500000, step=10000,
                label="Total Smoking-Related Admissions")
            smoking_prevalence = gr.Slider(
                minimum=15, maximum=30, value=22, step=1,
                label="Smoking Prevalence % (16 and Over)")
            affordability_index = gr.Slider(
                minimum=55, maximum=85, value=70, step=0.5,
                label="Affordability of Tobacco Index")

        with gr.Column():
            tobacco_price_index = gr.Slider(
                minimum=220, maximum=340, value=270, step=1,
                label="Tobacco Price Index Relative to Retail Price Index")
            expenditure_pct = gr.Slider(
                minimum=1.5, maximum=2.5, value=1.8, step=0.1,
                label="Expenditure on Tobacco as % of Total Expenditure")
            prescriptions = gr.Slider(
                minimum=1000, maximum=3000, value=2000, step=50,
                label="All Pharmacotherapy Prescriptions (thousands)")

    predict_btn = gr.Button("Predict Mortality Risk", variant="primary")
    output = gr.Textbox(label="Prediction Result", lines=6)

    predict_btn.click(
        fn=predict_mortality_risk,
        inputs=[total_admissions, smoking_prevalence, affordability_index,
                tobacco_price_index, expenditure_pct, prescriptions],
        outputs=output
    )

    gr.Markdown("""
    ### Feature Reference Ranges (2004-2014 England Data)
    | Feature | Low Risk Range | High Risk Range |
    |---------|---------------|-----------------|
    | Total Admissions | > 1,500,000 | < 1,500,000 |
    | Smoking Prevalence | < 21% | > 21% |
    | Affordability Index | < 75 | > 75 |
    | Tobacco Price Index | > 260 | < 260 |
    """)

if __name__ == "__main__":
    app.launch()