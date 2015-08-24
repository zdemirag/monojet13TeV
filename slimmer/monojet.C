#define monojet_cxx

#include "monojet.h"
#include <TH2.h>
#include <TStyle.h>
#include <TLorentzVector.h>
#include <vector>

using namespace std;

float dR_cut = 0.4;
float uPar = -9999. ; float uPerp = -9999.;
int n_tightlep = 0;
TBranch *bUPar;
TBranch *bUPerp;
TBranch *bntightlep;

void monojet::Begin(TTree *tree)
{
   // The Begin() function is called at the start of the query.
   // When running with PROOF Begin() is only called on the client.
   // The tree argument is deprecated (on PROOF 0 is passed).

   TString option = GetOption();

   // Get total weight from all
   TFile   *inFile         = tree->GetCurrentFile();
   TTree   *allTree        = (TTree*)inFile->Get("nero/all");
    
   allTree->SetBranchAddress("mcWeight", &mcWeight);
   allTree->SetBranchAddress("puTrueInt", &puTrueInt);
   allTree->GetEntry();

   histoFile = new TFile("monojet_dy.root","RECREATE");
   histoFile->cd();
    
   clonetree = allTree->CloneTree();

   tree->SetBranchStatus("*",0);
   tree->SetBranchStatus("isRealData",1);
   tree->SetBranchStatus("runNum",1);
   tree->SetBranchStatus("lumiNum",1);
   tree->SetBranchStatus("eventNum",1);
   tree->SetBranchStatus("rho",1);
   tree->SetBranchStatus("jetP4",1);
   tree->SetBranchStatus("jetPuId",1);
   tree->SetBranchStatus("jetMonojetId",1);
   tree->SetBranchStatus("jetMonojetIdLoose",1);
   tree->SetBranchStatus("lep*",1);
   tree->SetBranchStatus("metP4",1);
   tree->SetBranchStatus("genP4",1);
   tree->SetBranchStatus("photon*",1);
   tree->SetBranchStatus("tauP4",1);
   tree->SetBranchStatus("tauId",1);
   tree->SetBranchStatus("tauIso",1);

   eventstree = tree->CloneTree(0);

   bUPar  = eventstree->Branch("uPar" ,&uPar ,"uPar/F");
   bUPerp = eventstree->Branch("uPerp",&uPerp,"uPerp/F");

   bntightlep = eventstree->Branch("n_tightlep",&n_tightlep,"n_tightlep/I");

   //Setting up new tree
   tm = new TreeManager("type", "Monojet signal Tree" /*, histoFile*/);

   tm->AddVar("run","int");
   tm->AddVar("lumi","int");
   tm->AddVar("event","int");
   tm->AddVar("event_type","int");

   tm->InitVars();
    
}

void monojet::SlaveBegin(TTree * /*tree*/)
{
   // The SlaveBegin() function is called after the Begin() function.
   // When running with PROOF SlaveBegin() is called on each slave server.
   // The tree argument is deprecated (on PROOF 0 is passed).

   TString option = GetOption();

}

