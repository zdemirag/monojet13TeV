#!/bin/csh

cp monojet_TEMP.C monojet.C

sed -i "s/SUFFIX/$1/g" monojet.C

cat > run.C << +EOF

    #include <iostream>
    #include <fstream>
    #include <string>
    #include <vector>
    #include <cstdlib>

    using namespace std;

    void run(){

    gROOT->LoadMacro("TreeManager.cc+");
    TChain* fChain = new TChain("nero/events");

    ifstream sourceFiles("sourceFiles/$1.txt");
    char line[500];
    int count = 0;
    cout << "Adding files from $1 to chain..." << endl;
 
    while (sourceFiles >> line){
        fChain->Add(line);
        ++count;
    }

    cout << count << " files added!" << endl;
    sourceFiles.close();
    
    TStopwatch timer;
    timer.Start();

    fChain->Process("monojet.C++");

    cout << "Done!" << endl;    
    cout << "CPU Time: " << timer.CpuTime() << endl;    
    cout << "Real Time: " << timer.RealTime() << endl;    
    }

+EOF

root -l -b -q run.C
rm -f run.C
rm -f monojet.C

rm -f *_C*
rm -f *_cc*
rm -f *.so*
rm -f *~
