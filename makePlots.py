#! /usr/bin/env python

import sys, os, string, re
from multiprocessing import Process
from array import array
from LoadData import *
from ROOT import *
from math import *
from tdrStyle import *
from selection import build_selection
from datacard import dump_datacard
from pretty import plot_ratio, plot_cms

setTDRStyle()
gROOT.LoadMacro("functions.C+");

print "Starting Plotting Be Patient!"

lumi = 40.02

def plot_stack(channel, name,var, bin, low, high, ylabel, xlabel, setLog = False):

    folder = 'test'
    yield_Zll = {}
    yield_dic = {}
    yield_Wln = {}
    yield_signal = {}
    stack = THStack('a', 'a')
    added = TH1D('a', 'a',bin,low,high)
    added.Sumw2()

    Variables = {}    
    cut_standard= build_selection(channel,200)
    print "Channel is: ", channel, " variable is: ", var, " Selection is: ", cut_standard,"\n"

    reordered_physics_processes = []
    if channel == 'Zll': reordered_physics_processes = reversed(ordered_physics_processes)
    else: reordered_physics_processes = ordered_physics_processes
 
    for Type in reordered_physics_processes:
        # Create the Histograms
        histName = Type+'_'+name+'_'+channel
        Variables[Type] = TH1F(histName, histName, bin, low, high)
        Variables[Type].Sumw2()

        all_tree   = makeTrees(Type,"all",channel)
        n_allentries = all_tree.GetEntries()
        #print 'INFO - Input all entries: ' + str(n_allentries) + ' for sample: '+ Type
        ## Get total number of entries
        total = 0.0
        for i in range(0,n_allentries):
            all_tree.GetEntry(i)
            tmp = all_tree.mcWeight
            if tmp > 0: tmp = 1.0
            else: tmp = -1.0
            total += tmp
        #print Type, "total mcWeight in all tree in the given ntuples" , total        

        input_tree   = makeTrees(Type,"events",channel)
        n_entries = input_tree.GetEntries()
        seentotal = 0.0
        # Loop over the entries
        # Maybe we can optimize this by saving it in the slimmer
        for ientry in range(0,n_entries):
            # Grab the n'th entry
            input_tree.GetEntry(ientry)
            tmp = input_tree.mcWeight
            if tmp > 0: tmp = 1.0
            else: tmp = -1.0
            seentotal += tmp
        #print Type, "total mcWeight in events tree in the given ntuples" , seentotal        

        weight = seentotal * float(lumi)*physics_processes[Type]['xsec']/total
        #print "weight", weight, "seentotal", seentotal, "lumi", lumi, physics_processes[Type]['xsec'], total

        if Type.startswith('QCD') or Type.startswith('Zll') or \
        Type.startswith('others') or Type.startswith('Wlv') or \
        Type.startswith('Zvv'):

            Variables[Type].SetFillColor(physics_processes[Type]['color'])
            Variables[Type].SetLineColor(physics_processes[Type]['color'])
            makeTrees(Type,'events',channel).Draw(var + " >> " + histName,"(" + cut_standard + ")*" +str(weight),"goff")
            Variables[Type].Scale(float(lumi)*1000)
            stack.Add(Variables[Type],"hist")
            added.Add(Variables[Type])

        if Type.startswith('signal_higgs'):
            Variables[Type].SetLineColor(1)
            Variables[Type].SetLineWidth(3)
            Variables[Type].SetLineStyle(8)
            makeTrees(Type,"events",channel).Draw(var + " >> " + histName,"(" + cut_standard + ")*"+str(weight),"goff")
            Variables[Type].Scale(float(lumi)*1000)
                        
        if Type.startswith("data"):
            Variables[Type].SetMarkerStyle(20)
            makeTrees(Type,"events",channel).Draw(var + " >> " + histName,  "(" + cut_standard + ")*"+str(weight), "goff")
        
        yield_dic[Type] = round(Variables[Type].Integral(),3)

    dump_datacard(channel,yield_dic)

    #added.Write()

    legend = TLegend(.60,.60,.92,.92)
    for process in  ordered_physics_processes:
        Variables[process].SetTitle(process)
        #Variables[process].Write()
        if process is not 'data':
            legend . AddEntry(Variables[process],physics_processes[process]['label'] , "f")
        else:
            legend . AddEntry(Variables[process],physics_processes[process]['label'] , "p")

    c4 = TCanvas("c4","c4", 900, 1000)
    c4.SetBottomMargin(0.3)
    c4.SetRightMargin(0.06)

    stack.SetMinimum(0.1)

    if setLog:
        c4.SetLogy()
        stack.SetMaximum( stack.GetMaximum()  +  1000*stack.GetMaximum() )
    
    stack.Draw()
    stack.GetYaxis().SetTitle(ylabel)
    stack.GetYaxis().CenterTitle()
    stack.GetXaxis().SetTitle(xlabel)
    stack.GetXaxis().SetLabelSize(0)
    stack.GetXaxis().SetTitle('')

    Variables['data'].Draw("Esame")
    Variables['signal_higgs'].Draw("same")
    
    legend.SetShadowColor(0);
    legend.SetFillColor(0);
    legend.SetLineColor(0);

    legend.Draw("same")
    plot_cms(True,lumi)

    Pad = TPad("pad", "pad", 0.0, 0.0, 1.0, 1.0)
    Pad.SetTopMargin(0.7)
    Pad.SetFillColor(0)
    Pad.SetGridy(1)
    Pad.SetFillStyle(0)
    Pad.Draw()
    Pad.cd(0)
    Pad.SetRightMargin(0.06)
    
    data = Variables['data'].Clone()
    plot_ratio(False,data,added,bin,xlabel)

    f1 = TF1("f1","1",-5000,5000);
    f1.SetLineColor(4);
    f1.SetLineStyle(2);
    f1.SetLineWidth(2);
    f1.Draw("same")

    c4.SaveAs(folder+'/Histo_' + name + '_'+channel+'.pdf')

    del Variables
    del var
    c4.IsA().Destructor( c4 )
    stack.IsA().Destructor( stack )

arguments = {}
#                = [var, bin, low, high, yaxis, xaxis, setLog]
arguments['met']    = ['met','metP4[0].Pt()',16,200,1000,'Events/50 GeV','E_{T}^{miss} [GeV]',True]
arguments['metRaw'] = ['metRaw','metRaw',16,200,1000,'Events/50 GeV','Raw E_{T}^{miss} [GeV]',True]
arguments['genmet'] = ['genmet','genmet',16,200,1000,'Events/50 GeV','Generated E_{T}^{miss} [GeV]',True]
arguments['jetpt']  = ['jetpt','jet1.pt()',17,150,1000,'Events/50 GeV','Leading Jet P_{T} [GeV]',True]
arguments['njets']  = ['njets','njets',3,1,4,'Events','Number of Jets',True]

#channel_list = ['signal']
#channel_list  = ['signal','Wln','Zll']
channel_list  = ['Zll','Wln']
#variable_list = ['met','jetpt','njets','metRaw','genmet']
processes     = []

variable_list = ['met']

for channel in channel_list:
    for var in variable_list:
        arguments[var].insert(0,channel)
        print  arguments[var]
        process = Process(target = plot_stack, args = arguments[var])
        process.start()
        processes.append(process)
        arguments[var].remove(channel)
for process in processes: 
    process.join()
