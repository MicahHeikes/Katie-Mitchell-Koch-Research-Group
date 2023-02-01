# How to identify Solvent Accesible Surface Area
 
1. Load the protein of interest into UCSF Chimera, follow the download link if you do not have it. It's free!

2. On the top toolbar, select Actions -> Surface -> Show

3. On the top toolbar, select Tools -> Structure Analysis -> Render By Attribute

4. Towards the top of the pop-up window it will say "Attributes of atoms", change "atoms" to "residues"

5. Just below that you will see "choose attr", select AreaSAS.

6. Go to File -> Save Attributes, then click okay in the bottom right.  You can now exit Chimera.

7. Open and view the file in a text editor, the first column represents the assigned amino acid number followed by the chain identifier.  The next column of values is the area exposed to solvent. In the example below I would exclude residue 90 from my analysis because it is a buried residue.

                        :88.A	  60.979719996452332
                        :89.A	  26.847487822175026
                        :90.A	  0.0
                        :91.A	  48.802507400512695
                        :92.A	  62.521901279687881
                        :93.A	  11.463784137740731
                        :94.A	  19.184624820947647
                        :95.A	  54.410918235778809
	
	
