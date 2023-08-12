#!/usr/bin/env python
# coding: utf-8

# In[8]:


import sys
import os
from Bio.PDB import PDBParser
import requests

# Define properties for the 20 common amino acids
AA_PROPERTIES = {
    'ALA': {'full_name': 'Alanine', 'charge': 0, 'hydrophobic': True, 'hydrogen_bond': False},
    'CYS': {'full_name': 'Cysteine', 'charge': 0, 'hydrophobic': True, 'hydrogen_bond': True},
    'ASP': {'full_name': 'Aspartic Acid', 'charge': -1, 'hydrophobic': False, 'hydrogen_bond': True},
    'GLU': {'full_name': 'Glutamic Acid', 'charge': -1, 'hydrophobic': False, 'hydrogen_bond': True},
    'PHE': {'full_name': 'Phenylalanine', 'charge': 0, 'hydrophobic': True, 'hydrogen_bond': False},
    'GLY': {'full_name': 'Glycine', 'charge': 0, 'hydrophobic': False, 'hydrogen_bond': False},
    'HIS': {'full_name': 'Histidine', 'charge': 0, 'hydrophobic': False, 'hydrogen_bond': True},
    'ILE': {'full_name': 'Isoleucine', 'charge': 0, 'hydrophobic': True, 'hydrogen_bond': False},
    'LYS': {'full_name': 'Lysine', 'charge': 1, 'hydrophobic': False, 'hydrogen_bond': True},
    'LEU': {'full_name': 'Leucine', 'charge': 0, 'hydrophobic': True, 'hydrogen_bond': False},
    'MET': {'full_name': 'Methionine', 'charge': 0, 'hydrophobic': True, 'hydrogen_bond': False},
    'ASN': {'full_name': 'Asparagine', 'charge': 0, 'hydrophobic': False, 'hydrogen_bond': True},
    'PRO': {'full_name': 'Proline', 'charge': 0, 'hydrophobic': True, 'hydrogen_bond': False},
    'GLN': {'full_name': 'Glutamine', 'charge': 0, 'hydrophobic': False, 'hydrogen_bond': True},
    'ARG': {'full_name': 'Arginine', 'charge': 1, 'hydrophobic': False, 'hydrogen_bond': True},
    'SER': {'full_name': 'Serine', 'charge': 0, 'hydrophobic': False, 'hydrogen_bond': True},
    'THR': {'full_name': 'Threonine', 'charge': 0, 'hydrophobic': False, 'hydrogen_bond': True},
    'VAL': {'full_name': 'Valine', 'charge': 0, 'hydrophobic': True, 'hydrogen_bond': False},
    'TRP': {'full_name': 'Tryptophan', 'charge': 0, 'hydrophobic': True, 'hydrogen_bond': True},
    'TYR': {'full_name': 'Tyrosine', 'charge': 0, 'hydrophobic': False, 'hydrogen_bond': True},
}


def download_pdb_file(pdb_id):
    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise ValueError(f"Failed to download PDB file: {response.status_code}")


def parse_pdb_file(pdb_id, pdb_text):
    with open(f"{pdb_id}.pdb", "w") as pdb_file:
        pdb_file.write(pdb_text)
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure(pdb_id, f"{pdb_id}.pdb")
    os.remove(f"{pdb_id}.pdb")  # Clean up the temporary file
    return structure


def analyze_residues(pdb_id, chain_id, residue_list):
    pdb_text = download_pdb_file(pdb_id)
    structure = parse_pdb_file(pdb_id, pdb_text)

    results = []  # Store the results

    total_charge = 0
    hydrophilic_residues = 0
    hbond_residues = 0
    for residue_range in residue_list:
        start, end = map(int, residue_range.split('-'))
        for residue in range(start, end + 1):
            try:
                res = structure[0][chain_id][residue]
                res_name = res.get_resname()
                properties = AA_PROPERTIES.get(res_name)
                if properties:
                    results.append(f"Residue {residue}: {properties['full_name']} ({res_name}), "
                                  f"Charge: {properties['charge']}, "
                                  f"{'Hydrophobic' if properties['hydrophobic'] else 'Hydrophilic'}, "
                                  f"{'Can form H-bonds' if properties['hydrogen_bond'] else 'Cannot form H-bonds'}")
                    total_charge += properties['charge']
                    if not properties['hydrophobic']:
                        hydrophilic_residues += 1
                    if properties['hydrogen_bond']:
                        hbond_residues += 1
            except KeyError:
                results.append(f"Unknown residue: {residue} ({res_name})")

    total_residues = sum(end - start + 1 for residue_range in residue_list)
    results.append(f"\nTotal Charge: {total_charge}")
    results.append(f"% Hydrophilic Residues: {hydrophilic_residues / total_residues * 100}%")
    results.append(f"% of Residues that can form H-Bonds: {hbond_residues / total_residues * 100}%")

    return results


def main():
    pdb_id = "1B0G"
    chain_id = "A"
    residue_input = os.path.basename(os.getcwd())  # The residue range is the name of the current directory
    residue_list = residue_input.split(',')  # Handle multiple residue ranges

    results = analyze_residues(pdb_id, chain_id, residue_list)

    # Write the results to a file in the current working directory
    file_path = os.path.join(os.getcwd(), "Residue_Info.txt")
    try:
        with open(file_path, "w") as f:
            for result in results:
                f.write(result + "\n")
        print("Results written to 'Residue_Info.txt'")
    except OSError as e:
        print(f"Error occurred while writing the file: {e}")


if __name__ == '__main__':
    main()


# In[ ]:




