# Holiday Season Shopper Behavior Analysis
# A full mini-project analyzing November & December online sessions
# Designed to demonstrate real business insight

# --- [1] Import Libraries ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# --- [2] Load Data ---
shopping_data = pd.read_csv("online_shopping_session_data.csv")

# --- [3] Filter for November & December Sessions ---
nov_dec_data = shopping_data[shopping_data["Month"].isin(["Nov", "Dec"])]

# --- [4] Purchase Rate Analysis by Customer Type ---
grouped = nov_dec_data.groupby("CustomerType")
total_sessions = grouped["SessionID"].count()
total_purchases = grouped["Purchase"].sum()
purchase_rate = total_purchases / total_sessions

# Format result
purchase_rates = {
    "Returning_Customer": round(purchase_rate.get("Returning_Customer", 0), 3),
    "New_Customer": round(purchase_rate.get("New_Customer", 0), 3)
}

print("\n Purchase Rates by Customer Type:")
print(purchase_rates)

# --- [5] Strongest Correlation Among Time-on-Page Types (Returning Customers Only) ---
returning_nov_dec = nov_dec_data[nov_dec_data["CustomerType"] == "Returning_Customer"]
duration_df = returning_nov_dec[[
    "Administrative_Duration",
    "Informational_Duration",
    "ProductRelated_Duration"
]]
corr_matrix = duration_df.corr()
corr_pairs = corr_matrix.unstack()
corr_pairs = corr_pairs[corr_pairs.index.get_level_values(0) != corr_pairs.index.get_level_values(1)]
top_pair = corr_pairs.abs().idxmax()
top_corr_value = corr_pairs[top_pair]

top_correlation = {
    "pair": top_pair,
    "correlation": round(top_corr_value, 3)
}

print("\n Top Correlation of Time Spent Between Page Types:")
print(top_correlation)

# --- [6] Binomial Modeling: Campaign Impact on Returning Customers ---
p_original = purchase_rates["Returning_Customer"]
p_boosted = p_original * 1.15
n_sessions = 500
threshold = 100
prob_at_least_100_sales = 1 - binom.cdf(threshold - 1, n_sessions, p_boosted)

print("\n Probability of at least 100 purchases (with 15% boost):")
print(round(prob_at_least_100_sales, 4))

# --- [7] Visualization of Binomial Distribution ---
x_vals = np.arange(0, 200)
y_vals = binom.pmf(x_vals, n_sessions, p_boosted)

plt.figure(figsize=(10, 5))
plt.bar(x_vals, y_vals, color='lightblue', edgecolor='white')
plt.axvline(x=threshold, color='red', linestyle='--', label=f"{threshold} Sales Threshold")
plt.title("Probability Distribution of Purchases (Boosted Rate)")
plt.xlabel("Number of Purchases")
plt.ylabel("Probability")
plt.legend()
plt.tight_layout()
plt.show()

# --- [8] Portfolio Summary Block ---
print("""
Summary:
- New customers converted more than returning ones (27.3% vs 19.6%)
- Strongest behavioral correlation: Admin ↔ Product pages (0.417)
- Campaign simulation shows 92%+ probability of hitting 100+ sales if purchase rate increases by 15%
Data-backed marketing insight, modeling, and storytelling in one tight package.
""")
