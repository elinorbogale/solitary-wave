—————————————— READ ME ————————————
Version: 15.10.2026

PLEASE NOTE: The files in this repository are still in the process of being sorted, labeled and edited
for clarity to the reader! I will make sure to get in more detail :)

—> Overview
Consicely, the contents include selected program scripts developed by the author in a primary study titled, „Impulse decimation and solitary wave expansion in inverse tapered chains“ and a secondary study, which is yet to be released. The Programming Languages used include Python, C++ and MATLAB. 

—> Research Area
To fully understand and make use of the code in any way, I would recommend looking over the following topics: dynamics of inertia bodies, Delta Potentials, contact forces, momentum, disspative forces, Energy packets, and oscillations.

Keywords or buzzterms you might come across often in this area would be: solitons (single-moving energy packets), Hertzian (grain interaction potential is set to a certain power - usually 1.5), nonlinear (the equations of motions of our system are nasty to solve because they are not linear, and hence not separable)…

In physical terms, we set up a relatively long chain of metallic spheres (what we refer to as grains) initially aligned lined up next to each other and without any compression. The ends of the chain were fixed by two walls and subjected the start of the grain (left end of the chain) with an initial velocity. The exact geometry of the chain can be changed, but in this instance, we gradually increased the size of all the radii from left to right. After the left end is excited, it hits the next grain, which hits the third grain and so on; by the end of it, the whole chain is oscillating at different frequencies, but a solitary wave (continuous energy packet) is formed.The best visual explanation are those string of silver Newton Balls that swing back and forth  on the desks of CEOs in movies. 

And why is this important? Well, looking at these systems can open avenues in the distribution/attenuation of impacts (like car shocks) or the amplification of acoustic signals. As a physicist, work on the theory and let engineers bring it to life.

—> Data Simulation

The bulk of the simulation itself is based on a modification of an original code by Adam Sokolow named TaperChainMain.cpp (which includes additional internal packages). The program has been modified to accommodate for a vast geometric variety of possible configurations. Output files include energy, velocity, displacements and force applied.

—> Parametrizaton
{still pending - will rehash parameter file and instructions} As with any program, the correct usage of the parameters is essential for getting the right results, if any. 

—> Post-Processing
An assessment and evaluation of the data is conducted using MATLAB primarily. Fitting and interpolation procedures will be further detailed in the script and supporting docs. A few scripts already uploaded to the repo show a time -> frequency Fourier transform and power spectrum data. A large part of the data work involves the transformation of the wave‘s propagation from time to space, or a simultaneous view of the physical space over time (or both). A separate process to determine the moving average of the solitary wave in terms of grain widths was made possible, with the help of (who guessed it), Liquid Chromatography. I will upload the scripts for these programs. 

-> Visualisation
As with the processing step, I have compiled figures in Matlab, and to a certain extent, also in Python. For the latter I rely on these two libraries, with further supporting libraries: Matplotlib (good for most graphics), Mayavi (preferred for 3D and overlapping data), vks. The front cover of the Journal’s November 2026 issue will feature a design I programmed using Python, the file is titled self-referentially. 
