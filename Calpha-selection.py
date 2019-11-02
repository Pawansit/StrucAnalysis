
import os
from chimera import runCommand as rc # use 'rc' as shorthand for runCommand
from chimera import replyobj # for emitting status messages

os.chdir("/home/pawan/NII-Work/Projects/")
file_names_pdb = [fn for fn in os.listdir(".") if fn.endswith(".pdb")]


for fn in file_names_pdb:
  replyobj.status("Processing " + fn)
  rc("open " + fn)
  rc("del element.H")
  rc("sel #0:@CA")
  Mol2_name = fn +"_NoH.mol2"
  rc("write format mol2 0 "+Mol2_name+"")
  rc("close all")
