import pandas as pd
import matplotlib.pyplot as plt


# Load molecular descriptor results
df = pd.read_csv("results/molecular_descriptors.csv")


# 1. Molecular Weight Comparison
plt.figure(figsize=(10, 6))
plt.bar(df["Ligand"], df["Molecular Weight"])

plt.title("Molecular Weight Comparison")
plt.xlabel("Ligand")
plt.ylabel("Molecular Weight (Da)")
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig("results/molecular_weight_comparison.png", dpi=300)
plt.close()


# 2. LogP Comparison
plt.figure(figsize=(10, 6))
plt.bar(df["Ligand"], df["LogP"])

plt.title("LogP Comparison")
plt.xlabel("Ligand")
plt.ylabel("LogP")
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig("results/logp_comparison.png", dpi=300)
plt.close()


# 3. TPSA Comparison
plt.figure(figsize=(10, 6))
plt.bar(df["Ligand"], df["TPSA"])

plt.title("Topological Polar Surface Area")
plt.xlabel("Ligand")
plt.ylabel("TPSA (Å²)")
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig("results/tpsa_comparison.png", dpi=300)
plt.close()


print("All visualizations generated successfully.")