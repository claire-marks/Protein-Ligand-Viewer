# Protein-Ligand Viewer - README
Claire Marks
September 2020

### Overview

The protein-ligand viewer is a Flask app that can be used to visualise structures of proteins with bound ligands.

It uses PV viewer to display the structures, and shows a table containing the details of all ligands present.

### Requirements

All requirements are given in the requirements.txt file. A conda environment can be created using:

`conda create --name <envname> --file requirements.txt`


### Using the viewer

For the purposes of this, run the Flask app using a development server with the following command:

`python viewer.py`

By default the viewer can be seen in a browser on host 0.0.0.0 and port 5000, however these can be edited in the last line of file viewer.py if you wish.

To view the provided example files, go to http://0.0.0.0:5000/viewer/cdk2/ (or http://localhost:500/viewer/cdk2/) in your browser. To begin with, the protein structure and all ligands are shown together. The protein can be displayed using cartoon, ball and stick, or sphere representations by using the buttons beneath the viewer window. Ligands can be toggled on or off by using the individual 'hide'/'show' buttons in the table, or the 'hide all'/'show all' buttons beneath it. Molecules in the table can be sorted according to their properties by clicking the relevant column header.

Clicking on a part of the structure in the viewer will display the chain, residue, and atom (for parts of the protein), or the ligand name. To center the view on a different part of the structure, double click on it.

Other proteins/ligands can also be viewed, as long as the relevant files exist in the 'structures' directory. It is assumed that files follow the naming convention '<structureid>.pdb' and '<structureid>_ligs.sdf' for the protein and ligands respectively. For example, to view protein 'antibody.pdb' and associated ligands 'antibody_ligands.sdf', go to the address http://0.0.0.0:5000/viewer/antibody/. Unfortunately, only .sdf files in the 'V2000' format are supported at the moment.
