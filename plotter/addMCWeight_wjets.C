
void addMCWeight_wjets(TString filename, TString treename)
{

    //Processing addMCWeight_data.C("monojet_Zee.root","data_Zee")...
    //    In file included from input_line_24:1:
    //    /afs/cern.ch/work/z/zdemirag/work/frozen_monojet/monojet/plotter/./addMCWeight_data.C:16:43: error: use of undeclared identifier 'treeDir'
    //    cout << "Could not find tree " << treeDir << "/" << treename << endl
 


    using namespace std;

    cout << "WJets adding MCWeight to:"<< filename << endl;

    double scale_w;
    float mcWeight;
    int npv;
    float genBos_pt;
    float leptonSF;
    float met;

    TFile *file = new TFile(filename,"UPDATE");  
    TTree *oldtree = (TTree*)file->Get(treename);

    if(oldtree==NULL)
    {
        cout << "Could not find tree " << treename << endl
             << "in file " << file->GetName() << endl;
        return;
    }
  
    oldtree->SetBranchAddress("scale_w",&scale_w);
    oldtree->SetBranchAddress("mcWeight",&mcWeight);
    oldtree->SetBranchAddress("npv",&npv);
    oldtree->SetBranchAddress("genBos_pt",&genBos_pt);
    oldtree->SetBranchAddress("leptonSF",&leptonSF);
    oldtree->SetBranchAddress("met",&met);

    double scaleMC_w = 1.0;

    TBranch *branch = oldtree->Branch("scaleMC_w",&scaleMC_w,"scaleMC_w/D");

    for(int i = 0; i < oldtree->GetEntries(); i++)
    {
        oldtree->GetEntry(i);
      
        double w_npv = ((0.0*(npv>-0.5&&npv<=0.5)+3.30418257204*(npv>0.5&&npv<=1.5)+2.59691269521*(npv>1.5&&npv<=2.5)+2.44251087681*(npv>2.5&&npv<=3.5)+2.42846225153*(npv>3.5&&npv<=4.5)+2.40062512591*(npv>4.5&&npv<=5.5)+2.30279811595*(npv>5.5&&npv<=6.5)+2.12054720297*(npv>6.5&&npv<=7.5)+1.9104708827*(npv>7.5&&npv<=8.5)+1.67904936047*(npv>8.5&&npv<=9.5)+1.43348925382*(npv>9.5&&npv<=10.5)+1.17893952713*(npv>10.5&&npv<=11.5)+0.940505177881*(npv>11.5&&npv<=12.5)+0.740901867872*(npv>12.5&&npv<=13.5)+0.56877478036*(npv>13.5&&npv<=14.5)+0.433148655714*(npv>14.5&&npv<=15.5)+0.325343558476*(npv>15.5&&npv<=16.5)+0.241688459349*(npv>16.5&&npv<=17.5)+0.180491032782*(npv>17.5&&npv<=18.5)+0.136993937378*(npv>18.5&&npv<=19.5)+0.104859480066*(npv>19.5&&npv<=20.5)+0.0768271030309*(npv>20.5&&npv<=21.5)+0.0563426184938*(npv>21.5&&npv<=22.5)+0.0454037058117*(npv>22.5&&npv<=23.5)+0.0359945616383*(npv>23.5&&npv<=24.5)+0.0286879205085*(npv>24.5&&npv<=25.5)+0.0208185595478*(npv>25.5&&npv<=26.5)+0.0170977379612*(npv>26.5&&npv<=27.5)+0.0122446391898*(npv>27.5&&npv<=28.5)+0.0148028308301*(npv>28.5&&npv<=29.5)+0.0120527550003*(npv>29.5&&npv<=30.5)+0.00402643194054*(npv>30.5&&npv<=31.5)+0.00981143754301*(npv>31.5&&npv<=32.5)+0.0*(npv>32.5&&npv<=33.5)+0.0155664899019*(npv>33.5&&npv<=34.5)+0.0*(npv>34.5&&npv<=35.5)+0.0*(npv>35.5&&npv<=36.5)+0.0*(npv>36.5&&npv<=37.5)+0.0*(npv>37.5&&npv<=38.5)+0.0*(npv>38.5&&npv<=39.5)));        

        double ewk = (0.980859240872*(genBos_pt>100.0&&genBos_pt<=150.0)+0.962118764182*(genBos_pt>150.0&&genBos_pt<=200.0)+0.944428528597*(genBos_pt>200.0&&genBos_pt<=250.0)+0.927685912907*(genBos_pt>250.0&&genBos_pt<=300.0)+0.911802238928*(genBos_pt>300.0&&genBos_pt<=350.0)+0.896700388113*(genBos_pt>350.0&&genBos_pt<=400.0)+0.875368225896*(genBos_pt>400.0&&genBos_pt<=500.0)+0.849096933047*(genBos_pt>500.0&&genBos_pt<=600.0)+0.792158791839*(genBos_pt>600.0));

        double kfactor = (1.89123123702*(genBos_pt>100.0&&genBos_pt<=150.0)+1.70414182145*(genBos_pt>150.0&&genBos_pt<=200.0)+1.60726459197*(genBos_pt>200.0&&genBos_pt<=250.0)+1.57205818769*(genBos_pt>250.0&&genBos_pt<=300.0)+1.51688539716*(genBos_pt>300.0&&genBos_pt<=350.0)+1.41090079307*(genBos_pt>350.0&&genBos_pt<=400.0)+1.30757555038*(genBos_pt>400.0&&genBos_pt<=500.0)+1.32046236765*(genBos_pt>500.0&&genBos_pt<=600.0)+1.26852513234*(genBos_pt>600.0));
        
        double w_trig = ((met < 250)*0.97 + (met >=250 && met<350)* 0.987 + (met>=350)* 1.0 );

        //std::cout << "Hi Zeynep, Lepton SF is: " << leptonSF << std::endl;

        //scaleMC_w = scale_w*mcWeight*w_npv*kfactor*ewk*leptonSF;
        //scaleMC_w = scale_w*mcWeight*w_npv*kfactor*ewk*w_trig*leptonSF;
        scaleMC_w = scale_w*mcWeight*w_npv*kfactor*ewk*w_trig;
        branch->Fill();
    }

    file->cd();
    oldtree->CloneTree()->Write(treename, TObject::kOverwrite);
    file->Close();
  
}
