# Monojet analysis 13TeV studies

At the moment this is a copy of 8 TeV studies with some minor changes. All scripts to be updated.

```
input is bambu files + slimmer / skimmer
```

if the bambu input changes, the slimmer and skimmer will have to change (at least the .h file)

To run do:
```
./makePlots.py -b -q -l
```

Make sure you have a directory called /test where the output histograms will be written to.


To-Do List:

1) Add trigger info to the slimmer/skimmer
2) Add met + Z or W to the slimmer/skimmer
3) Write a preliminary selector/plotter that selects events with Jet > 100 GeV