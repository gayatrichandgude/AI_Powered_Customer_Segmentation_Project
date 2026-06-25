# 🧠 AI Customer Segmentation & Recommendation System

A Machine Learning based Customer Segmentation System that groups customers into meaningful clusters using K-Means Clustering and provides AI-based product recommendations through a Flask web application.

# 📌 Project Overview

This project uses Machine Learning (K-Means Algorithm) to analyze customer behavior based on:
```text
Age
Annual Income
Spending Score
```
The system segments customers into different groups and provides personalized product recommendations, along with an interactive Flask dashboard for visualization and insights.

# 🎯 Objectives
```text
Build a Machine Learning model for customer segmentation
Group customers into meaningful clusters using K-Means
Provide AI-based product recommendations
Visualize customer behavior using charts
Develop a Flask-based web application
Enable dataset upload and dynamic analysis
Generate business insights for decision making
```
# 🚀 Features
```text
👥 Customer Management Dashboard
📊 AI Customer Segmentation (K-Means Clustering)
🎯 Personalized Product Recommendations
📈 Interactive Analytics Charts
📑 Business Reports & Insights
📤 CSV Dataset Upload System
🔍 Customer Search Functionality
📊 Segment-wise Visualization
🧠 AI-based Rule Engine for Recommendations
```
# 🛠 Technologies Used
```text
Python
Flask
Pandas
NumPy
Scikit-Learn
Matplotlib
Seaborn
Joblib
HTML5
CSS3
Bootstrap 5
```
# 📂 Project Structure

```text
AI_Powered_Customer_Segmentation_Project/

├── app.py
├── train_model.py
├── requirements.txt
│
├── dataset/
│   ├── customers.csv
│   ├── products.csv
│   ├── customer_segments.csv
│
├── model/
│   ├── kmeans_model.pkl
│   ├── scaler.pkl
│
├── static/
│   ├── css/
│   ├── charts/
│
├── templates/
│   ├── home.html
│   ├── dashboard.html
│   ├── customers.html
│   ├── segments.html
│   ├── recommendations.html
│   ├── analytics.html
│   ├── reports.html
│
└── README.md
```
# 📊 Dataset Description

The dataset contains customer behavior data.

# Customer Dataset:
```text
CustomerID
CustomerName
Gender
Age
AnnualIncome
SpendingScore
Segment 
```
# Product Dataset:
```text
ProductID
ProductName
Category
Price
```
# 🔄 Data Preprocessing
```text
Handling missing values
Feature selection
Standardization using StandardScaler
Data normalization
Label assignment using K-Means
```
# 🧠 Machine Learning Model
# Algorithm Used:
👉 K-Means Clustering

# Features Used:
Age
Annual Income
Spending Score

# Number of Clusters:
👉 4 Customer Segments (0, 1, 2, 3)

# Output:
Customer Segment Label

# 📈 System Modules

# 👥 1. Customer Module
View all customers
Gender & spending analysis
Search customers

# 📊 2. Segmentation Module
Cluster visualization
Segment-wise breakdown

# 🎯 3. Recommendation Module
Product recommendation based on segment
Category-based mapping

# 📈 4. Analytics Module
Spending distribution graph
Segment distribution graph

# 📑 5. Reports Module
Total customers/products
Top segment analysis
AI insights summary

# ⚙ Installation

# Clone Repository
git clone https://github.com/gayatrichandgude/AI_Powered_Customer_Segmentation_Project.git

cd AI_Powered_Customer_Segmentation_Project

# Create Virtual Environment
python -m venv venv

# Activate Environment
venv\Scripts\activate

# Install Dependencies
pip install -r requirements.txt

# Run Project
Train Model
python train_model.py

# Run Flask App
python app.py

# Open Browser
http://127.0.0.1:5000

# 📊 Key Insights
```text
Customers are divided into 4 behavior-based clusters
High-income users receive premium recommendations
Low-income users receive budget-friendly suggestions
Helps businesses improve targeted marketing
Improves customer understanding using AI
```

# 🔮 Future Improvements
```text
AI-based recommendation engine (collaborative filtering)
Real-time model training
User login & authentication system
Cloud database integration
Deployment on AWS / Render / Azure
Mobile application version
```

# 👩‍💻 Author

Gayatri Chandgude

GitHub:
https://github.com/gayatrichandgude

# 📜 License

This project is for educational purposes only.
