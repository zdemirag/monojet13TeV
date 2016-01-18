#! /usr/bin/env python

import os, re, array, ROOT
import sys
from optparse import OptionParser

# - S U B R O U T I N E S -----------------------------------------------------------------------------

# Print Event information
def printEventInfo(tree):
  print '{0:10s}: {1:10d} | {2:10s}: {3:10d} | {4:10s}: {5:10d}'\
  .format('Run',tree.runNum,'LumiSec',tree.lumiNum,'EventNum',tree.eventNum) 
  return

# Print MET information
def printMetInfo(tree):
  print '{0:10s}: {1:10.4f} | {2:10s}: {3:10.1f}'\
  .format('PFMet',tree.met,'Phi',tree.metPhi 
  return

#Print Jet information
def printJetInfo(tree):
  # Num jets
  print '{0:10s}: {1:10d}'\
  .format('nJets',tree.jetP4.GetEntriesFast()) 
  for i in range (0,tree.jetP4.GetEntriesFast()):
    # Jet
    print '{0:10s}: {1:10.4f} | {2:10s}: {3:10.4f} | {4:10s}: {5:10.4f}'\
    .format('JetPt',tree.jetP4[i].Pt(),'JetEta',tree.jetP4[i].Eta(),'JetBtag',tree.jetBdiscr[i]) 
  return

# Print Lepton information
def printLepInfo(tree):
  # Num leptons
  print '{0:10s}: {1:10d}'\
  .format('nLeptons',tree.lepP4.GetEntriesFast()) 
  for i in range (0,tree.lepP4.GetEntriesFast()):
    # First Lepton
    print '{0:10s}: {1:10.4f} | {2:10s}: {3:10.4f} | {4:10s}: {5:10.1f}'\
    .format('LepPt',tree.lepP4[i].Pt(),'LepEta',tree.lepP4[i].Eta(),'LepId',tree.lepPdgId[i]) 
  return

# Print Photon information
def printPhoInfo(tree):
  # Num photons
  print '{0:10s}: {1:10d}'\
  .format('nPhotons',tree.photonP4.GetEntriesFast()) 
  for i in range (0,tree.photonP4.GetEntriesFast()):
    # Photon
    print '{0:10s}: {1:10.4f} | {2:10s}: {3:10.4f}'\
    .format('PhoPt',tree.photonP4[i].Pt(),'PhoEta',tree.photonP4[i].Eta()) 
  return

# Print Taus information
def printTauInfo(tree):
  # Num taus
  print '{0:10s}: {1:10d}'\
  .format('nTaus',tree.tauP4.GetEntriesFast()) 
  # Tau Lepton
  for i in range (0,tree.tauP4.GetEntriesFast()):
    print '{0:10s}: {1:10.4f} | {2:10s}: {3:10.4f}'\
    .format('TauPt',tree.tauP4[i].Pt(),'TauEta',tree.tauP4[i].Eta()) 
  return

# - M A I N ----------------------------------------------------------------------------------------

# Prepare the command line parser
parser = OptionParser()
parser.add_option("-f", "--file", dest="input_file", default='NeroNtuple.root',
                  help="input root file [default: %default]")
parser.add_option("-t", "--treename", dest="input_tree", default='events',
                  help="root tree name [default: %default]")
parser.add_option("-n", "--nprocs", dest="nprocs", type="int", default=10,
                  help="number of processed entries [default: %default]")
(options, args) = parser.parse_args()

# Get all the root classes
from ROOT import *

# Open the correct input file and get the event tree
input_file = TFile.Open(options.input_file)
if input_file:
  print 'INFO - Opening input root file: ' + options.input_file
  
else:
  print 'ERROR - Cannot open input root file: ' + options.input_file + ' , exiting!'
  raise SystemExit
  
input_tree = input_file.FindObjectAny(options.input_tree)
if input_tree:
  print 'INFO - Opening root tree: ' + options.input_tree
  
else:
  print 'ERROR - Cannot open root tree: ' + options.input_tree + ' , exiting!'
  raise SystemExit

#initialize 
n_jet=0; n_met=0; n_njet=0; n_nlep=0; n_ntau=0; n_npho=0;

# Check the number of entries in the tree
n_entries = input_tree.GetEntriesFast()
print 'INFO - Input tree entries: ' + str(n_entries)

# Determine number of entries to process
if options.nprocs > 0 and options.nprocs < n_entries:
  n_entries = options.nprocs

print 'INFO - Number of entries to be processed: ' + str(n_entries)

# Loop over the entries
for ientry in range(0,n_entries):
  # Grab the n'th entry
  input_tree.GetEntry(ientry)
  print 'INFO ------------------------ Event '+str(ientry)+' ------------------------ '
  # Print event information
  #print '\n'
  printEventInfo(input_tree)
  
  # Print MET information
  #print '\n'
  printMetInfo(input_tree)
  
  # Print Jet information
  #print '\n'
  printJetInfo(input_tree)
     
  # Print FatJet information
  #print '\n'
  printFatJetInfo(input_tree)
     
  # Print Lepton information
  #print '\n'
  printLepInfo(input_tree)

  # Print Photon information
  #print '\n'
  printPhoInfo(input_tree)

  # Print Tau information
  #print '\n'
  printTauInfo(input_tree)

  print '\n'
