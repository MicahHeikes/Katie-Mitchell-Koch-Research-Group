# Diffusion Steps
 
1. Move all .sh files into diffusion folder

2. Move into the folder analysis folder and create a new folder titled diffusion

3.  In diffusion folder, we want to create a folder for each solvent accessible region.  This is done by executing the bash script folders.sh.

4.  Copy and rename the index.dat file from each folder in Solvation to details.txt, this can be done by executing the createdetails.sh bash script. 

5.  If you look at details.txt you will notice that the first column lists the time snapshot, next is the number of molecules in question (water in our case) and third lists the assigned number of each molecule.  We need to get rid of both the time snapshot and the number of molecules present.  To do this execute the details.sh script.  View the file again and you will notice the first 16 lines of the page have been deleted.

6.  We need to move two bash scripts into each residue folder, index.sh and msd.sh.  To do this run the movefile.sh bash script. Be sure to 
edit the .xtc and .gro names in the msd.sh script to match the name you assigned for your simulation. 

7.  Next we need to execute the index.sh bash script in each residue folder.  This can be done by running the bashindex.sh script.

8.  Now we have everything ready to do mean square displacement analysis.  Run the diffusion.sh bash script, this will take a while.  The output of the diffusion.sh script is an msd.xvg file for each index file.  You can check the progress of diffusion by seeing how many residue folders have msd.xvg files populated in them. 

