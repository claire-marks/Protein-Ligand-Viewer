#!/usr/bin/env python
"""
    Main handler for the protein-ligand viewer Flask app.
    Exscientia coding problem
	Claire Marks
	September 2020
"""

##### IMPORTS ####
import os
from rdkit import Chem
from rdkit.Chem import AllChem, Draw
from flask import Flask, url_for, render_template, Markup, send_from_directory


##### PATHS #####
STRUCTURE_DIRECTORY = os.path.join(os.getcwd(), "structures")


##### INITIALISE WEBAPP #####
app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


##### FUNCTIONS #####
def load_ligands(ligandsFname):
    """
    Parse SDF using RDKit, loading information into a dictionary.
    
    arguments: path to file containing ligands
    returns: dictionary containing ligand info, keys=ligand names
    """
    
    ligandData = {}
    suppl = Chem.SDMolSupplier(os.path.join(STRUCTURE_DIRECTORY, ligandsFname))
    for mol in suppl:         
        molDict = mol.GetPropsAsDict()
        molName = molDict["Molecule Name"]
        ligandData[molName] = molDict
        
        # Save image as 2D SVG
        AllChem.Compute2DCoords(mol)
        img = Chem.Draw.MolsToGridImage([mol], molsPerRow=1, subImgSize=(150, 100), useSVG=True)
        ligandData[molName]["img"] = Markup(img.replace("\n", ""))

    return ligandData


##### ROUTES #####

# Main page
@app.route('/viewer/<structureId>/')
def viewer(structureId):
    # Work out file names from given structure name - assume <structureid>.pdb for protein and <structureid>_ligs.sdf for ligands
    proteinFname = structureId + ".pdb"
    ligandsFname = structureId + "_ligs.sdf"
    
    # Display error message if files do not exist
    errmsg = None
    if os.path.exists(os.path.join(STRUCTURE_DIRECTORY, proteinFname)) is False:
        errmsg = "No protein structure with ID %s found." %(structureId)
        return render_template("index.html", errmsg=errmsg)
    elif os.path.exists(os.path.join(STRUCTURE_DIRECTORY, ligandsFname)) is False:
        errmsg = "Ligand file for structure %s not found." %(structureId)
        return render_template("index.html", errmsg=errmsg)
	
    ligandData = load_ligands(ligandsFname)
	
    return render_template('index.html', 
                           errmsg=errmsg,
                           structureId=structureId, 
                           proteinFname=proteinFname, 
                           ligandsFname=ligandsFname, 
                           ligandData=ligandData)

# route to fetch files from the structure directory
@app.route('/structurefiles/<fname>/')
def get_structure_file(fname):

	return send_from_directory(STRUCTURE_DIRECTORY, fname)
    
    
##### MAIN #####
if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5000')
