#!/bin/bash

source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-slc6-gcc62-opt/setup.sh

export PYTHIA8DATA=/afs/cern.ch/work/a/arapyan/MCProd/pythia8243/share/Pythia8/xmldoc

echo "Now you can do: python generate_delphes.py --lhe /tmp/arapyan/ee2lepton.lhe --numevents 1000000 --ecm 91.1876 --pythia8 configInclusive.cmnd --output /tmp/arapyan/ee2lepton.root"

