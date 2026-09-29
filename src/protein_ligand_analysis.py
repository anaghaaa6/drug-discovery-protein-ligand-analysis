from Bio.PDB import PDBParser
import pandas as pd
import numpy as np


# -------------------------------
# Load protein structure
# -------------------------------

pdb_file = "data/1HSG.pdb"

parser = PDBParser(QUIET=True)
structure = parser.get_structure("1HSG", pdb_file)


# -------------------------------
# Identify ligand
# -------------------------------

# MK1 is the bound ligand in this structure
ligand_name = "MK1"

ligand_atoms = []

for model in structure:
    for chain in model:
        for residue in chain:

            if residue.get_resname().strip() == ligand_name:

                for atom in residue:
                    ligand_atoms.append(atom)


if not ligand_atoms:
    print(f"Ligand {ligand_name} not found.")
    exit()


print(f"Ligand {ligand_name} found.")
print(f"Number of ligand atoms: {len(ligand_atoms)}")


# -------------------------------
# Find nearby residues
# -------------------------------

cutoff = 4.0

interactions = []

for model in structure:

    for chain in model:

        for residue in chain:

            # Ignore water and the ligand itself
            if residue.get_resname().strip() in ["HOH", ligand_name]:
                continue

            # Only standard amino-acid residues
            if residue.id[0] != " ":
                continue

            residue_name = residue.get_resname()
            residue_number = residue.id[1]

            minimum_distance = float("inf")

            for protein_atom in residue:

                for ligand_atom in ligand_atoms:

                    distance = np.linalg.norm(
                        protein_atom.coord - ligand_atom.coord
                    )

                    if distance < minimum_distance:
                        minimum_distance = distance

            if minimum_distance <= cutoff:

                interactions.append({
                    "Chain": chain.id,
                    "Residue": residue_name,
                    "Residue Number": residue_number,
                    "Minimum Distance (Å)": round(minimum_distance, 2)
                })


# -------------------------------
# Create results table
# -------------------------------

interaction_df = pd.DataFrame(interactions)

interaction_df = interaction_df.sort_values(
    by="Minimum Distance (Å)"
)


# -------------------------------
# Save results
# -------------------------------

output_file = "results/protein_ligand_interactions.csv"

interaction_df.to_csv(
    output_file,
    index=False
)


# -------------------------------
# Display results
# -------------------------------

print("\nProtein–Ligand Interaction Analysis")
print("==================================")

print(interaction_df.to_string(index=False))

print(
    f"\nNumber of nearby residues: "
    f"{len(interaction_df)}"
)

print(f"Results saved to: {output_file}")