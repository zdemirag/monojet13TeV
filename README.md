# Monojet analysis 13TeV studies

This directory holds the skimmer & slimmer code (slimmer/monojet.C) and the selection macro
(makePlots.py). Its usage is briefly explained below.

The skimmer input is a nero file (preferablly from bambu). This code will drop the unnecessary
branches, and add an other tree with some newly calculated information for the analysis.
This will also replace some of the branches in the events tree depending which control region
we would like to check.

In the future, this code can also be used to calculate shifted / smeared collection for systematic
uncertainty calculations.

Note that, if the input file format changes, the slimmer and skimmer will have to change (at least the .h file)
This is kind of annoying, might want to make it more independent of the version somehow..
At the current implementation it is a TSelector. you will have to run it in root, so after
doing root -l do:

```
gROOT->LoadMacro("TreeManager.cc+");
gROOT->ProcessLine(".L monojet.C++");
TChain* fChain = new TChain("nero/events")
fChain->Add("nero_dy.root");
fChain->Process("monojet")
```
WRITE A WRAPPER AROUND IT! ALSO TEST CONDOR SUBMISSION AND BATCH SUBMISSION


The selection macro is the makePlots.py At the end of this script you can specify the variable you would like to 
draw and also the channel (signal or the control regions or even all). selection.py script will hold the different
selection to be called for each channel. This script relies on a simple TDraw. The weights (lumi, mc weight, etc)
are calculated on the fly. type tree created by the slimmer is added as a friend to the events tree (this is done
in LoadData.py).

To run the selector and plotter do:

```
./makePlots.py -b -q -l
```

Make sure you have a directory called /test where the output histograms will be written to.

To-Do List:

Test the whole chain with the real input files. Try to get the monojet signal results.