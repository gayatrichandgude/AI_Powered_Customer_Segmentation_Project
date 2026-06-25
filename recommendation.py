import pandas as pd

# Load files
customers = pd.read_csv(
    "dataset/customer_segments.csv"
)

products = pd.read_csv(
    "dataset/products.csv"
)

def get_recommendations(segment):

    if segment == 0:
        return products[
            products["Price"] >= 10000
        ]["ProductName"].tolist()

    elif segment == 1:
        return products[
            (products["Price"] >= 3000) &
            (products["Price"] < 10000)
        ]["ProductName"].tolist()

    elif segment == 2:
        return products[
            products["Price"] < 3000
        ]["ProductName"].tolist()

    else:
        return products.sample(
            min(5, len(products))
        )["ProductName"].tolist()


print("\nCustomer Recommendations\n")

for index, row in customers.iterrows():

    recommendations = get_recommendations(
        row["Segment"]
    )

    print(
        f"Customer {row['CustomerID']} "
        f"(Segment {row['Segment']})"
    )

    print(recommendations)

    print("-" * 50)