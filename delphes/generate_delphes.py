import os
import argparse
import fileinput
import subprocess

parser = argparse.ArgumentParser(description='Delphes production')

parser.add_argument('--lhe', dest='lhe', help='LHE file', default='/tmp/arapyan/unweighted_events.lhe', type=str)
parser.add_argument('--output', dest='output', help='Output file name', default='/tmp/arapyan/test.root', type=str)
parser.add_argument('--numevents', dest='events', help='Number of events to process', default='100', type=int)
parser.add_argument('--ecm', dest='ecm', help='Center of mass energy', default='240', type=float)
parser.add_argument('--pythia8', dest='pythia8', help='Pythia8 settings', default='configInclusive.cmnd', type=str)

args = parser.parse_args()

#define the environment warning
print('Rememer to set the environment first: source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-slc6-gcc62-opt/setup.sh')
print('And point to pythia8: export PYTHIA8DATA=/afs/cern.ch/work/a/arapyan/MCProd/pythia8243/share/Pythia8/xmldoc')

#copy the Delphes executable
os.system('cp /afs/cern.ch/work/a/arapyan/MCProd/Delphes-3.4.2/DelphesPythia8 .')

#modify the number of events and center of mass energy in the pythia8 card
for line in fileinput.input(args.pythia8, inplace=True):
    if 'Beams:eCM' in line:
        line = 'Beams:eCM = {0}\n'.format(args.ecm)
    elif 'Beams:LHEF' in line:
        line = 'Beams:LHEF = {0}\n'.format(args.lhe)
    elif 'Main:numberOfEvents' in line:
        line = 'Main:numberOfEvents = {0}\n'.format(args.events)
    print(line[:-1]) #don't start a new line

print('Will start running with the following paratmerets')
print('Center of mass energy',args.ecm)
print('Number of events',args.events)
print('Pythia config',args.pythia8)

print('DelphesPythia8 delphes_card_ILD.tcl {0} {1}'.format(args.pythia8, args.output))

#run delphes
os.system('/afs/cern.ch/work/a/arapyan/MCProd/Delphes-3.4.2/DelphesPythia8 delphes_card_ILD.tcl {0} {1}'.format(args.pythia8, args.output))


