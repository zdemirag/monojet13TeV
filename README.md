# Monojet analysis 13TeV studies

At the moment this is a copy of 8 TeV studies with some minor changes. All scripts to be updated.

```
input is bambu files + slimmer / skimmer
```

If the bambu input changes, the slimmer and skimmer will have to change (at least the .h file)
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
WRITE A WRAPPER AROUND IT!

To run the selector and plotter do:
```
./makePlots.py -b -q -l
```

Make sure you have a directory called /test where the output histograms will be written to.

To-Do List:

Test the whole chain with the real input files. Try to get the monojet signal results.