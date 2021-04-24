import ROOT

# global parameters
intLumi        = 150000000. #in pb-1
ana_tex        = "Z #rightarrow q#bar{q}"
delphesVersion = "3.4.2"
energy         = 91.0
collider       = "FCC-ee"
inputDir       = "/eos/experiment/fcc/ee/analyses/case-studies/flavour/Bc2TauNu/flatNtuples/21042021/Analysis_stage2/"
inputDir       = "/eos/experiment/fcc/ee/analyses/case-studies/flavour/Bc2TauNu/flatNtuples/21042021/Training_4stage2/"
formats        = ['png','pdf']
yaxis          = ['lin','log']
stacksig       = ['stack','nostack']
outdir         = '/eos/home-h/helsens/www/FCC/ee/flavour/Bc2TauNu/22042021/'
variables = [ "EVT_CandMass",
              ##"EVT_minRhoMass","EVT_maxRhoMass",
              "EVT_ThrustEmin_E","EVT_ThrustEmax_E",
              "EVT_ThrustEmin_Echarged", "EVT_ThrustEmax_Echarged",
              "EVT_ThrustEmin_Eneutral", "EVT_ThrustEmax_Eneutral",
              "EVT_ThrustEmin_Ncharged", "EVT_ThrustEmax_Ncharged",
              "EVT_ThrustEmin_Nneutral", "EVT_ThrustEmax_Nneutral",
              "EVT_ThrustEmin_NDV",      "EVT_ThrustEmax_NDV",
              "EVT_ThrustDiff_E",
              "EVT_ThrustDiff_Echarged","EVT_ThrustDiff_Eneutral",
              "EVT_ThrustDiff_Ncharged","EVT_ThrustDiff_Nneutral",
              "EVT_CandVtxFD",
              "EVT_CandAngleThrust",
              "EVT_CandAngleThrust_2",

              ]

scaleSig=100.
###Dictonnary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['Flavour']   = ["sel0","sel1"]#,"sel2","sel3","sel4"]

extralabel = {}
extralabel['sel0'] = "Selection: MVA1>0.8, MVA2>0.8"
extralabel['sel1'] = "Selection: MVA1>0.9, MVA2>0.9"
extralabel['sel2'] = "Selection: MVA1>0.95, MVA2>0.95"
extralabel['sel3'] = "Selection: MVA1>0.98, MVA2>0.98"
extralabel['sel4'] = "Selection: MVA1>0.99, MVA2>0.99"

colors = {}
colors['Z_flavour'] = ROOT.kRed
colors['Z_bb'] = ROOT.kBlue+1
colors['Z_cc'] = ROOT.kGreen+1
colors['Z_uds'] = ROOT.kGreen+2
colors['Z_Bu'] = ROOT.kGreen+3

plots = {}
plots['Flavour'] = {'signal':{'Z_flavour':['p8_ee_Zbb_ecm91_EvtGen_Bc2TauNuTAUHADNU']},
                    'backgrounds':{'Z_bb':['p8_ee_Zbb_ecm91'],
                                   'Z_cc':['p8_ee_Zcc_ecm91'],
                                   'Z_uds':['p8_ee_Zuds_ecm91'],
                                   'Z_Bu':['p8_ee_Zbb_ecm91_EvtGen_Bu2TauNuTAUHADNU']
                                   }
           }

legend = {}
legend['Z_flavour'] = 'B_{c}#rightarrow #tau#nu (#tau#rightarrow 3#pi)'
legend['Z_bb'] = 'Z#rightarrow b#bar{b}'
legend['Z_cc'] = 'Z#rightarrow c#bar{c}'
legend['Z_uds'] = 'Z#rightarrow q#bar{q}'
legend['Z_Bu'] = 'B_{u}#rightarrow #tau#nu (#tau#rightarrow 3#pi)'




