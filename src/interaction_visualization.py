import pandas as pd
import matplotlib.pyplot as plt


# Load protein-ligand interaction results
df = pd.read_csv("results/protein_ligand_interactions.csv")


# Select the 10 closest residues
top_interactions = df.head(10).copy()

# Create residue labels
top_interactions["Residue Label"] = (
    top_interactions["Chain"]
    + ":"
    + top_interactions["Residue"]
    + top_interactions["Residue Number"].astype(str)
)


# Create plot
plt.figure(figsize=(10, 6))

plt.barh(
    top_interactions["Residue Label"],
    top_interactions["Minimum Distance (Å)"]
)

plt.xlabel("Minimum Distance (Å)")
plt.ylabel("Protein Residue")
plt.title("Closest Protein Residues to Bound Ligand MK1")

plt.gca().invert_yaxis()

plt.tight_layout()

plt.savefig(
    "results/protein_ligand_distance_analysis.png",
    dpi=300
)

plt.close()

print("Protein-ligand interaction visualization generated successfully.")