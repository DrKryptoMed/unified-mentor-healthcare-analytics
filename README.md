# Unified Mentor Healthcare Data Analytics Portfolio

**Internship:** Unified Mentor — Healthcare Data Analyst  
**Duration:** 2026  
**Domain:** Healthcare Data Analytics & Data Science  

---

## Portfolio Overview

This repository contains 5 end-to-end healthcare data analytics projects completed 
as part of the Unified Mentor internship programme. Each project combines SQL-driven 
analysis, exploratory data analysis, data visualisation and machine learning using 
real-world healthcare datasets.

---

## Projects

### Project 1 - COVID-19 Clinical Trials EDA
- **Dataset:** ClinicalTrials.gov via Kaggle (5,783 trials, 27 columns)
- **Tools:** Python, Pandas, SQLite, Matplotlib, Seaborn
- **Key Findings:** 48% of trials still recruiting at data capture, April 2020 
registration spike coinciding with WHO pandemic declaration, US and France leading 
global trial contributions
- **Skills:** Multi-column missing data classification (MAR/MCAR/MNAR), 
feature engineering, time series analysis

---

### Project 2 - Drugs, Side Effects and Medical Conditions
- **Dataset:** Drugs.com via Kaggle (2,931 drugs, 17 columns)
- **Tools:** Python, Pandas, SQLite, Matplotlib, Seaborn
- **Key Findings:** 47% of drugs interact with alcohol, only 18 drugs are 
completely safe in pregnancy (Category A), opioids dominate highest user ratings 
reflecting both effectiveness and dependency risk
- **Skills:** Delimited string parsing, binary feature engineering, 
pharmaceutical domain analysis

---

### Project 3 - Life Expectancy Analysis
- **Dataset:** WHO and United Nations (2,938 rows, 193 countries, 2000-2015)
- **Tools:** Python, Pandas, SQLite, Scikit-learn, Matplotlib, Seaborn
- **Key Findings:** 12.1 year life expectancy gap between developed and developing 
countries, Schooling is the strongest linear predictor (r=0.72), Random Forest 
achieves R²=0.966 and RMSE=1.71 years
- **Skills:** Panel data imputation, multicollinearity detection, Linear Regression, 
Random Forest, feature importance analysis

---

### Project 4 - OCD Patient Demographics and Clinical Data
- **Dataset:** OCD Patient Dataset (1,500 patients, 17 columns)
- **Tools:** Python, Pandas, SQLite, Matplotlib, Seaborn
- **Key Findings:** 70% of patients have Severe or Extreme OCD, average symptom 
duration over 10 years, 51% comorbid depression and 50% comorbid anxiety, 
dataset identified as synthetically generated through uniform distribution analysis
- **Skills:** Y-BOCS clinical scoring, severity classification, 
comorbidity analysis, synthetic data detection

---

### Project 5 - Tobacco Use and Mortality (2004-2015)
- **Dataset:** HSCIC England (5 CSV files: fatalities, admissions, smokers, 
metrics, prescriptions)
- **Tools:** Python, Pandas, SQLite, Scikit-learn, XGBoost, SHAP, Gradio
- **Key Findings:** 18.5% decline in smoking-related deaths over 10 years, 
simultaneous 22% rise in admissions reflecting public health paradox, tobacco 
price index is the strongest mortality predictor confirmed by both EDA and SHAP
- **Skills:** Multi-table SQL joins, XGBoost classification, SHAP explainability, 
Gradio web app deployment

---

## Repository Structure
unified_mentor_projects/
├── project_1_covid_trials/
│   └── covid_trials_eda.ipynb
├── project_2_drugs_side_effects/
│   └── drugs_side_effects_eda.ipynb
├── project_3_life_expectancy/
│   └── life_expectancy_eda.ipynb
├── project_4_ocd_patients/
│   └── ocd_patients_eda.ipynb
├── project_5_tobacco_mortality/
│   ├── tobacco_mortality_eda.ipynb
│   ├── app.py
│   └── requirements.txt
└── README.md

## Tools and Technologies

- **Languages:** Python, SQL
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, XGBoost, SHAP, Gradio
- **Database:** SQLite (one database per project)
- **Environment:** Jupyter Notebook, VS Code
- **Deployment:** Gradio (Project 5)

---

## Key Skills Demonstrated

- SQL-driven analysis with SQLite across all projects
- Missing data classification using MAR, MCAR and MNAR framework
- Healthcare domain interpretation of clinical findings
- Machine learning including regression and classification models
- Model explainability using SHAP values
- Interactive web application development with Gradio