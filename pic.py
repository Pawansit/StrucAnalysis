import os
from chimera import runCommand as rc
from chimera import replyobj
os.chdir("/home/pawan/Documents/Covid-Protease/Ligand")
file_names_pdb = [fn for fn in os.listdir(".") if fn.endswith(".pdb")]

for fn in file_names_pdb:
  replyobj.status("Processing " + fn)
  rc("open " + fn)
  name = fn[:-4]+".jpeg"
  rc("copy file "+name+" width 6 height 5 units in supersample 4  dpi 300")
  rc("close #1")
