from flask import Flask, render_template
import pandas as pd
import joblib
from flask import Flask, render_template, request, redirect
import sqlite3
import matplotlib
matplotlib.use('Agg')   
import matplotlib.pyplot as plt
import os
from flask import session, redirect, url_for
from flask import Flask


app = Flask(__name__)

df = pd.read_csv("dataset/customers.csv")

# ✅ ADD THIS LINE (IMPORTANT)
app.secret_key = "segment_ai_secret_key_123"

@app.route("/logout")
def logout():
    session.clear()   # user session remove karega
    return redirect(url_for("home"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/dashboard")
def dashboard():

    customers = pd.read_csv("dataset/customers.csv")
    products = pd.read_csv("dataset/products.csv")

    # Analytics
    total_customers = len(customers)
    total_products = len(products)
    avg_spending = round(customers["SpendingScore"].mean(), 2)

    # Segments
    customer_segments = 4

    # Chart
    plt.figure(figsize=(8,4))
    plt.hist(customers["SpendingScore"], bins=10)
    plt.title("Customer Spending Score Distribution")
    plt.xlabel("Spending Score")
    plt.ylabel("Customers")

    os.makedirs("static/charts", exist_ok=True)

    plt.savefig(
        "static/charts/customer_chart.png",
        bbox_inches="tight"
    )

    plt.close()

    # Table Data
    customer_data = customers.to_dict(orient="records")

    return render_template(
        "dashboard.html",
        total_customers=total_customers,
        total_products=total_products,
        avg_spending=avg_spending,
        customer_segments=customer_segments,
        customer_data=customer_data,
        chart_file="charts/customer_chart.png"
    )

@app.route("/upload", methods=["POST"])
def upload():

    import pandas as pd
    import os

    os.makedirs("dataset", exist_ok=True)

    customer_file = request.files.get("customer_file")
    product_file = request.files.get("product_file")

    # ------------------------
    # CUSTOMER FILE SAFE HANDLING
    # ------------------------
    if customer_file and customer_file.filename.endswith(".csv"):

        df = pd.read_csv(customer_file)

        # Clean column names
        df.columns = df.columns.str.strip()

        required_cols = [
            "CustomerID",
            "CustomerName",
            "Gender",
            "Age",
            "AnnualIncome",
            "SpendingScore",
            "Segment"
        ]

        # Validate structure
        if all(col in df.columns for col in required_cols):
            df.to_csv("dataset/customers.csv", index=False)
        else:
            return "❌ Invalid Customer CSV format"

    # ------------------------
    # PRODUCT FILE SAFE HANDLING
    # ------------------------
    if product_file and product_file.filename.endswith(".csv"):

        df2 = pd.read_csv(product_file)

        df2.columns = df2.columns.str.strip()

        required_product_cols = [
            "ProductID",
            "ProductName",
            "Category",
            "Price"
        ]

        if all(col in df2.columns for col in required_product_cols):
            df2.to_csv("dataset/products.csv", index=False)
        else:
            return "❌ Invalid Product CSV format"

    return redirect(url_for("dashboard"))
@app.route("/customers")
def customers():

    df = pd.read_csv("dataset/customers.csv")

    total_customers = len(df)

    male_count = len(
        df[df["Gender"]=="Male"]
    )

    female_count = len(
        df[df["Gender"]=="Female"]
    )

    avg_spending = round(
        df["SpendingScore"].mean(),2
    )

    customers_data = (
        df.to_dict(orient="records")
    )

    return render_template(
        "customers.html",
        total_customers=total_customers,
        male_count=male_count,
        female_count=female_count,
        avg_spending=avg_spending,
        customers=customers_data
    )
    
@app.route("/segments")
def segments():

    import pandas as pd
    import matplotlib.pyplot as plt
    import os

    # Load Dataset
    df = pd.read_csv("dataset/customers.csv")

    # Segment Counts
    segment0 = len(df[df["Segment"] == 0])
    segment1 = len(df[df["Segment"] == 1])
    segment2 = len(df[df["Segment"] == 2])
    segment3 = len(df[df["Segment"] == 3])

    # Create Chart
    plt.figure(figsize=(6,4))

    df["Segment"].value_counts().sort_index().plot(
        kind="bar"
    )

    plt.title("Customer Segments")
    plt.xlabel("Segment")
    plt.ylabel("Customers")

    os.makedirs("static/charts", exist_ok=True)

    plt.savefig(
        "static/charts/segment_chart.png",
        bbox_inches="tight"
    )

    plt.close()

    customers = df.to_dict(orient="records")

    return render_template(
        "segments.html",
        customers=customers,
        segment0=segment0,
        segment1=segment1,
        segment2=segment2,
        segment3=segment3,
        chart_file="charts/segment_chart.png"
    )
    
@app.route("/recommendations")
def recommendations():

    import pandas as pd
    from collections import Counter

    customers = pd.read_csv("dataset/customers.csv")
    products = pd.read_csv("dataset/products.csv")

    recommendations = []

    # -------------------------
    # Product Recommendation
    # -------------------------
    for _, customer in customers.iterrows():

        if customer["Segment"] == 3:
            product = products.iloc[0]

        elif customer["Segment"] == 2:
            product = products.iloc[1]

        elif customer["Segment"] == 1:
            product = products.iloc[2]

        else:
            product = products.iloc[3]

        recommendations.append({
            "CustomerID": customer["CustomerID"],
            "Segment": customer["Segment"],
            "ProductName": product["ProductName"],
            "Category": product["Category"],
            "Price": product["Price"]
        })

    # -------------------------
    # ✅ DEFINE ICONS HERE (FIX)
    # -------------------------
    category_icons = {
        "Electronics": "fa-tv",
        "Fashion": "fa-shirt",
        "Books": "fa-book",
        "Sports": "fa-futbol",
        "Beauty": "fa-spa",
        "Home Appliances": "fa-blender"
    }

    # -------------------------
    # Category Cards
    # -------------------------
    category_counts = Counter(products["Category"])

    category_cards = [
        {
            "category": cat,
            "count": count,
            "icon": category_icons.get(cat, "fa-tags")
        }
        for cat, count in category_counts.items()
    ]

    # -------------------------
    # Render Template
    # -------------------------
    return render_template(
        "recommendations.html",
        recommendations=recommendations,
        category_cards=category_cards,
        total_customers=len(customers),
        total_products=len(products),
        total_recommendations=len(recommendations)
    )

@app.route("/analytics")
def analytics():

    import pandas as pd
    import matplotlib.pyplot as plt
    import os

    df = pd.read_csv("dataset/customers.csv")

    os.makedirs("static/charts", exist_ok=True)

    # Chart 1

    plt.figure(figsize=(7,4))

    plt.hist(
        df["SpendingScore"],
        bins=10
    )

    plt.title(
        "Spending Score Distribution"
    )

    plt.savefig(
        "static/charts/spending_chart.png",
        bbox_inches="tight"
    )

    plt.close()

    # Chart 2

    plt.figure(figsize=(6,4))

    df["Segment"].value_counts().sort_index().plot(
        kind="bar"
    )

    plt.title(
        "Customer Segments"
    )

    plt.savefig(
        "static/charts/segment_distribution.png",
        bbox_inches="tight"
    )

    plt.close()

    return render_template(
        "analytics.html",
        total_customers=len(df),
        avg_income=round(df["AnnualIncome"].mean()),
        avg_spending=round(df["SpendingScore"].mean()),
        chart1="charts/spending_chart.png",
        chart2="charts/segment_chart.png"
    )
    

   
@app.route("/reports")
def reports():

    import pandas as pd

    # ----------------------
    # Load Data
    # ----------------------
    customers = pd.read_csv("dataset/customers.csv")
    products = pd.read_csv("dataset/products.csv")

    # ----------------------
    # Basic KPIs
    # ----------------------
    total_customers = len(customers)
    total_products = len(products)

    avg_price = round(products["Price"].mean(), 2)

    # Top segment
    top_segment = customers["Segment"].value_counts().idxmax()

    # ----------------------
    # Category Insights
    # ----------------------
    category_counts = products["Category"].value_counts().to_dict()

    # ----------------------
    # Segment Insights
    # ----------------------
    segment_counts = customers["Segment"].value_counts().to_dict()

    # ----------------------
    # AI Simple Insights (rule-based)
    # ----------------------
    top_category = max(category_counts, key=category_counts.get)

    insight_text = f"""
    Electronics and Fashion are most active categories.
    Segment {top_segment} has highest customer base.
    {top_category} is the most popular category.
    """

    # ----------------------
    # Render Template
    # ----------------------
    return render_template(
        "reports.html",
        total_customers=total_customers,
        total_products=total_products,
        avg_price=avg_price,
        top_segment=top_segment,
        category_counts=category_counts,
        segment_counts=segment_counts,
        top_category=top_category,
        insight_text=insight_text
    )




if __name__ == "__main__":
    app.run(debug=True)