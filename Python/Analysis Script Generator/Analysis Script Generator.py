#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 13:21:33 2023

@author: z548m774
"""

import os
import re
import shutil
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QLineEdit

class FileProcessor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BashScriptEditor")
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Add QLabel for the image
        image_label = QLabel()
        pixmap = QPixmap("script_generator3.png")  # Replace with the actual path to your image

        desired_width = 900
        desired_height = 350

        # Calculate the scaled size while maintaining aspect ratio
        aspect_ratio = pixmap.width() / pixmap.height()
        if aspect_ratio > desired_width / desired_height:
            scaled_width = desired_width
            scaled_height = int(scaled_width / aspect_ratio)
        else:
            scaled_height = desired_height
            scaled_width = int(scaled_height * aspect_ratio)

        pixmap = pixmap.scaled(scaled_width, scaled_height, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(image_label)


        # XTC File Input
        layout.addWidget(QLabel('Please enter the name of the xtc file including .xtc suffix:'))
        self.xtc_file_name = QLineEdit()
        layout.addWidget(self.xtc_file_name)

        # GRO File Input
        layout.addWidget(QLabel('Please enter the name of the gro file including .gro suffix:'))
        self.gro_file_name = QLineEdit()
        layout.addWidget(self.gro_file_name)

        # TPR File Input
        layout.addWidget(QLabel('Please enter the name of the tpr file including .tpr suffix:'))
        self.tpr_file_name = QLineEdit()
        layout.addWidget(self.tpr_file_name)

        # Residues to Analyze Input
        layout.addWidget(QLabel('Residues to analyse:'))
        self.residues_to_analyze = QLineEdit()
        layout.addWidget(self.residues_to_analyze)
        layout.addWidget(QPushButton('Browse', clicked=self.browse_residues_file))

        # Process Files Button
        layout.addWidget(QPushButton('Process Files', clicked=self.process_files))

        # Adjust the window size
        self.resize(800, 400)  # Adjust the width and height as per your requirements
        
    def process_files(self):
        # Process the files here
        file_list = ["template_dipole.sh",
                     "template_hbonding.sh",
                     "template_index.sh",
                     "template_index_solvation_shell_rdf.sh",
                     "template_make_index.sh", 
                     "template_msd.sh", 
                     "template_rdf.sh", 
                     "template_solvation_shell_COM.sh", 
                     "template_index_solvation_shell.sh"]

        for filename in file_list:
            if filename in [self.xtc_file_name.text(), self.gro_file_name.text(), self.tpr_file_name.text()]:
                continue

            with open(filename, 'r') as file:
                filedata = file.read()

            filedata = filedata.replace('xtcfile', self.xtc_file_name.text())
            filedata = filedata.replace('grofile', self.gro_file_name.text())
            filedata = filedata.replace('tprfile', self.tpr_file_name.text())

            with open('updated_' + filename, 'w') as file:
                file.write(filedata)

        def process_template_file(template_filename, output_filename, residues):
            with open(template_filename, "r") as template_file:
                lines = template_file.readlines()
                shebang = lines.pop(0)
                template_content = "".join(lines)

            with open(output_filename, "w") as output_file:
                output_file.write(shebang)
                for residue in residues:
                    residue = residue.strip()
                    new_content = template_content.replace("resi", residue)
                    output_file.write(new_content)
                    output_file.write("\n\n")

        with open(self.residues_to_analyze.text(), "r") as residues_file:
            residues = residues_file.readlines()

        files = [
            ("template_bashindex.sh", "bashindex.sh"),
            ("template_createdetails.sh", "createdetails.sh"),
            ("template_details.sh", "details.sh"),
            ("template_diffusion.sh", "diffusion.sh"),
            ("template_movefiles.sh", "movefiles.sh"),
            ("template_dipole_calc.sh", "dipole_calc.sh"),
            ("template_move_index_diffusion_dipole.sh", "move_index_diffusion_dipole.sh"),
            ("template_move_dipolescript.sh", "move_dipolescript.sh"),
            ("template_move_dipole_plots.sh", "move_dipole_plots.sh"),
            ("template_dipole_averaging.sh", "dipole_averaging.sh"),
            ("template_curve_fitting.sh", "curve_fitting.sh"),
            ("template_get_parameters.sh", "get_parameters.sh"),
            ("template_move_index_diffusion_hbond.sh", "move_index_diffusion_hbond.sh"),
            ("template_move_index_solvation_hbond.sh", "move_index_solvation_hbond.sh"),
            ("template_move_ndx_hbond.sh", "move_ndx_hbond.sh"),
            ("template_run_hbonding.sh", "run_hbonding.sh"),
            ("template_build_index_files.sh", "build_index_files.sh"),
            ("template_move_msd.sh", "move_msd.sh"),
            ("template_blockaveraging.sh", "blockaveraging.sh"),
            ("template_move_calc_regression.sh", "move_calc_regression.sh"),
            ("template_get_diffusion_averages.sh", "get_diffusion_averages.sh"),
            ("updated_template_index_solvation_shell_rdf.sh", "index_solvation_shell_rdf.sh"),
            ("template_rdf_integrate.sh", "rdf_integrate.sh"),
            ("updated_template_rdf.sh", "rdf.sh"),
            ("updated_template_index_solvation_shell.sh", "index_solvation_shell.sh"),
            ("updated_template_solvation_shell_com.sh", "solvation_shell_COM.sh"),
            ("template_residue_folders.sh", "residue_folders.sh"),
            ("template_Residue_Info.sh", "Residue_Info.sh"),
            ("template_hbond_averaging.sh", "hbond_averaging.sh"),
            ("template_curve_fitting_hbond.sh", "curve_fitting_hbond.sh"),
            ("template_get_lifetimes.sh", "get_lifetimes.sh"),
        ]

        for template, output in files:
            process_template_file(template, output, residues)

        self.clean_up_files()
        
    def clean_up_files(self):
        directory = '.'
        files_to_remove = ['updated_template_rdf.sh', 
                           'updated_template_index_solvation_shell.sh',
                           'updated_template_index_solvation_shell_rdf.sh', 
                           'updated_template_solvation_shell_COM.sh']

        for filename in files_to_remove:
            file_path = os.path.join(directory, filename)
            if os.path.exists(file_path):
                os.remove(file_path)

        for filename in os.listdir(directory):
            match = re.match(r'^updated_template_(.+\.sh)$', filename)
            if match:
                new_name = match.group(1)
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

        folders = ['Diffusion', 'Solvation', 'RDF', 'MSD', 'Dipole', 'Dipole_Plots', 'HBond', 'HBond_Lifetime', 'Residue_Details', 'Templates']
        for folder in folders:
            os.makedirs(folder, exist_ok=True)

        # Diffusion Folder
        diffusion_files = ['bashindex_diffusion', 'bashindex.sh', 'createdetails.sh', 
                           'details.sh', 'run_diffusion', 'diffusion.sh', 'index.sh', 'movefiles.sh', 'msd.sh']
        for file in diffusion_files:
            shutil.move(file, os.path.join('Diffusion', file))

        # Solvation Folder
        solvation_files = ['index_solvation_shell.sh', 'solvation_shell_COM.sh', 'run_solvation']
        for file in solvation_files:
            shutil.move(file, os.path.join('Solvation', file))

        # RDF Folder
        rdf_files = ['rdf_integrate.sh', 'rdf.sh', 'run_rdf', 'index_solvation_shell_rdf.sh']
        for file in rdf_files:
            shutil.move(file, os.path.join('RDF', file))

        # MSD Folder
        msd_files = ['move_msd.sh', 'blockaveraging.sh', 'move_calc_regression.sh', 'get_diffusion_averages.sh', 'Linear_Regression.py', 'block.averaging_20blocks.py']
        for file in msd_files:
            shutil.move(file, os.path.join('MSD', file))

        # Dipole Folder
        dipole_files = ['dipole_calc.sh', 'dipole.sh', 'dipoles', 'move_index_diffusion_dipole.sh', 'move_dipolescript.sh']
        for file in dipole_files:
            shutil.move(file, os.path.join('Dipole', file))

        # Dipole Plots Folder
        dipole_plots_files = ['move_dipole_plots.sh', 'dipole_averaging.sh', 'curve_fitting.py', 'dipole_averaging.py', 'curve_fitting.sh', 'get_parameters.sh', 'reorientation_times.py']
        for file in dipole_plots_files:
            shutil.move(file, os.path.join('Dipole_Plots', file))

        # HBond Folder
        hbond_files = ['hbonding.sh', 'move_index_diffusion_hbond.sh', 'move_index_solvation_hbond.sh', 
                       'move_ndx_hbond.sh', 'make_index.sh', 'run_hbonding.sh', 'build_index_files.sh', 'indexing', 'hbond_analysis']
                       
        for file in hbond_files:
            shutil.move(file, os.path.join('HBond', file))

        # HBond_Lifetime Folder
        hbond_lifetime_files = ['curve_fitting_hbond.sh', 'curve_fitting_hbond.py', 'hbond_averaging.py', 'hbond_averaging.sh']
        for file in hbond_lifetime_files:
            shutil.move(file, os.path.join('HBond_Lifetime', file))

        # Residue_Details Folder
        residue_details_files = ['residue_folders.sh', 'Residue_Info.sh', 'Residue_Info.py']
        for file in residue_details_files:
            shutil.move(file, os.path.join('Residue_Details', file))
            
        # Templates Folder
        all_files = os.listdir(directory)
        templates_files = [file for file in all_files if file.startswith('template_')]
        for file in templates_files:
            shutil.move(file, os.path.join('Templates', file))

    def browse_residues_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file')
        if fname[0]:
            self.residues_to_analyze.setText(fname[0])

if __name__ == '__main__':
    app = QApplication([])
    processor = FileProcessor()
    processor.show()
    app.exec_()
