import os
from chimera import runCommand as rc # use 'rc' as shorthand for runCommand
from chimera import replyobj # for emitting status messages

os.chdir("/home/pawan/NII-Work/Malaria/CliquePharm/Dynophore/Dynaphore-HIVP/Program")
file_names_pdb = [fn for fn in os.listdir(".") if fn.endswith(".mol2")]


for fn in file_names_pdb:
	
	for fm in file_names_pdb:
		replyobj.status("Processing " + fn)
		replyobj.status("Processing " + fm)
		rc("open " + fn)
		rc("open " + fm)
		rc("match #0 #1 move false")
		rc("close all")	
  
