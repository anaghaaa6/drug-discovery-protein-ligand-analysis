import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski


# Load ligand dataset
input_file = "data/ligands.csv"
df = pd.read_csv(input_file)

results = []

for _, row in df.iterrows():

    ligand_name = row["Ligand"]
    smiles = row["SMILES"]

    molecule = Chem.MolFromSmiles(smiles)

    if molecule is None:
        print(f"Invalid SMILES for {ligand_name}")
        continue

    # Molecular descriptors
    molecular_weight = Descriptors.MolWt(molecule)
    logp = Descriptors.MolLogP(molecule)
    hbd = Lipinski.NumHDonors(molecule)
    hba = Lipinski.NumHAcceptors(molecule)
    rotatable_bonds = Lipinski.NumRotatableBonds(molecule)
    tpsa = Descriptors.TPSA(molecule)

    # Lipinski Rule of Five violations
    violations = 0

    if molecular_weight > 500:
        violations += 1

    if logp > 5:
        violations += 1

    if hbd > 5:
        violations += 1

    if hba > 10:
        violations += 1

    rule_of_five = "Pass" if violations == 0 else "Violation"

    results.append({
        "Ligand": ligand_name,
        "Molecular Weight": round(molecular_weight, 2),
        "LogP": round(logp, 2),
        "H-Bond Donors": hbd,
        "H-Bond Acceptors": hba,
        "Rotatable Bonds": rotatable_bonds,
        "TPSA": round(tpsa, 2),
        "Lipinski Violations": violations,
        "Lipinski Status": rule_of_five
    })


# Create results dataframe
results_df = pd.DataFrame(results)

# Save results
output_file = "results/molecular_descriptors.csv"
results_df.to_csv(output_file, index=False)

# Display results
print("\nDrug-Likeness Analysis")
print("======================")
print(results_df.to_string(index=False))

print(f"\nResults saved to: {output_file}")