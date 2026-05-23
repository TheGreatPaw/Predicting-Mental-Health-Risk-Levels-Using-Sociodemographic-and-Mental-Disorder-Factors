# Predicting Mental Health Risk Levels Using Sociodemographic and Mental Disorder Factors

This project presents a **Classification-Based Assessment Model** designed to predict mental health risk levels (Low, Medium, or High) by analyzing demographic data and psychological scores. Utilizing the **SEMMA framework**, the study identifies that internal emotional states like depression and anxiety are far more predictive of risk than basic sociodemographic factors.

## 🔍 Overview
Mental disorders affect over 1 billion people globally. This study develops a predictive tool to assist in **early intervention** by classifying individuals into risk categories based on age, gender, stress, depression, and anxiety scores.

## ❓ Research Questions
1. How do age, gender, and mental-health related scores relate to risk levels?
2. Which factors are most useful in predicting Low, Medium, or High risk?
3. Can a **Decision Tree Model** accurately estimate a person’s risk level?

## 📊 Dataset
* **Source:** Publicly available synthetic mental health dataset.
* **Size:** 9,000 participants (4,500 male, 4,500 female).
* **Age Range:** 18–65 years.
* **Features:** Age, Gender, Stress Level, Depression Score, and Anxiety Score.
* **Target:** Risk Level (Low, Medium, High).

## 🛠 Methodology (SEMMA)
The study follows the **SEMMA** (Sample, Explore, Modify, Model, Assess) methodology:
*   **Sample:** Data split into **70% Training, 15% Validation, and 15% Testing** using stratified sampling.
*   **Explore:** EDA revealed a balanced dataset with no missing values or outliers.
*   **Modify:** Categorical variables (Gender, Risk) were **Label Encoded**; numeric variables were **Standardized**.
*   **Model:** A **Decision Tree Classifier** was trained to provide an interpretable rule-based system.
*   **Assess:** Evaluated using Accuracy, Precision, Recall, and F1-Score.

## 📈 Model & Performance
The **Decision Tree** model achieved stable performance, indicating no overfitting.

| Metric | Validation Set | Test Set |
| :--- | :--- | :--- |
| **Accuracy** | 80.9% | **82.4%** |
| **Precision** | 80.8% | 82.3% |
| **Recall** | 80.9% | 82.4% |
| **F1-Score** | 80.8% | 82.2% |

### Feature Importance
The study utilized **Pearson Correlation** and **SHAP values** to determine feature impact:
*   **Depression Score:** Strongest predictor (0.67 correlation).
*   **Anxiety Score:** Moderate predictor (0.52 correlation).
*   **Age, Gender, Stress:** Minimal to no direct relationship with risk levels.

## 💡 Key Insights
*   **Behavioral vs. Demographic:** Behavioral indicators (depression/anxiety) carry significantly more weight than sociodemographic factors.
*   **Risk Consistency:** The model was particularly strong at identifying **medium-risk cases**.
*   **Early Intervention:** This tool can help guide mental-health programs by highlighting vulnerable groups based on psychological scores.

## ⚠️ Limitations & Future Work
*   **Data Source:** The use of **synthetic data** may limit real-world generalization.
*   **Algorithm Scope:** The study focused on simple Decision Trees; future work should explore **Random Forests or Gradient Boosting**.
*   **Feature Expansion:** Future iterations could include social, environmental, or clinical factors and utilize real-world survey data.

## 👥 Authors
*   **Abdulkarim, Hamad D.**
*   **Ansary, Sausanah M.**
*   **Macarandas, Rohaimah S.**
*   **Ms. Nornina J. Dia**
*(Faculty of Information and Computing Sciences, Mindanao State University)*
