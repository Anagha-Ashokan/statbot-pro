import pandas as pd
import matplotlib.pyplot as plt

def analyze_data(question):

    df = pd.read_csv("sales.csv")

    if "total revenue" in question.lower():

        total = df["revenue"].sum()
        return f"Total revenue is {total}"

    elif "graph" in question.lower():

        plt.plot(df["date"], df["revenue"])
        plt.title("Revenue Over Time")
        plt.xticks(rotation=45)

        plt.savefig("graph.png")
        plt.close()

        return "Graph saved as graph.png"

    else:
        return "I don't understand the question"