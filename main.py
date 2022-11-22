import os

# Modify these to suit your needs
EXPERIMENTS = "./experiments"
DATA = "./dataset/aligned"
SNAP = 10

# Build the command and run it
cmd = f"/usr/bin/python3 /content/stylegan2-ada-pytorch/train.py "\
  f"--snap {SNAP} --outdir {EXPERIMENTS} --data {DATA}"
!{cmd}