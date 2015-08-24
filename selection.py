def build_selection(selection,bin0):

    selections = ['signal','Zll','Wln']

    snippets = {
        #** monojet
        'leading jet pT':['jetP4[0].Pt()>0.',selections],
        #'leading jet eta':['abs(jetP4[0].Eta())<2.4',selections],
        #'jet cleaning':['jetMonojetId[0]==1',selections],
        #'trailing jet':['(jet2.pt() <30 || deltaPhi(jet1.Phi(),jet2.Phi())<2)',selections],
        #'trigger':['((trigger&1)==1 || (trigger&2)==2)',selections],
        #'lepton veto':['nlep==0',['signal']],
        #'extra stuff veto':['nphotons==0&&ntaus==0',selections], 
        #'jet multiplicity':['njets<3',selections],

        #** Control Regions
        'leading lep ID': ['n_tightlep==1',['Wln','Zll']],
        #'leading muon Iso': ['lep1IsIsolated',['Wln']],
        'Zmm':['@lepP4.size()==2 && ((lepPdgId)[0]*(lepPdgId)[1])== -169 ',['Zll']],
        #&& abs(vectorSumMass(lepP4[0].Px(),lepP4[0].Py(),lepP4[0].Pz(),lepP4[1].Px(),lepP4[1].Py(),lepP4[1].Pz())-91)<30',['Zll']],
        #'dilepPt':['vectorSumPt(lepP4[0].Pt(),lepP4[0].Phi(),lepP4[1].Pt(),lepP4[2].Phi())>100',['Zll']],
        'Wln':['@lepP4.size()==1 && abs((lepPdgId)[0])==13 && mt > 50.',['Wln']],
        }

    selectionString = ''
    for cut in snippets:
        if selection in snippets[cut][1]: 
            selectionString += snippets[cut][0]+'&&'

    met  = 'metP4[0].Pt()'

    analysis_bin = {}
    analysis_bin[0] = bin0

    #if selection.find('Zll')>-1: selectionString+='deltaPhi(jet1.Phi(),'+metZ+'Phi)>2 && '+metZ+'>'+str(analysis_bin[0])
    #elif selection.find('Wln')>-1: selectionString+='deltaPhi(jet1.Phi(),'+metW+'Phi)>2 && '+metW+'>'+str(analysis_bin[0])
    #else: 

    selectionString+=met+'>'+str(analysis_bin[0])

    return selectionString

