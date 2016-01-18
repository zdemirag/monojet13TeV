from ROOT import *

f = TFile("scalefactors_v4.root","READ")

#f = TFile("puWeights_13TeV_25ns.root","READ")

h = {}
#h['puWeights'] = f.Get("puWeights")

#h['wnlo012_over_wlo'] = f.Get("wnlo012_over_wlo/wnlo012_over_wlo")
#h['znlo012_over_zlo'] = f.Get("znlo012_over_zlo/znlo012_over_zlo")
#h['z3jnlo012_over_z3jlo'] = f.Get("z3jnlo012_over_z3jlo/z3jnlo012_over_z3jlo")
h['anlo1_over_alo'] = f.Get("anlo1_over_alo/anlo1_over_alo")
h['a_ewkcorr'] = f.Get("a_ewkcorr/a_ewkcorr")
#h['w_ewkcorr'] = f.Get("w_ewkcorr/w_ewkcorr")
#h['z_ewkcorr'] = f.Get("z_ewkcorr/z_ewkcorr")


#h['znlohist'] = f.Get("znlo012/znlo012_nominal")
#h['zlohist'] = f.Get("zlo/zlo_nominal")

h['alo'] = f.Get("alo/alo_nominal")
h['anlo'] = f.Get("anlo1/anlo1_nominal")

h['ratio'] = h['anlo'].Clone()
h['ratio'].Divide(h['alo'])


#genBos_pt
w= {}
for hist in h:
    w[hist] = "("
    for i in range(1,h[hist].GetNbinsX()+1):
        print hist,h[hist].GetBinContent(i),h[hist].GetBinLowEdge(i),h[hist].GetBinLowEdge(i+1)
        w[hist]=w[hist]+str(h[hist].GetBinContent(i))+"*(genBos_pt>"+str(h[hist].GetBinLowEdge(i))+"&&genBos_pt<="+str(h[hist].GetBinLowEdge(i+1))+")"
        #w[hist]=w[hist]+str(h[hist].GetBinContent(i))+"*(npv>"+str(h[hist].GetBinLowEdge(i))+"&&npv<="+str(h[hist].GetBinLowEdge(i+1))+")"
        if i<h[hist].GetNbinsX():
            w[hist]+="+"
    w[hist]+=")"
    print hist,w[hist]
