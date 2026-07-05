# 🛒 AI Dynamic Pricing System using Machine Learning

## 📌 Project Overview

The **AI Dynamic Pricing System** is a Machine Learning project designed to predict the **Purchase Probability** of products based on customer behavior, pricing strategies, product details, and shopping preferences. The system helps businesses optimize pricing decisions, improve sales, and enhance customer satisfaction through data-driven insights.

---

## 🎯 Problem Statement

Businesses often struggle to determine the optimal product price due to changing customer behavior, discounts, seasonal demand, and competition. Manual pricing strategies may lead to reduced sales or lower profits.

This project uses Machine Learning algorithms to analyze customer and product data and predict the likelihood of a purchase, enabling smarter pricing decisions.

---

## 🎯 Objectives

* Build a Machine Learning model to predict purchase probability.
* Perform data preprocessing and feature engineering.
* Compare multiple classification algorithms.
* Improve model performance using Hyperparameter Tuning.
* Deploy the final model using Streamlit.

---

## 📂 Dataset

The dataset contains customer, product, and transaction-related information.

### Features

* Product_ID
* Category
* Brand
* Customer_Age
* Customer_Gender
* Customer_Location
* Competitor_Price
* Historical_Demand
* Seasonal_Factor
* Inventory_Level
* Discount
* Payment_Method
* Shipping_Method
* Customer_Rating
* Purchase_History
* Product_Rating
* Review_Count
* Purchase_Probability (Target Variable)

---

## 🛠️ Technologies Used

* Python
* Jupyter Notebook
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit
* Joblib

---

## 📊 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Encoding
5. Feature Scaling
6. Train-Test Split
7. Model Building
8. Hyperparameter Tuning
9. Model Evaluation
10. Model Comparison
11. Model Saving
12. Streamlit Deployment

---

## 🤖 Machine Learning Models

The following classification models were implemented:

* Naive Bayes Classifier
* K-Nearest Neighbors (KNN)
* Decision Tree Classifier

---

## ⚙ Hyperparameter Tuning

Model optimization was performed using:

* GridSearchCV
* RandomizedSearchCV

This improved model accuracy and helped identify the best-performing parameters.

---

## 📈 Model Evaluation Metrics

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* Classification Report

---

## 📁 Project Structure

```
AI-Dynamic-Pricing-System/
│
├── data/
│   └── ecommerce_dynamic_pricing_dataset.csv
│
├── notebooks/
│   └── Dynamic_Pricing_System.ipynb
│
├── models/
│   ├── model.pkl
│   ├── scaler.pkl
│   └── encoder.pkl
│
├── app.py
├── requirements.txt
├── README.md
└── images/
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/AI-Dynamic-Pricing-System.git
```

Move into the project directory:

```bash
cd AI-Dynamic-Pricing-System
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Application

Launch the Streamlit application:

```bash
streamlit run app.py
```

---

## 📊 Key Insights

* Customer demographics significantly influence purchasing decisions.
* Discounts increase purchase probability.
* Seasonal demand impacts product sales.
* Inventory level affects pricing strategies.
* Product ratings and customer reviews contribute to purchase likelihood.

---

## 💡 Future Enhancements

* Real-time dynamic pricing using live market data.
* Deep Learning-based prediction models.
* Integration with cloud databases.
* Interactive business dashboard.
* REST API for deployment.
* Automated price recommendation engine.

---

## 📷 Screenshots

Add screenshots of:

* Dataset Overview
* EDA Visualizations
* Model Comparison
* Streamlit Application
* Prediction Output

---

## 👨‍💻 Author

**Tejaswi Kolluri**

Machine Learning | Data Science | Python | AI Enthusiast

---

## 📜 License

This project is developed for educational and learning purposes.
