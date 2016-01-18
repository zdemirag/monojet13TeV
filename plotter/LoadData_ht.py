#! /usr/bin/env python

from ROOT import *
from colors import *
colors = defineColors()

lumi = 1.0

######################################################

dataDir = "/tmp/zdemirag/slim/"
dataDir2 = "/afs/cern.ch/work/z/zdemirag/work/frozen_monojet/monojet/plotter/"

physics_processes = {
#        'Zll': { 'label':'Z#rightarrow ll',
#                       'datacard':'Zll',
#                       'color' : colors.keys()[0],
#                       'ordering': 0,                  
#                       'xsec' : 6025.2,
#                       'files':[dataDir2+"DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v3+AODSIM.root"],
#                 },


        'Zll_ht100': { 'label':'Z#rightarrow ll',
                       'datacard':'Zll',
                       'color' : colors.keys()[0],
                       'ordering': 0,                  
                       'xsec' : 148.0,
                       'files':[dataDir+"DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2+AODSIM.root"],
                 },
        'Zll_ht200': { 'label':'Z#rightarrow ll',
                       'datacard':'Zll',
                       'color' : colors.keys()[0],
                       'ordering': 0,                  
                       'xsec' : 40.94,
                       'files':[dataDir+"DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2+AODSIM.root"],
                       },
        'Zll_ht400': { 'label':'Z#rightarrow ll',
                       'datacard':'Zll',
                       'color' : colors.keys()[0],
                       'ordering': 0,                  
                       'xsec' : 5.497,
                       'files':[dataDir+"DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9_ext1-v1+AODSIM.root"],
                 },
        'Zll_ht600': { 'label':'Z#rightarrow ll',
                       'datacard':'Zll',
                       'color' : colors.keys()[0],
                       'ordering': 0,                  
                       'xsec' : 2.193,
                       'files':[dataDir+"DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2+AODSIM.root"],
                 },        
        'others': { 'label':'Top quark',
                    'datacard':'others',
                    'color' : colors.keys()[3],
                    'ordering': 2,
                    'xsec' : 831.76,
                    'files':[dataDir+'TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1+AODSIM.root',],
                    },        
        'signal_dm_av_1_2': { 'label':'AV (2 TeV)',
                          'datacard':'signal',
                          'color' : 1,
                          'ordering': 5,
                          'xsec' : 1.,
                              'files':['/afs/cern.ch/user/z/zdemirag/lnwork/../public/dm_only/DMV_NNPDF30_Axial_Mphi-2000_Mchi-1_gSM-0p25_gDM-1p0_13TeV-powheg+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1+AODSIM/nero_0000.root'],
                          },


        'data': { 'label':'Data',
                  'datacard':'data',
                  'color': 1,
                  'ordering': 6,    
                  'xsec' : 1.0,
                  'files':[dataDir+'MET+Run2015D-PromptReco+AOD.root'],
                  }
        }

tmp = {}
for p in physics_processes: 
	if physics_processes[p]['ordering']>-1: tmp[p] = physics_processes[p]['ordering']
ordered_physics_processes = []

for key, value in sorted(tmp.iteritems(), key=lambda (k,v): (v,k)):
	ordered_physics_processes.append(key)

def makeTrees(process,tree,channel):
	Trees={}
	Trees[process] = TChain(tree)
	for sample in  physics_processes[process]['files']:
		Trees[process].Add(sample)
	return Trees[process]

######################################################
