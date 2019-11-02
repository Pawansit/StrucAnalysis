import os
from chimera import runCommand as rc
from chimera import replyobj

os.chdir("/home/pawan/NII-Work/Projects/")
file_names_pdb = [fn for fn in os.listdir(".") if fn.endswith(".pdb")]

for fn in file_names_pdb:
  replyobj.status("Processing " + fn)
  rc("open " + fn)
  rc("del element.H")
  rc("intersurf #0:.a #0:.b select true prune 7")
  new_pdb = "Interface" + fn
  rc("write format pdb selected 0 "+new_pdb+"")
  rc("close all")
