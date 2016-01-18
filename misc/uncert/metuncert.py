import array
import ROOT

tree = ROOT.TChain('nero/events')
tree_up = ROOT.TChain('nero/events')
tree_down = ROOT.TChain('nero/events')

sample = "DMV_NNPDF30_Axial_Mphi-2000_Mchi-1_gSM-0p25_gDM-1p0_13TeV-powheg+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1+AODSIM"
#sample = "DMS_NNPDF30_Pseudoscalar_Mphi-300_Mchi-100_gSM-1p0_gDM-1p0_13TeV-powheg+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1+AODSIM"

tree.Add('root://eoscms.cern.ch//eos/cms/store/user/yiiyama/nerov3photonid/'+sample+'/nero_0000.root')

for iF in range(10):
    tree_up.Add('root://eoscms.cern.ch//eos/cms/store/user/yiiyama/nerov3jecup/'+sample+'/nero_%04d.root' % iF)
    tree_down.Add('root://eoscms.cern.ch//eos/cms/store/user/yiiyama/nerov3jecdown/'+sample+'/nero_%04d.root' % iF)    

outputFile = ROOT.TFile.Open('/afs/cern.ch/user/z/zdemirag/public/monojet/metuncert_'+sample+'.root', 'recreate')
#binning = array.array('d', [200,250,300,350,400,600,1000])
binning = array.array('d', [100. + 50. * x for x in range(6)] + [400., 500., 600., 1000.])
nominal = ROOT.TH1D('nominal', '', len(binning) - 1, binning)
jesup   = ROOT.TH1D('jesup', '', len(binning) - 1, binning)
jesdown = ROOT.TH1D('jesdown', '', len(binning) - 1, binning)
nominal.Sumw2()
jesup.Sumw2()
jesdown.Sumw2()

cut = 'Sum$(jetP4.Pt() > 100.) != 0'

outputFile.cd()
tree.Draw('metP4.Pt()>>nominal', 'mcWeight * (%s)' % cut, 'goff')
tree_up.Draw('metPtJESUP>>jesup', 'mcWeight * (%s)' % cut, 'goff')
tree_down.Draw('metPtJESDOWN>>jesdown', 'mcWeight * (%s)' % cut, 'goff')

rjesup = jesup.Clone('jesup_over_nominal')
rjesup.Divide(nominal)

rjesdown = jesdown.Clone('jesdown_over_nominal')
rjesdown.Divide(nominal)

print "writing the output file"
outputFile.Write()
