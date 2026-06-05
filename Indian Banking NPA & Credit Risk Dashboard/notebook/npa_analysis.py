import pandas as pd
import matplotlib.pyplot as plt

# Read cleaned Excel sheet
df = pd.read_excel(
    r"C:\BankingProject\Indian Banking NPA & Credit Risk Dashboard\data\clean_npa_data.xlsx",
    sheet_name="clean_data"
)


df = df.iloc[::-1].reset_index(drop=True)

# Print first rows
print(df.head())

# Plot Gross vs Net NPA
plt.figure(figsize=(10,5))

plt.plot(
    df["Year"],
    df["Gross_NPA_Percent"],
    marker='o',
    label="Gross NPA %"
)

plt.plot(
    df["Year"],
    df["Net_NPA_Percent"],
    marker='o',
    label="Net NPA %"
)

plt.xticks(rotation=45)

plt.title("Indian Banking NPA Trend")
plt.xlabel("Year")
plt.ylabel("NPA Percentage")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig(
    r"C:\BankingProject\Indian Banking NPA & Credit Risk Dashboard\images\npa_graph.png"
)
plt.show()

import numpy as np

# Calculate yearly change
df["Gross_NPA_Change"] = df["Gross_NPA_Percent"].diff()

print("\nYearly Gross NPA Change:\n")
print(df[["Year", "Gross_NPA_Change"]])

# -----------------------------
# ROLLING AVERAGE
# -----------------------------

df["Rolling_Avg_NPA"] = (
    df["Gross_NPA_Percent"]
    .rolling(window=3)
    .mean()
)

print("\nRolling Average NPA:\n")

print(df[[
    "Year",
    "Rolling_Avg_NPA"
]])

plt.figure(figsize=(10,5))

plt.bar(
    df["Year"],
    df["Gross_NPA_Percent"]
)

plt.xticks(rotation=45)

plt.title("Gross NPA Percentage by Year")

plt.xlabel("Year")

plt.ylabel("Gross NPA %")

plt.tight_layout()

plt.savefig(
    r"C:\BankingProject\Indian Banking NPA & Credit Risk Dashboard\images\gross_npa_bar.png"
)

plt.show()

# -----------------------------
# ROLLING AVERAGE GRAPH
# -----------------------------

plt.figure(figsize=(12,6))

plt.plot(
    df["Year"],
    df["Gross_NPA_Percent"],
    label="Actual Gross NPA",
    marker='o'
)

plt.plot(
    df["Year"],
    df["Rolling_Avg_NPA"],
    label="3-Year Rolling Average",
    linewidth=3
)

plt.xticks(rotation=45)

plt.title("Rolling Average of Gross NPA")

plt.xlabel("Year")

plt.ylabel("NPA Percentage")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig(
    r"C:\BankingProject\Indian Banking NPA & Credit Risk Dashboard\images\rolling_avg_npa.png"
)

plt.show()

# -----------------------------
# SUMMARY STATISTICS
# -----------------------------

print("\nSummary Statistics:\n")

print(df[[
    "Gross_NPA_Percent",
    "Net_NPA_Percent"
]].describe())

# -----------------------------
# WORST NPA YEAR
# -----------------------------

worst_year = df.loc[
    df["Gross_NPA_Percent"].idxmax()
]

print("\nWorst Banking Stress Year:\n")

print(worst_year)


print("\nKey Insights:\n")

print("1. Indian banking NPAs peaked around 1996-97.")
print("2. NPAs sharply declined during 2000-2008.")
print("3. Stress increased again after 2014.")
print("4. Recent years show improving asset quality.")
print("5. Rolling averages confirm long-term decline in NPAs.")
