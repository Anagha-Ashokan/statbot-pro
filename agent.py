import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales.csv")

def analyze_data(question):

    question = question.lower()

    # Count rows
    if "how many rows" in question:
        return len(df)

    # Mean revenue
    elif "mean revenue" in question or "average revenue" in question:
        return df["revenue"].mean()

    # Plot graph
    elif "plot sales" in question or "sales over time" in question:

        plt.figure()
        plt.plot(df["date"], df["revenue"])
        plt.xticks(rotation=45)

        plt.title("Sales Over Time")
        plt.xlabel("Date")
        plt.ylabel("Revenue")

        plt.savefig("sales_chart.png")

        return "Graph generated and saved as sales_chart.png"

    else:
        return "I don't understand the question"