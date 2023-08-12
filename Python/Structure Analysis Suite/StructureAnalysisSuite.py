#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 12:18:42 2023

@author: z548m774
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLineEdit, QLabel, QTextEdit, QHBoxLayout
from Bio.PDB import PDBParser
import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QSizePolicy

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

def read_and_process_sasa(file_path):
    groups = []
    current_group = []
    prev_residue_number = -1
    current_chain = "A"

    with open(file_path, 'r') as file:
        lines = file.readlines()[1:]  # Skip the header line

        for line in lines:
            parts = line.split()
            if len(parts) < 3:  # Skip empty or incomplete lines
                continue

            try:
                residue_number = int(parts[1])
                value = float(parts[2])
            except ValueError:  # Skip lines with unexpected data
                continue

            if residue_number <= prev_residue_number:
                if current_group:
                    groups.append((current_group, current_chain))
                    current_group = []
                current_chain = chr(ord(current_chain) + 1)

            if value < 0.5:
                if current_group:
                    groups.append((current_group, current_chain))
                    current_group = []
            else:
                current_group.append(residue_number)

            prev_residue_number = residue_number

        if current_group:  # Add the last group, if not empty
            groups.append((current_group, current_chain))

    return groups

def format_groups(groups):
    formatted_groups = []
    for group, chain in groups:
        if len(group) > 1:
            formatted_groups.append(f"{group[0]}-{group[-1]} {chain}")
    return formatted_groups

def write_to_file(filename, formatted_groups):
    with open(filename, 'w') as file:
        for group in formatted_groups:
            file.write(group + "\n")

def script1():
    file_path, _ = QFileDialog.getOpenFileName()  # Show an open file dialog
    if not file_path:
        print("No file selected!")
        return

    output_file = f"residues_{file_path.split('/')[-1]}.txt"
    groups = read_and_process_sasa(file_path)
    formatted_groups = format_groups(groups)
    write_to_file(output_file, formatted_groups)
    print(f"Residue groups with values greater than or equal to 0.5 in column 3 have been written to {output_file}")

def read_pdb_and_extract_ranges(pdb_file):
    ranges = []

    with open(pdb_file, 'r') as file:
        for line in file:
            if line.startswith("HELIX") or line.startswith("SHEET"):
                chain_letter = line[21]  # Extract the chain letter from position 22 (after the first 3-letter amino acid code)
                if not chain_letter.isalpha():  # Check if chain_letter is not a valid alphabetic character
                    chain_letter = line[19]  # Use the chain letter from position 20 instead
                start_value = int(line[23:27].strip())  # Updated start_value position
                end_value = int(line[34:38].strip())
                range_type = line[:6].strip()
                ranges.append((chain_letter, start_value, end_value, range_type))

    return ranges

def write_ranges_to_file(ranges, output_file):
    with open(output_file, 'w') as file:
        for chain_letter, start_value, end_value, range_type in ranges:
            file.write(f"{chain_letter} {start_value}-{end_value} {range_type}\n")

def script2():
    pdb_file, _ = QFileDialog.getOpenFileName()  # Show an open file dialog
    if not pdb_file:
        print("No file selected!")
        return

    output_file = "Secondary_Structure.txt"
    ranges = read_pdb_and_extract_ranges(pdb_file)
    ranges.sort(key=lambda x: (x[0], x[1]))  # Sort ranges first by chain_letter, then by start_value
    write_ranges_to_file(ranges, output_file)

class PDBWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)
        
        left_layout = QVBoxLayout()
        main_layout.addLayout(left_layout)
        
        title = QLabel('Detailed Residue Analysis')
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        left_layout.addWidget(title)
        
        subtitle = QLabel('Detailed Properties for a series of residues')
        subtitle.setStyleSheet("font-size: 12px; font-style: italic")
        left_layout.addWidget(subtitle)

        self.pdb_id_input = QLineEdit()
        self.pdb_id_input.setToolTip('Enter the ID of the Protein Data Bank (PDB) entry you want to analyze')
        self.chain_id_input = QLineEdit()
        self.chain_id_input.setToolTip('Enter the ID of the chain in the PDB entry you want to analyze')
        self.residues_input = QLineEdit()
        self.residues_input.setToolTip('Enter the number(s) of the residue(s) you want to analyze, separated by commas')

        left_layout.addWidget(QLabel('PDB ID:'))
        left_layout.addWidget(self.pdb_id_input)
        left_layout.addWidget(QLabel('Chain ID:'))
        left_layout.addWidget(self.chain_id_input)
        left_layout.addWidget(QLabel('Residue number(s):'))
        left_layout.addWidget(self.residues_input)
        left_layout.addWidget(QPushButton('Analyze', clicked=self.analyze))
        
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        main_layout.addWidget(QLabel('Output:'))
        main_layout.addWidget(self.output)
        
        write_button = QPushButton('Write to file')
        write_button.clicked.connect(self.write_to_file)
        left_layout.addWidget(write_button)

        clear_button = QPushButton('Clear')
        clear_button.clicked.connect(self.clear)
        left_layout.addWidget(clear_button)

    def analyze(self):
        # Get input values
        pdb_id = self.pdb_id_input.text()
        chain_id = self.chain_id_input.text()
        residues = self.residues_input.text()

        # Download PDB file
        url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
        r = requests.get(url)
        open(f"{pdb_id}.pdb", 'w').write(r.text)

        # Parse PDB file
        parser = PDBParser(QUIET=True)
        structure = parser.get_structure(pdb_id, f"{pdb_id}.pdb")

        # Split user input and handle ranges
        residue_list = []
        for part in residues.split(','):
            if '-' in part:
                start, end = map(int, part.split('-'))
                residue_list.extend(range(start, end + 1))
            else:
                residue_list.append(int(part))
        
        
        # Get residues
        total_charge = 0
        hydrophobic_residues = 0
        hbond_residues = 0
        for residue in residue_list:
            res = structure[0][chain_id][residue]
            res_name = res.get_resname()
            properties = AA_PROPERTIES.get(res_name)
            if properties:
                self.output.append(f"Residue {residue}: {properties['full_name']} ({res_name}), "
                                  f"Charge: {properties['charge']}, "
                                  f"{'hydrophobic' if properties['hydrophobic'] else 'Hydrophilic'}, "
                                  f"{'Can form H-bonds' if properties['hydrogen_bond'] else 'Cannot form H-bonds'}")
                total_charge += properties['charge']
                if properties['hydrophobic']:
                    hydrophobic_residues += 1
                if properties['hydrogen_bond']:
                    hbond_residues += 1
            else:
                self.output.append(f"Unknown residue: {residue} ({res_name})")
                
        total_residues = len(residue_list)
        self.output.append(f"\nTotal Charge: {total_charge}")
        self.output.append(f"% Hydrophobic Residues: {hydrophobic_residues / total_residues * 100}%")
        self.output.append(f"% of Residues that can form H-Bonds: {hbond_residues / total_residues * 100}%")
        
    def write_to_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save File")
        if filename:
            with open(filename, 'w') as file:
                file.write(self.output.toPlainText())

    def clear(self):
        self.output.clear()

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Load the image
        pixmap = QPixmap('Analysis.png')  # replace with your image path
        pixmap = pixmap.scaled(525, 175)  # replace with desired width and height

        # Create the label and set the pixmap
        image_label = QLabel()
        image_label.setPixmap(pixmap)
        image_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Create the horizontal layout and add the image label in the center
        top_layout = QHBoxLayout()
        top_layout.addWidget(image_label)
        layout.addLayout(top_layout)

        # Title for script1
        title1 = QLabel('SASA Analysis')
        title1.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title1)
        
        # Subtitle for script1
        subtitle1 = QLabel('This script processes SASA data and identifies residues')
        subtitle1.setStyleSheet("font-size: 12px; font-style: italic")
        layout.addWidget(subtitle1)
        layout.addWidget(QPushButton('Run SASA Analysis', clicked=script1))

        # Title for script2
        title2 = QLabel('Secondary Structure Analysis')
        title2.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title2)
        
        # Subtitle for script2
        subtitle2 = QLabel('This script extracts and displays range of PDB data')
        subtitle2.setStyleSheet("font-size: 12px; font-style: italic")
        layout.addWidget(subtitle2)
        layout.addWidget(QPushButton('Run Secondary Structure Analysis', clicked=script2))


        layout.addWidget(PDBWidget())

def main():
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.resize(1200, 700) # width and height of window
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
