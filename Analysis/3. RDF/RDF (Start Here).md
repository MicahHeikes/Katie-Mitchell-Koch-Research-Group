# RDF Steps
 
1. Inside analysis folder, create folder named RDF

2. In the RDF foler just created, we need to create index files for each solvent accessible residue to use as a reference, to do this run the index_solvation_shell.sh bash script. Be sure to 
edit the .xtc and .gro names to match the name you assigned for your simulation. 

3. Now that we have the reference index.ndx files, we can run RDF calculations by running the rdf.sh bash script.

4. After rdf.sh has finished, in each residue folder you should see an rdf.xvg file.

5. To calculate the population density within the first solvation layer we will run the rdfint.sh bash script.  If possible sbatch this script, this will give you an output
file with all the integrals listed.

6. We want a file with just the integrals, to do this we will utilize the grep command using the intgrep.sh bash script. This is only applicable if you sbatched the job and have an output file
such as slurm-55864.out for example.  If you did this be sure to alter the name of the input file to your file name.

6. Look at the integrals.txt file, it should have as many integrals as you do residues.  If you haven't changed the residue numbers it will be 23 integrals. 
