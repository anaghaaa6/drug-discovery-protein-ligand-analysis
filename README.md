# Drug Discovery: Protein–Ligand Analysis & Visualization Using Python

## Overview

This project presents a computational workflow for analyzing small-molecule ligands and studying protein–ligand structural relationships using Python.

The project combines cheminformatics, molecular descriptor analysis, Lipinski drug-likeness evaluation, molecular visualization, and protein–ligand proximity analysis.

## Objectives

- Calculate molecular descriptors using RDKit
- Evaluate ligands using Lipinski's Rule of Five
- Visualize molecular structures
- Compare physicochemical properties of ligands
- Analyze an experimentally determined protein–ligand complex
- Identify protein residues located near a bound ligand
- Generate visualizations of computational results

## Technologies Used

- Python
- RDKit
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Biopython
- Jupyter Notebook

## Project Structure

```text
drug-discovery-protein-ligand-analysis/
│
├── data/
│   ├── ligands.csv
│   └── 1HSG.pdb
│
├── src/
│   ├── molecular_analysis.py
│   ├── visualization.py
│   ├── molecule_visualization.py
│   ├── protein_ligand_analysis.py
│   └── interaction_visualization.py
│
├── results/
│   ├── molecular_descriptors.csv
│   ├── molecular_weight_comparison.png
│   ├── logp_comparison.png
│   ├── tpsa_comparison.png
│   ├── ligand_structures.png
│   ├── protein_ligand_interactions.csv
│   └── protein_ligand_distance_analysis.png
│
├── notebooks/
├── README.md
├── requirements.txt
└── .gitignore
Workflow
Ligand SMILES
      ↓
RDKit Molecular Analysis
      ↓
Molecular Descriptors
      ↓
Lipinski Rule of Five
      ↓
Molecular Visualization
      ↓
Protein–Ligand Structure
      ↓
Residue Proximity Analysis
      ↓
Results & Visualization
Molecular Analysis

The project calculates:

Molecular Weight
LogP
Hydrogen Bond Donors
Hydrogen Bond Acceptors
Rotatable Bonds
Topological Polar Surface Area (TPSA)

The current ligand dataset contains:

Caffeine
Aspirin
Ibuprofen
Paracetamol
Naproxen
Lipinski Rule of Five

Each ligand is evaluated using four commonly used criteria:

Molecular weight ≤ 500 Da
LogP ≤ 5
Hydrogen bond donors ≤ 5
Hydrogen bond acceptors ≤ 10

The project reports the number of Lipinski violations for each ligand.

Protein–Ligand Analysis

The project uses the experimentally determined protein–ligand structure 1HSG from the Protein Data Bank.

The analysis identifies protein residues within a 4 Å proximity cutoff of the bound ligand MK1 and calculates the minimum distance between each nearby residue and the ligand.

The analysis identified 26 nearby protein residues using this cutoff.

Results

The project generates:

Molecular descriptor CSV
Molecular weight comparison
LogP comparison
TPSA comparison
Ligand structure visualization
Lipinski drug-likeness results
Protein–ligand interaction CSV
Protein–ligand distance visualization
Important Note

The protein–ligand analysis is a structural proximity analysis, not a molecular docking calculation.

A residue being located within 4 Å of the ligand does not by itself establish a specific interaction such as a hydrogen bond or salt bridge.

Lipinski Rule of Five is a drug-likeness guideline and does not establish biological activity, efficacy, or clinical suitability.

How to Run
1. Create a virtual environment
python -m venv venv
2. Activate the environment

Windows:

venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Run molecular analysis
python src\molecular_analysis.py
5. Generate molecular property visualizations
python src\visualization.py
6. Generate ligand structure visualization
python src\molecule_visualization.py
7. Run protein–ligand analysis
python src\protein_ligand_analysis.py
8. Generate interaction visualization
python src\interaction_visualization.py
Author

Anagha S

B.Tech Bioinformatics
Amity University Rajasthan


After pasting, press **Ctrl + S**.

Then tell me **“done”**. We'll move to the final GitHub setup. 🚀
Author

Anagha S

B.Tech Bioinformatics
Amity University Rajasthan shuid i paste these aii

Yes, exactly. 👍 Paste that Author section too.

At the very bottom of your README.md, put:

## Author

**Anagha S**

B.Tech Bioinformatics  
Amity University Rajasthan

The ## Author is a heading, and your name and degree appear underneath it.

Then press Ctrl + S. ✅

You don't need to add your phone number, email, or personal details.

Once saved, tell me done and we'll move to the GitHub part. 🚀

give ready t0 c0py c0de 

Yes. Copy everything below into your README.md:

# Drug Discovery: Protein–Ligand Analysis & Visualization Using Python

## Overview

This project presents a computational workflow for analyzing small-molecule ligands and studying protein–ligand structural relationships using Python.

The project combines cheminformatics, molecular descriptor analysis, Lipinski drug-likeness evaluation, molecular visualization, and protein–ligand proximity analysis.

## Objectives

- Calculate molecular descriptors using RDKit
- Evaluate ligands using Lipinski's Rule of Five
- Visualize molecular structures
- Compare physicochemical properties of ligands
- Analyze an experimentally determined protein–ligand complex
- Identify protein residues located near a bound ligand
- Generate visualizations of computational results

## Technologies Used

- Python
- RDKit
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Biopython
- Jupyter Notebook

## Project Structure

```text
drug-discovery-protein-ligand-analysis/
│
├── data/
│   ├── ligands.csv
│   └── 1HSG.pdb
│
├── src/
│   ├── molecular_analysis.py
│   ├── visualization.py
│   ├── molecule_visualization.py
│   ├── protein_ligand_analysis.py
│   └── interaction_visualization.py
│
├── results/
│   ├── molecular_descriptors.csv
│   ├── molecular_weight_comparison.png
│   ├── logp_comparison.png
│   ├── tpsa_comparison.png
│   ├── ligand_structures.png
│   ├── protein_ligand_interactions.csv
│   └── protein_ligand_distance_analysis.png
│
├── notebooks/
├── README.md
├── requirements.txt
└── .gitignore
Workflow
Ligand SMILES
      ↓
