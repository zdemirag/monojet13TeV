#! /usr/bin/env python

from ROOT import *
from colors import *
colors = defineColors()

lumi = 1.0

######################################################

#dataDir = "eos/cms/store/user/zdemirag/FrozenMonoJetSlim/"
#dataDir = "/afs/cern.ch/work/d/dabercro/public/Winter15/forZeynep_hadd/"
#dataDir = "/afs/cern.ch/work/z/zdemirag/public/slim_Nov9_new/"

#dataDir = "/tmp/zdemirag/slim_Nov11/"

dataDir = "/afs/cern.ch/work/z/zdemirag/public/slim_unblind/"
dataDir_eos = "eos/cms/store/user/zdemirag/slim_nov17_bkp/slim_Nov17/"

physics_processes = {
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


        'Wlv_ht100': { 'label':'W#rightarrow  l#nu',
                       'datacard':'Wlv',
                       'color' : colors.keys()[2],
                       'ordering': 3,                  
                       'xsec' : 1343.,
                       'files':[dataDir+'WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1+AODSIM.root',],
                       },
        'Wlv_ht200': { 'label':'W#rightarrow  l#nu',
                       'datacard':'Wlv',
                       'color' : colors.keys()[2],
                       'ordering': 3,                  
                       'xsec' : 359.6,
                       'files':[dataDir+'WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1+AODSIM.root',],
                       },
        'Wlv_ht400': { 'label':'W#rightarrow  l#nu',
                       'datacard':'Wlv',
                       'color' : colors.keys()[2],
                       'ordering': 3,                  
                       'xsec' : 48.85,
                       'files':[dataDir+'WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v3+AODSIM.root',],
                       },
        'Wlv_ht600': { 'label':'W#rightarrow  l#nu',
                       'datacard':'Wlv',
                       'color' : colors.keys()[2],
                       'ordering': 3,                  
                       'xsec' : 18.91,
                       'files':[dataDir+'WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1+AODSIM.root',],
                       },
        'QCD_200To300': { 'label':'QCD',
                          'datacard':'qcd',
                          'color' : colors.keys()[1],
                          'ordering': 2,
                          'xsec' : 1735000.0,
                          'files':[dataDir+'QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2+AODSIM.root'],
                          },
        'QCD_300To500': { 'label':'QCD',
                          'datacard':'qcd',
                          'color' : colors.keys()[1],
                          'ordering': 2,
                          'xsec' : 366800.0,
                          'files':[dataDir+'QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2+AODSIM.root'],
                          },
        'QCD_500To700': { 'label':'QCD',
                          'datacard':'qcd',
                          'color' : colors.keys()[1],
                          'ordering': 2,
                          'xsec' : 29370.0,
                          'files':[dataDir+'QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1+AODSIM.root'],
                          },
        'QCD_700To1000': { 'label':'QCD',
                           'datacard':'qcd',
                           'color' : colors.keys()[1],
                           'ordering': 2,
                           'xsec' : 6524.0,
                           'files':[dataDir+'QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1+AODSIM.root'],
                           },
        'QCD_1000To1500': { 'label':'QCD',
                            'datacard':'qcd',
                            'color' : colors.keys()[1],
                            'ordering': 2,
                            'xsec' : 1064.0,
                            'files':[dataDir+'QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2+AODSIM.root'],
                            },
#        'GJets_40To100': { 'label':'#gamma + jets',
#                           'datacard': 'gjets',
#                           'color' :  colors.keys()[6],
#                           'ordering': 1,
#                           'xsec' : 23080.0,
#                           'files':[dataDir+'GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2+AODSIM.root'],
#                           },
#        'GJets_100To200': { 'label':'#gamma + jets',
#                            'datacard': 'gjets',
#                            'color' :  colors.keys()[6],
#                            'ordering': 1,
#                            'xsec' : 9110.0,
#                            'files':[dataDir+'GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2+AODSIM.root'],
#                            },
#        'GJets_200To400': { 'label':'#gamma + jets',
#                            'datacard': 'gjets',
#                            'color' :  colors.keys()[6],
#                            'ordering': 1,
#                            'xsec' : 2281.0,
#                            'files':[dataDir+'GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2+AODSIM.root'],
#                           },
#        'GJets_400To600': { 'label':'#gamma + jets',
#                            'datacard': 'gjets',
#                            'color' :  colors.keys()[6],
#                            'ordering': 1,
#                            'xsec' : 273.0,
#                            'files':[dataDir+'GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1+AODSIM.root'],
#                            },
#        'GJets_600ToInf': { 'label':'#gamma + jets',
#                            'datacard': 'gjets',
#                            'color' :  colors.keys()[6],
#                            'ordering': 1,
#                            'xsec' : 94.5,
#                            'files':[dataDir+'GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1+AODSIM.root'],
#                            },
        'others': { 'label':'Top quark + diboson',
                    'datacard':'others',
                    'color' : colors.keys()[3],
                    'ordering': 2,
                    'xsec' : 831.76,
                    'files':[dataDir+'TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1+AODSIM.root',],
                    },        
        'antitop': { 'label':'Top quark + diboson',
                    'datacard':'others',
                    'color' : colors.keys()[3],
                    'ordering': 2,
                    'xsec' : 26.22,
                    'files':[dataDir_eos+'ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1+RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1+AODSIM.root',],
                    },        
        'top': { 'label':'Top quark + diboson',
                    'datacard':'others',
                    'color' : colors.keys()[3],
                    'ordering': 2,
                    'xsec' : 44.07,
                    'files':[dataDir_eos+'ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1+AODSIM.root'],
                    },        
        'antitop_5f': { 'label':'Top quark + diboson',
                    'datacard':'others',
                    'color' : colors.keys()[3],
                    'ordering': 2,
                    'xsec' : 35.6,
                    'files':[dataDir_eos+'ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1+AODSIM.root'],
                    },        
        'top_5f': { 'label':'Top quark + diboson',
                    'datacard':'others',
                    'color' : colors.keys()[3],
                    'ordering': 2,
                    'xsec' : 35.6,
                    'files':[dataDir_eos+'ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1+AODSIM.root'],
                    },        
        'WW' : { 'label':'Top quark + diboson',
                 'datacard':'others',
                 'color':colors.keys()[3],
                 'ordering': 2,
                 'xsec' : 63.21,
                 'files':[dataDir_eos+'WW_TuneCUETP8M1_13TeV-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1+AODSIM.root',],
                 },
        'ZZ' : { 'label':'Top quark + diboson',
                 'datacard':'others',
                 'color':colors.keys()[3],
                 'ordering': 2,
                 'xsec' : 10.32,
                 'files':[dataDir_eos+'ZZ_TuneCUETP8M1_13TeV-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v3+AODSIM.root',],
                 },
        'WZ' : { 'label':'Top quark + diboson',
                 'datacard':'others',
                 'color':colors.keys()[3],
                 'ordering': 2,
                 'xsec' : 22.82,
                 'files':[dataDir_eos+'WZ_TuneCUETP8M1_13TeV-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1+AODSIM.root',],
                 },
        #991.600 fb--> 0.991 * 10 pb  
        'signal_dm': { 'label':'AV (2 TeV)',
                          'datacard':'signal',
                          'color' : 1,
                          'ordering': 5,
                          'xsec' : 1.,
                          'files':[dataDir+'DMV_NNPDF30_Axial_Mphi-2000_Mchi-1_gSM-0p25_gDM-1p0_13TeV-powheg+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1+AODSIM.root'],
                          },
        'data': { 'label':'Data',
                  'datacard':'data',
                  'color': 1,
                  'ordering': 6,    
                  'xsec' : 1.0,
                  'files':[dataDir+'monojet_SingleElectron+Run2015D.root',],
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