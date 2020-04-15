import os
from chimera import runCommand as rc # use 'rc' as shorthand for runCommand
from chimera import replyobj # for emitting status messages

os.chdir("/home/pawan/Documents/Covid-Protease/docking/Clusters/Cluster-2")
file_names_pdb = [fn for fn in os.listdir(".") if fn.endswith(".pdb")]


for fn in file_names_pdb:
  replyobj.status("Processing " + fn)
  rc("open " + fn)
  rc("addh")
  rc("addcharge")
  Mol2_name = fn[:-4] +".mol2"
  rc("write format mol2 0 "+Mol2_name+"")
  rc("close all")
