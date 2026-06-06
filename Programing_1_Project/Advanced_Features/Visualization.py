"""
Using Matplotlib and Seaborn this file will be used to visualize the data of the categories and expenses of 'expenses.txt'
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(file_path):
    df = pd.read_csv(file_path)
    colour = sns.color_palette("flare", as_cmap=True)
    sns.barplot(x="Category", y="Amount", data=df, color=colour(2.5))
    plt.title("Expense Distribution of all Categories")
    plt.xlabel("Category")
    plt.ylabel("Amount (in $)")
    plt.xticks(rotation=45)
    plt.yticks(rotation=45)
    plt.tight_layout()
    return plt.show()
