import os
from chimera import runCommand as rc # use 'rc' as shorthand for runCommand
from chimera import replyobj # for emitting status messages

os.chdir("/home/pawan/Documents/Covid-Protease/16-April/PDB/Fragmet/Co-valent/backup")
file_names_pdb = [fn for fn in os.listdir(".") if fn.endswith(".pdb")]
ref_pdb ="/home/pawan/Documents/Covid-Protease/16-April/PDB/Unliganded/6YB7.pdb"

rc("open " + ref_pdb)

for fn in file_names_pdb:
	replyobj.status("Processing " + fn)
	rc("open " + fn)
	rc("mm #0:10-190 #1:10-190")	
	rc("sel #1")
	new_pdb = "Ali-" + fn
	rc("write format pdb selected #1 "+new_pdb+"")
	rc("close #1")
