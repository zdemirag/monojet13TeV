gROOT->LoadMacro("TreeManager.cc+");
gROOT->ProcessLine(".L monojet.C++");
TChain* fChain = new TChain("nero/events")
fChain->Add("nero_dy.root");
fChain->Process("monojet")
