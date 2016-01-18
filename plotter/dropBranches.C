void dropBranches(){

    //Get old file, old tree and set top branch address
    TFile *oldfile = new TFile("monojet_signal.root");
    TFile *newfile = new TFile("monojet_signal_ps.root","recreate");
    
    
    TIter next (oldfile->GetListOfKeys());
    TKey *key;
    while ((key = (TKey*)next())) {
        if (strstr(key->GetClassName(),"TTree")) {            
            
            std::cout << key->GetName() << std::endl;
            std::string name = key->GetName();            
            if (
                name == "signal_dm_ps_200_1_signal"   ||  
                name == "signal_dm_ps_200_10_signal"  || 
                name == "signal_dm_ps_200_100_signal" || 
                name == "signal_dm_ps_200_150_signal" || 
                name == "signal_dm_ps_200_50_signal") 
            {

                printf (" key : %s is a %s \n",key->GetName(),key->GetClassName());
                TTree *oldtree = (TTree*)oldfile->Get(key->GetName());
                oldtree->SetBranchStatus("*",0);
                oldtree->SetBranchStatus("met",1);
                oldtree->SetBranchStatus("jet1Pt",1);
                oldtree->SetBranchStatus("scaleMC_w",1);
                oldtree->SetBranchStatus("genBos_pt",1);
                TTree *newtree = oldtree->CloneTree();
                newtree->SetName(key->GetName());
            }
            
        }   
    }

    

    /*

    TTree *oldtree = (TTree*)oldfile->Get("signal_h_ggf_signal");
    oldtree->SetBranchStatus("*",0);
    oldtree->SetBranchStatus("met",1);
    oldtree->SetBranchStatus("jet1Pt",1);
    oldtree->SetBranchStatus("scaleMC_w",1);
    oldtree->SetBranchStatus("genBos_pt",1);
    TTree *newtree = oldtree->CloneTree();
    newtree->SetName("signal_h_ggf_signal");


    TTree *oldtree = (TTree*)oldfile->Get("signal_h_vbf_signal");
    oldtree->SetBranchStatus("*",0);
    oldtree->SetBranchStatus("met",1);
    oldtree->SetBranchStatus("jet1Pt",1);
    oldtree->SetBranchStatus("scaleMC_w",1);
    oldtree->SetBranchStatus("genBos_pt",1);
    TTree *newtree = oldtree->CloneTree();
    newtree->SetName("signal_h_vbf_signal");
    */
    
    newfile->Write();
    delete oldfile;
    delete newfile;
}
