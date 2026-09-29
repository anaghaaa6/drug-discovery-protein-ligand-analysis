import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw


# Load ligand dataset
df = pd.read_csv("data/ligands.csv")

molecules = []
legends = []

for _, row in df.iterrows():

    molecule = Chem.MolFromSmiles(row["SMILES"])

    if molecule is not None:
        molecules.append(molecule)
        legends.append(row["Ligand"])


# Generate molecular structure image
image = Draw.MolsToGridImage(
    molecules,
    molsPerRow=3,
    subImgSize=(300, 300),
    legends=legends
)

# Save image
image.save("results/ligand_structures.png")

print("Ligand structure visualization generated successfully.")