Bool_t monojet::Process(Long64_t entry)
{
    GetEntry(entry);

    if( entry % 5000 == 0 ) cout << "Processing event number: " << entry << endl;
    cout << "Processing event number: " << entry << endl;

    // To make the processing fast, apply a very looose selection
    if (((TLorentzVector*)((*metP4)[0]))->Pt() < 40. or jetP4->GetEntries() < 1) return kTRUE;

    //this is the type tree
    tm->SetValue("run",runNum);
    tm->SetValue("event",eventNum);
    tm->SetValue("lumi",lumiNum);    

    float dR = 0.;
    TClonesArray *tightLep;
    TClonesArray *cleanJet;
    TClonesArray *cleanTau;

    tightLep = new TClonesArray("TLorentzVector",20);
    cleanJet = new TClonesArray("TLorentzVector",20);
    cleanTau = new TClonesArray("TLorentzVector",20);

    std::vector<bool>  jetMonojetId_clean;
    jetMonojetId_clean.clear();
    std::vector<bool>  jetMonojetIdLoose_clean;
    jetMonojetIdLoose_clean.clear();
    //std::vector<float> jetPuId_clean; 
    //jetPuId_clean.clear();

    std::vector<float>  tauId_clean;
    tauId_clean.clear();
    std::vector<float>  tauIso_clean;
    tauIso_clean.clear();

    n_tightlep = 0;

    // ********* Leptons ********** //
    for(int lepton = 0; lepton < lepP4->GetEntries(); lepton++){
        TLorentzVector* Lepton = (TLorentzVector*) lepP4->At(lepton);
        // check if this is a tight lep, and check the overlap

        //iso_1 = divide(input_tree.lepIso[0],input_tree.lepP4[0].Pt())
        //if (input_tree.lepTightId[0]==0 or iso_1 > 0.12): continue

        if (Lepton->Pt() > 20. && (*lepTightId)[lepton] == 1){
            n_tightlep +=1;
            new ( (*tightLep)[tightLep->GetEntriesFast()]) TLorentzVector(Lepton->Px(), Lepton->Py(), Lepton->Pz(), Lepton->Energy());            
            
            //FILL FAKEMET
            
            //check overlap with jets
            for(int j = 0; j < jetP4->GetEntries(); j++){
                TLorentzVector* Jet = (TLorentzVector*) jetP4->At(j);
                dR = deltaR(Lepton,Jet);
                if (dR > dR_cut) {
                    new ( (*cleanJet)[cleanJet->GetEntriesFast()]) TLorentzVector(Jet->Px(), Jet->Py(), Jet->Pz(), Jet->Energy());
                    jetMonojetId_clean.push_back((*jetMonojetId)[j]);
                    jetMonojetIdLoose_clean.push_back((*jetMonojetIdLoose)[j]);
                    //jetPuId_clean.push_back((*jetPuId)[j]);
                }
            }

            //check overlap with taus
            for(int tau = 0; tau < tauP4->GetEntries(); tau++){
                TLorentzVector* Tau = (TLorentzVector*) tauP4->At(tau);
                dR = deltaR(Lepton,Tau);
                if (dR > dR_cut) new ( (*cleanTau)[cleanTau->GetEntriesFast()]) TLorentzVector(Tau->Px(), Tau->Py(), Tau->Pz(), Tau->Energy());
                tauId_clean.push_back((*tauId)[tau]);
                tauIso_clean.push_back((*tauIso)[tau]);
            } // tau overlap
        } // tight lepton selection
    }//lepton loop

    bntightlep->Fill();

    // Z Selection
    TLorentzVector Z;
    if(lepP4->GetEntries() == 2 && n_tightlep > 0){
        if (((*lepPdgId)[0]+(*lepPdgId)[1])==0 ){
            Z = *((TLorentzVector*)((*lepP4)[0])) + *((TLorentzVector*)((*lepP4)[1])); 
        }
    }    

    //// W Selection                                                                         
    //if(lepP4->GetEntries() == 1 && n_tightlep == 1){
    //    MT = input_tree.lepP4[0] + metP4;
    //}
    

    //std::cout << "tightLep PT: " << ((TLorentzVector*)((*tightLep)[0]))->Pt()   << std::endl;

    std::cout << "Tight Lepton count: " << tightLep->GetEntries() << std::endl;
    std::cout << "Clean Jet count: " << cleanJet->GetEntries() << std::endl;
    std::cout << "Clean Tau count: " << cleanTau->GetEntries() << std::endl;

    // ********* Jets ********** //
    for(int jet = 0; jet < jetP4->GetEntries(); jet++){
        TLorentzVector* Jet = (TLorentzVector*) jetP4->At(jet);
        //cout << (*jetMonojetId)[0] <<endl;
        //cout << Jet->Pt()<<endl;
    }
    
    // ********* Met ********** //
    // Here try to save all possible met variables
    // and the recoil vectors (for Z and Photon)
      
    TLorentzVector Recoil(-9999.,-9999.,-9999.,-9999);

    if(Z.Pt() > 0){
        Recoil = *((TLorentzVector*)((*metP4)[0])) + Z;
        Recoil.RotateZ(TMath::Pi());
        Recoil.RotateZ(-Z.Phi());
        if (Z.Phi() > TMath::Pi())  uPar = Recoil.Px() - Z.Pt() ;
        else uPar = Recoil.Px() + Z.Pt();
        uPerp = Recoil.Py(); 
    }
    bUPar->Fill();
    bUPerp->Fill();
   
    // Decide on the type of the event and fill the
    // type tree

    int type_event = -1;
    
    // forcing all regions to be orthogonal wrt to each other
    if (((TLorentzVector*)((*metP4)[0]))->Pt() > 100. && 
        jetP4->GetEntries() > 0 && lepP4->GetEntries() == 0) type_event=0;
    if (lepP4->GetEntries() == 1 && (*lepTightId)[0] == 1) type_event=1;
    if (lepP4->GetEntries() == 2 && ((*lepTightId)[0] == 1 || (*lepTightId)[1] == 1 )) type_event=2;
    
    tm->SetValue("event_type",type_event);
    
    // Now replace all the needed collections based
    // on the type
    
    if (type_event ==1 || type_event==2){
        jetP4 = cleanJet;
        tauP4 = cleanTau;
        *jetMonojetId = jetMonojetId_clean;
        *jetMonojetIdLoose = jetMonojetIdLoose_clean;
        //*jetPuId = jetPuId_clean;
        *tauId = tauId_clean;
        *tauIso = tauIso_clean;
    }
    
    
    // skim and fill both trees;
    if(((TLorentzVector*)((*metP4)[0]))->Pt() > 100.){
        tm ->TreeFill();
        eventstree->Fill();
    }

    return kTRUE;
}

void monojet::SlaveTerminate()
{
   // The SlaveTerminate() function is called after all entries or objects
   // have been processed. When running with PROOF SlaveTerminate() is called
   // on each slave server.

}

void monojet::Terminate()
{
   // The Terminate() function is the last function to be called during
   // a query. It always runs on the client, it can be used to present
   // the results graphically or save the results to file.

    histoFile->cd();
    clonetree->Write();
    tm->TreeWrite();
    eventstree->Write();
    histoFile->Close();
}

float monojet::deltaPhi(float phi1, float phi2){
    float PHI = TMath::Abs(phi1-phi2);
    if (PHI <= 3.14159265)
        return PHI;
    else
        return 2*3.14159265-PHI;
}

float monojet::deltaR(TLorentzVector *a, TLorentzVector *b){
    return TMath::Sqrt( (a->Eta() - b->Eta()) * (a->Eta() - b->Eta()) + ( deltaPhi(a->Phi(),b->Phi()) ) * ( deltaPhi(a->Phi(),b->Phi()) ) );
}