RDKit Molecular Analysis
      ↓
Molecular Descriptors
      ↓
Lipinski Rule of Five
      ↓
Molecular Visualization
      ↓
Protein–Ligand Structure
      ↓
Residue Proximity Analysis
      ↓
Results & Visualization
Molecular Analysis

The project calculates:

Molecular Weight
LogP
Hydrogen Bond Donors
Hydrogen Bond Acceptors
Rotatable Bonds
Topological Polar Surface Area (TPSA)

The current ligand dataset contains:

Caffeine
Aspirin
Ibuprofen
Paracetamol
Naproxen
Lipinski Rule of Five

Each ligand is evaluated using four commonly used criteria:

Molecular weight ≤ 500 Da
LogP ≤ 5
Hydrogen bond donors ≤ 5
Hydrogen bond acceptors ≤ 10

The project reports the number of Lipinski violations for each ligand.

Protein–Ligand Analysis

The project uses the experimentally determined protein–ligand structure 1HSG from the Protein Data Bank.

The analysis identifies protein residues within a 4 Å proximity cutoff of the bound ligand MK1 and calculates the minimum distance between each nearby residue and the ligand.

The analysis identified 26 nearby protein residues using this cutoff.

Results

The project generates:

Molecular descriptor CSV
Molecular weight comparison
LogP comparison
TPSA comparison
Ligand structure visualization
Lipinski drug-likeness results
Protein–ligand interaction CSV
Protein–ligand distance visualization
Important Note

The protein–ligand analysis is a structural proximity analysis, not a molecular docking calculation.

A residue being located within 4 Å of the ligand does not by itself establish a specific interaction such as a hydrogen bond or salt bridge.

Lipinski Rule of Five is a drug-likeness guideline and does not establish biological activity, efficacy, or clinical suitability.

How to Run
1. Create a virtual environment
python -m venv venv
2. Activate the environment

Windows:

venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Run molecular analysis
python src\molecular_analysis.py
5. Generate molecular property visualizations
python src\visualization.py
6. Generate ligand structure visualization
python src\molecule_visualization.py
7. Run protein–ligand analysis
python src\protein_ligand_analysis.py
8. Generate interaction visualization
python src\interaction_visualization.py
Author

Anagha S

B.Tech Bioinformatics
Amity University Rajasthan