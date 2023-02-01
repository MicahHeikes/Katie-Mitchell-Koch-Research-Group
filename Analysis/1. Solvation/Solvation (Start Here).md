# Solvation Steps
 
1. Create folder named analysis

2. Inside analysis folder create a solvation folder

3. Inside solvation folder, run the bash script index_solvation_shell.sh, this will create a folder and index files for each region of solvent accessible residues.  Be sure to 
edit the .xtc and .gro names to match the name you assigned for your simulation. THIS WILL NEED TO BE DONE FOR MOST SCRIPTS.

4. Run the bash script solvation_shell_com.sh.  This will look for water molecules within 6 angstroms of our created index.ndx (solvent accessible residues) file and output a file titled index.dat. 

5. After the script has finished running look at the index.dat file, the first column of numbers tells us at what time the solvation layer was analyzed. The second column tells us how many waters are present during that instance in time. The following numbers are the assigned molecule number of each water present, we will use these molecule identifiers to track their movement over time. 
