#!/bin/csh                                                                                                                       

cp monojet_TEMP.C monojet.C
sed -i "s/SUFFIX/$1/g" monojet.C

cat > Executable.C << +EOF

void Executable(){
    gROOT->LoadMacro("TreeManager.cc+");
    gROOT->ProcessLine(".L monojet.C++");

}

+EOF

root -l -b -q Executable.C
rm -f Executable.C
rm -f monojet.C
mv monojet_C.so monojet_${1}_C.so

echo "FINISHED COMPILING"

cat > run_${1}.C <<EOF

    #include <iostream>
    #include <fstream>
    #include <string> 
    #include <vector> 
    #include <cstdlib>
    #include <stdio>
    #include <TVectorT>
                      
    using namespace std;
        
    void run_${1}() {

    gROOT->LoadMacro("TreeManager_cc.so");
    gROOT->LoadMacro("monojet_${1}_C.so");
  
    TChain* fChain = new TChain("nero/events");
    TChain* globChain = new TChain("nero/all");
    ifstream sourceFiles("sourceFiles/$1.txt");
    char line[500];
    int  count = 0;
    cout<< "Adding files from $1 to chain..."<< endl;
    while (sourceFiles >> line) {
        fChain->Add(line);
        globChain->Add(line);
        ++count;
    }

    cout << count<<" files added!"<<endl;
    sourceFiles.close();
    TStopwatch timer;
    timer.Start();    
    fChain->Process("monojet");

    TFile *Target;
    cout << "/afs/cern.ch/work/z/zdemirag/work/run2/monojet/monojet13TeV/slimmer/eos/cms/store/user/zdemirag/nero_skim/monojet_${1}.root" << endl;

    //Target = new TFile("/afs/cern.ch/work/z/zdemirag/work/run2/monojet/monojet13TeV/slimmer/eos/cms/store/user/zdemirag/nero_skim/monojet_${1}.root","UPDATE");
    Target = new TFile("monojet_${1}.root","UPDATE");
    //Target = TFile::Open( "/afs/cern.ch/work/z/zdemirag/work/run2/monojet/monojet13TeV/slimmer/eos/cms/store/user/zdemirag/nero_skim/monojet_${1}.root", "UPDATE");
    globChain->Merge(Target->GetFile(),0,"keep");
    
    float mcWeight = 0.0; float total = 0.0; float tmp = 0.0;
    globChain->SetBranchAddress("mcWeight",&mcWeight);

    for (int entry =0; entry < globChain->GetEntries(); entry++){
        globChain->GetEntry(entry);
        tmp = mcWeight;
        if (tmp > 0) tmp = 1.0;
        else tmp = -1.0;
        total += tmp;
    }

    TH1F *htotal = new TH1F("htotal","htotal",1,0,1);
    //htotal->Fill(total);
    htotal->SetBinContent(1,total);
    htotal->Write();

    std::cout << "Total number of effective events: " << total << std::endl;
    //TVectorD *v(1);
    //v[0] = total;
    //v.Write("total");
        
    Target->SaveSelf(kTRUE);

    cout << "\n\nDone!" << endl;
    cout << "CPU Time : " << timer.CpuTime() <<endl;
    cout << "RealTime : " << timer.RealTime() <<endl;                             
    cout <<"\n";
}
EOF
echo "WROTE A NEW RUN_{SOURCE}.C FILE"

root -l -b -q  run_${1}.C
mv monojet_${1}.root /afs/cern.ch/work/z/zdemirag/work/run2/monojet/monojet13TeV/slimmer/eos/cms/store/user/zdemirag/nero_skim/monojet_${1}.root
rm -f  run_${1}.C
rm -f  monojet_${1}_C.so
