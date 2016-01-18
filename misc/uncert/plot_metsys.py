#! /usr/bin/env python                                                                                                                                                         

from ROOT import *
from array import array
from tdrStyle import *

setTDRStyle()

def plotvariations():

    f  = TFile("metuncert.root","READ")
    h1 = f.Get("jesup_over_nominal")
    h2 = f.Get("jesdown_over_nominal")
    
    c4 = TCanvas("c4","c4", 900, 1000)

    # Add Legend                                                                                                                                                                   
    legend = TLegend(.60,.60,.92,.92)
    legend . AddEntry(h2,"MET JES Up/Down","l")
    
    h1.Draw("hist")
    h1.GetYaxis().SetTitle('Scale')
    h1.GetYaxis().CenterTitle()
    h1.GetYaxis().SetTitleOffset(1.2)
    h1.GetXaxis().SetTitle('MET')
    h2.Draw("histsame")
    legend.Draw("same")

    c4.SaveAs("test.root")
    c4.SaveAs("test.pdf")
    c4.SaveAs("test.png")

plotvariations()
