# Diffusion Coefficient Calculation Steps

1. Move all .sh files to diffusion folder

2. Run the bash script move_and_bash_calc.sh, this will move the bash script calculate_diff.sh into each residue folder and run it.

3. When you look in each residue foler you will see 2 new text files, Diffusion_Coefficients.txt and Average_Diffusion_Coefficient.txt.  Diffusion_Coefficients.txt lists
   a diffusion coefficient for each timeframe you assigned for msd.  If you looked at MSD every 200 ps then the first value is from 0 -> 200, the second from 200 -> 400 and 
   so on.  Average_Diffusion_Coefficient.txt is an average of all diffusion coefficients.

4. In the diffusion folder a file named Diffusion_Coefficient_Averages has also been made, this contains the average diffusion coefficient from each residue folder and is   
   listed in order.