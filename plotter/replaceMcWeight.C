void replaceMcWeight(){
    
   
    using namespace std;

    float mcWeight;

    //TFile *file = new TFile("DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v3+AODSIM.root","UPDATE");

    TFile *file = new TFile("/tmp/zdemirag/slim/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8+RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1+AODSIM.root","UPDATE");  
    TTree *oldtree = (TTree*)file->Get("events");

    if(oldtree==NULL)
    {
        cout << "Could not find tree " << "events" << endl
             << "in file " << file->GetName() << endl;
        return;
    }
  
    oldtree->SetBranchAddress("mcWeight",&mcWeight);

    TBranch *branch = oldtree->Branch("mcWeight",&mcWeight,"mcWeight/D");

    for(int i = 0; i < oldtree->GetEntries(); i++)
    {
        oldtree->GetEntry(i);
      
        if ((mcWeight) > 0)
            mcWeight = 1 ;
        if ((mcWeight) < 0)
            mcWeight = -1 ;
        
        branch->Fill();
    }

    file->cd();
    oldtree->CloneTree()->Write("events", TObject::kOverwrite);
    file->Close();
  
}
