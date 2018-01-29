def sistriplayout(i, p, *rows): i["SiStrip/Layouts/" + p] = DQMItem(layout=rows)

sistriplayout(dqmitems, "00 - SiStrip ReportSummary",
 [{ 'path': "SiStrip/MechanicalView/detFractionReportMap",
    'description': "Fraction of Good Detector Modules plotted in different parts of the Tracker - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "no" }},
  { 'path': "SiStrip/MechanicalView/sToNReportMap",
    'description': "Accepted S/N Ratios in different parts of the Tracker. The values are 1 if the ratio is within the accepted range otherwise it is 0  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}],
 [{ 'path': "SiStrip/EventInfo/reportSummaryMap",
    'description': "Overall Report Summary where detector fraction and S/N flags are combined together -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "no" }}])
sistriplayout(dqmitems, "01 - FED-Detected Errors Summary",
 [{ 'path': "SiStrip/ReadoutView/FED/nFEDErrors",
    'description': "# of FEDs with any FED level error per event - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a>"}],
 [{ 'path': "SiStrip/ReadoutView/Fiber/nBadActiveChannelStatusBits",
    'description': "# of active channels with bad status bits per event - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a>"}])
sistriplayout(dqmitems, "02 - FED-Detected Errors",
 [{ 'path': "SiStrip/ReadoutView/Fiber/VsId/BadActiveChannelStatusBits",
  'description': "FED IDs having connected channels, with a detected tickmark, with APV/Link errors - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
  { 'path': "SiStrip/ReadoutView/Fiber/VsId/BadChannelStatusBits",
  'description': "FED IDs having connected channels with APV/Link Errors - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
  { 'path': "SiStrip/ReadoutView/FED/VsId/AnyFEDErrors",
  'description': "FED IDs having any FED level error - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
 [{ 'path': "SiStrip/ReadoutView/Fiber/nUnlocked",
    'description': "Number of connected channels per event being without a detected tickmark - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
  { 'path': "SiStrip/ReadoutView/Fiber/nOutOfSync",
    'description': "Number of connected channels per event being out-of-sync - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
  { 'path': "SiStrip/ReadoutView/APV/nAPVAddressError",
    'description': "Number of connected APVs per event having wrong pipeline address tickmark - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])
sistriplayout(dqmitems, "03 - # of Cluster Trend",
  [{ 'path': "SiStrip/MechanicalView/TIB/TotalNumberOfClusterProfile__TIB",
     'description': "Total # of Clusters in TIB with event time in Seconds  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TOB/TotalNumberOfClusterProfile__TOB",
     'description': "Total # of Clusters in TOB with event time in Seconds  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
  [{ 'path': "SiStrip/MechanicalView/TID/MINUS/TotalNumberOfClusterProfile__TID__MINUS",
     'description': "Total # of Clusters in TID -ve side with event time in Seconds  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TID/PLUS/TotalNumberOfClusterProfile__TID__PLUS",
     'description': "Total # of Clusters in TID +ve side with event time in Seconds  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
  [{  'path':"SiStrip/MechanicalView/TEC/MINUS/TotalNumberOfClusterProfile__TEC__MINUS",
     'description': "Total # of Clusters in TEC -ve side with event time in Seconds  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   {  'path':"SiStrip/MechanicalView/TEC/PLUS/TotalNumberOfClusterProfile__TEC__PLUS",
     'description': "Total # of Clusters in TEC +ve side with event time in Seconds  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])
sistriplayout(dqmitems, "04 - OnTrackCluster (StoN)",
  [{ 'path': "SiStrip/MechanicalView/TIB/Summary_ClusterStoNCorr_OnTrack__TIB",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TIB  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
   { 'path': "SiStrip/MechanicalView/TOB/Summary_ClusterStoNCorr_OnTrack__TOB",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TOB  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}],
  [{ 'path': "SiStrip/MechanicalView/TID/MINUS/Summary_ClusterStoNCorr_OnTrack__TID__MINUS",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TID -ve side  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
   { 'path': "SiStrip/MechanicalView/TID/PLUS/Summary_ClusterStoNCorr_OnTrack__TID__PLUS",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TID +ve side  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}],
  [{ 'path':"SiStrip/MechanicalView/TEC/MINUS/Summary_ClusterStoNCorr_OnTrack__TEC__MINUS",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TEC -ve side - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
   { 'path':"SiStrip/MechanicalView/TEC/PLUS/Summary_ClusterStoNCorr_OnTrack__TEC__PLUS",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TEC +ve side - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}])
sistriplayout(dqmitems, "05 - OffTrackCluster (Total Number)",
  [{ 'path': "SiStrip/MechanicalView/TIB/Summary_TotalNumberOfClusters_OffTrack__TIB",
     'description': "Total Number of Off-Track clusters in TIB  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
   { 'path': "SiStrip/MechanicalView/TOB/Summary_TotalNumberOfClusters_OffTrack__TOB",
     'description': "Total Number of Off-Track clusters in TOB  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}],
  [{ 'path': "SiStrip/MechanicalView/TID/MINUS/Summary_TotalNumberOfClusters_OffTrack__TID__MINUS",
     'description': "Total Number of Off-Track clusters in TID -ve side - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
   { 'path': "SiStrip/MechanicalView/TID/PLUS/Summary_TotalNumberOfClusters_OffTrack__TID__PLUS",
     'description': "Total Number of Off-Track clusters in TID +ve side - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}],
  [{ 'path':"SiStrip/MechanicalView/TEC/MINUS/Summary_TotalNumberOfClusters_OffTrack__TEC__MINUS",
     'description': "TotalNumberOf Off-Track clusters in TEC -ve side - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
   { 'path':"SiStrip/MechanicalView/TEC/PLUS/Summary_TotalNumberOfClusters_OffTrack__TEC__PLUS",
     'description': "TotalNumberOf Off-Track clusters in TEC +ve side - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}])

sistriplayout(dqmitems, "06a - FED Errors vs FED ID",
 [{ 'path': "SiStrip/ReadoutView/FEDErrorsVsId",
    'description': "Type of FED errors vs FED ID",
    'draw': {'withref': "no" }}])

sistriplayout(dqmitems, "06b - Detailed FED-Detected Errors",
 [{ 'path': "SiStrip/ReadoutView/FED/VsId/AnyDAQProblems",
    'description': "FED IDs having DAQ problem - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
  { 'path': "SiStrip/ReadoutView/FED/VsId/CorruptBuffers",
    'description': "FED IDs having corrupt FED buffers - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
  { 'path': "SiStrip/ReadoutView/FE/VsId/AnyFEProblems",
    'description': "FED IDs having overflowed, missing or with bad majority address FE units - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
 [{'path': "SiStrip/ReadoutView/FedIdVsApvId",
   'description': "APV error: FED ID vs APV ID - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])

sistriplayout(dqmitems, "07 - OnTrackClusters(Total Number)",
  [{ 'path': "SiStrip/MechanicalView/TIB/Summary_TotalNumberOfClusters_OnTrack__TIB",
     'description': "Total Number of On-Track clusters in TIB  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
   { 'path': "SiStrip/MechanicalView/TOB/Summary_TotalNumberOfClusters_OnTrack__TOB",
     'description': "Total Number of On-Track clusters in TOB  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}],
  [{ 'path': "SiStrip/MechanicalView/TID/MINUS/Summary_TotalNumberOfClusters_OnTrack__TID__MINUS",
     'description': "Total Number of On-Track clusters in TID -ve side - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
   { 'path': "SiStrip/MechanicalView/TID/PLUS/Summary_TotalNumberOfClusters_OnTrack__TID__PLUS",
     'description': "Total Number of On-Track clusters in TID +ve side - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}],
  [{ 'path':"SiStrip/MechanicalView/TEC/MINUS/Summary_TotalNumberOfClusters_OnTrack__TEC__MINUS",
     'description': "TotalNumberOf On-Track clusters in TEC -ve side - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
   { 'path':"SiStrip/MechanicalView/TEC/PLUS/Summary_TotalNumberOfClusters_OnTrack__TEC__PLUS",
     'description': "TotalNumberOf On-Track clusters in TEC +ve side - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}])
sistriplayout(dqmitems, "08 - OffTrackCluster (Charge)",
  [{ 'path': "SiStrip/MechanicalView/TIB/Summary_ClusterCharge_OffTrack__TIB",
     'description': "Charge for Off-Track clusters in TIB - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes"}},
   { 'path': "SiStrip/MechanicalView/TOB/Summary_ClusterCharge_OffTrack__TOB",
     'description': "Charge for Off-Track clusters in TOB - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes"}}],
  [{ 'path': "SiStrip/MechanicalView/TID/MINUS/Summary_ClusterCharge_OffTrack__TID__MINUS",
     'description': "Charge for Off-Track clusters in TID -ve side - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes"}},
   { 'path': "SiStrip/MechanicalView/TID/PLUS/Summary_ClusterCharge_OffTrack__TID__PLUS",
     'description': "Charge for Off-Track clusters in TID +ve side - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes"}}],
  [{ 'path':"SiStrip/MechanicalView/TEC/MINUS/Summary_ClusterCharge_OffTrack__TEC__MINUS",
     'description': "Charge for Off-Track clusters in TEC -ve - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes"}},
   { 'path':"SiStrip/MechanicalView/TEC/PLUS/Summary_ClusterCharge_OffTrack__TEC__PLUS",
     'description': "Charge for Off-Track clusters in TEC +ve - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes"}}])
sistriplayout(dqmitems, "09 - TIB Summary",
  [{ 'path': "SiStrip/MechanicalView/TIB/layer_1/Summary_ClusterStoNCorr__OnTrack__TIB__layer__1",
     'description': "Corrected S/N ratio for TIB Layer #1 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TIB/layer_2/Summary_ClusterStoNCorr__OnTrack__TIB__layer__2",
     'description': "Corrected S/N ratio for TIB Layer #2 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
  [{ 'path': "SiStrip/MechanicalView/TIB/layer_3/Summary_ClusterStoNCorr__OnTrack__TIB__layer__3",
     'description': "Corrected S/N ratio for TIB Layer #3 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TIB/layer_4/Summary_ClusterStoNCorr__OnTrack__TIB__layer__4",
     'description': "Corrected S/N ratio for TIB Layer #4 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])
sistriplayout(dqmitems, "10 - TID+ Summary",
  [{ 'path': "SiStrip/MechanicalView/TID/PLUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__1",
     'description': "Corrected S/N ratio for TID+ Wheel #1 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TID/PLUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__2",
     'description': "Corrected S/N ratio for TID+ Wheel #2 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
  [{ 'path': "SiStrip/MechanicalView/TID/PLUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__PLUS__wheel__3",
     'description': "Corrected S/N ratio for TID+ Wheel #3 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])
sistriplayout(dqmitems, "11 - TID- Summary",
  [{ 'path': "SiStrip/MechanicalView/TID/MINUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__1",
     'description': "Corrected S/N ratio for TID- Wheel #1 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TID/MINUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__2",
     'description': "Corrected S/N ratio for TID- Wheel #2 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
  [{ 'path': "SiStrip/MechanicalView/TID/MINUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__MINUS__wheel__3",
     'description': "Corrected S/N ratio for TID- Wheel #3 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])
sistriplayout(dqmitems, "12 - TOB Summary",
  [{ 'path': "SiStrip/MechanicalView/TOB/layer_1/Summary_ClusterStoNCorr__OnTrack__TOB__layer__1",
     'description': "Corrected S/N ratio for TOB Layer #1 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TOB/layer_2/Summary_ClusterStoNCorr__OnTrack__TOB__layer__2",
     'description': "Corrected S/N ratio for TOB Layer #2 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TOB/layer_3/Summary_ClusterStoNCorr__OnTrack__TOB__layer__3",
     'description': "Corrected S/N ratio for TOB Layer #3 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
  [{ 'path': "SiStrip/MechanicalView/TOB/layer_4/Summary_ClusterStoNCorr__OnTrack__TOB__layer__4",
     'description': "Corrected S/N ratio for TOB Layer #4 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TOB/layer_5/Summary_ClusterStoNCorr__OnTrack__TOB__layer__5",
     'description': "Corrected S/N ratio for TOB Layer #5 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TOB/layer_6/Summary_ClusterStoNCorr__OnTrack__TOB__layer__6",
     'description': "Corrected S/N ratio for TOB Layer #6 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])
sistriplayout(dqmitems, "13 - TEC+ Summary",
  [{ 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__1",
     'description': "Corrected S/N ratio for TEC+ Wheel #1 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__2",
     'description': "Corrected S/N ratio for TEC+ Wheel #2 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__3",
     'description': "Corrected S/N ratio for TEC+ Wheel #3 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__4",
     'description': "Corrected S/N ratio for TEC+ Wheel #4 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__5",
     'description': "Corrected S/N ratio for TEC+ Wheel #5 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
  [{ 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__6",
     'description': "Corrected S/N ratio for TEC+ Wheel #6 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__7",
     'description': "Corrected S/N ratio for TEC+ Wheel #7 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__8",
     'description': "Corrected S/N ratio for TEC+ Wheel #8 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__PLUS__wheel__9",
     'description': "Corrected S/N ratio for TEC+ Wheel #9 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])
sistriplayout(dqmitems, "14 - TEC- Summary",
   [{ 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__1",
     'description': "Corrected S/N ratio for TEC- Wheel #1 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__2",
     'description': "Corrected S/N ratio for TEC- Wheel #2 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__3",
     'description': "Corrected S/N ratio for TEC- Wheel #3 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__4",
     'description': "Corrected S/N ratio for TEC- Wheel #4 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__5",
     'description': "Corrected S/N ratio for TEC- Wheel #5 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
  [{ 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__6",
     'description': "Corrected S/N ratio for TEC- Wheel #6 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__7",
     'description': "Corrected S/N ratio for TEC- Wheel #7 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__8",
     'description': "Corrected S/N ratio for TEC- Wheel #8 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__MINUS__wheel__9",
     'description': "Corrected S/N ratio for TEC- Wheel #9 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])
sistriplayout(dqmitems, "15 - TIB Cluster TkHMap",
  [{ 'path': "SiStrip/MechanicalView/TIB/layer_1/TkHMap_NumberOfOnTrackCluster_TIB_L1",
     'description': "Cluster TkHistoMap  in TIB Layer #1"},
   { 'path': "SiStrip/MechanicalView/TIB/layer_2/TkHMap_NumberOfOnTrackCluster_TIB_L2",
     'description': "Cluster TkHistoMap  in TIB Layer #2"}],
  [{ 'path': "SiStrip/MechanicalView/TIB/layer_3/TkHMap_NumberOfOnTrackCluster_TIB_L3",
     'description': "Cluster TkHistoMap  in TIB Layer #3"},
   { 'path': "SiStrip/MechanicalView/TIB/layer_4/TkHMap_NumberOfOnTrackCluster_TIB_L4",
     'description': "Cluster TkHistoMap  in TIB Layer #4"}])
sistriplayout(dqmitems, "16 - TOB Cluster TkHMap",
  [{ 'path': "SiStrip/MechanicalView/TOB/layer_1/TkHMap_NumberOfOnTrackCluster_TOB_L1",
     'description': "Cluster TkHistoMap  in TOB Layer #1"},
   { 'path': "SiStrip/MechanicalView/TOB/layer_2/TkHMap_NumberOfOnTrackCluster_TOB_L2",
     'description': "Cluster TkHistoMap  in TOB Layer #2"},
   { 'path': "SiStrip/MechanicalView/TOB/layer_3/TkHMap_NumberOfOnTrackCluster_TOB_L3",
     'description': "Cluster TkHistoMap  in TOB Layer #3"}],
  [{ 'path': "SiStrip/MechanicalView/TOB/layer_4/TkHMap_NumberOfOnTrackCluster_TOB_L4",
     'description': "Cluster TkHistoMap  in TOB Layer #4"},
   { 'path': "SiStrip/MechanicalView/TOB/layer_5/TkHMap_NumberOfOnTrackCluster_TOB_L5",
     'description': "Cluster TkHistoMap  in TOB Layer #5"},
   { 'path': "SiStrip/MechanicalView/TOB/layer_6/TkHMap_NumberOfOnTrackCluster_TOB_L6",
     'description': "Cluster TkHistoMap  in TOB Layer #6"}])
sistriplayout(dqmitems, "17 - TID+ Cluster TkHMap",
  [{ 'path': "SiStrip/MechanicalView/TID/PLUS/wheel_1/TkHMap_NumberOfOnTrackCluster_TIDP_D1",
     'description': "Cluster TkHistoMap s in TID+ Wheel #1"},
   { 'path': "SiStrip/MechanicalView/TID/PLUS/wheel_2/TkHMap_NumberOfOnTrackCluster_TIDP_D2",
     'description': "Cluster TkHistoMap s in TID+ Wheel #2"},
   { 'path': "SiStrip/MechanicalView/TID/PLUS/wheel_3/TkHMap_NumberOfOnTrackCluster_TIDP_D3",
     'description': "Cluster TkHistoMap s in TID+ Wheel #3 "}])
sistriplayout(dqmitems, "18 - TID- Cluster TkHMap",
  [{ 'path': "SiStrip/MechanicalView/TID/MINUS/wheel_1/TkHMap_NumberOfOnTrackCluster_TIDM_D1",
     'description': "Cluster TkHistoMap s in TID- Wheel #1"},
   { 'path': "SiStrip/MechanicalView/TID/MINUS/wheel_2/TkHMap_NumberOfOnTrackCluster_TIDM_D2",
     'description': "Cluster TkHistoMap s in TID- Wheel #2"},
   { 'path': "SiStrip/MechanicalView/TID/MINUS/wheel_3/TkHMap_NumberOfOnTrackCluster_TIDM_D3",
     'description': "Cluster TkHistoMap s in TID- Wheel #3 "}])
sistriplayout(dqmitems, "19 - TEC+ Cluster TkHMap",
  [{ 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_1/TkHMap_NumberOfOnTrackCluster_TECP_W1",
     'description': "Cluster TkHistoMap  in TEC+ Wheel #1"},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_2/TkHMap_NumberOfOnTrackCluster_TECP_W2",
     'description': "Cluster TkHistoMap  in TEC+ Wheel #2"},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_3/TkHMap_NumberOfOnTrackCluster_TECP_W3",
     'description': "Cluster TkHistoMap  in TEC+ Wheel #3"}],
  [{ 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_4/TkHMap_NumberOfOnTrackCluster_TECP_W4",
     'description': "Cluster TkHistoMap  in TEC+ Wheel #4"},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_5/TkHMap_NumberOfOnTrackCluster_TECP_W5",
     'description': "Cluster TkHistoMap  in TEC+ Wheel #5"},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_6/TkHMap_NumberOfOnTrackCluster_TECP_W6",
     'description': "Cluster TkHistoMap  in TEC+ Wheel #6"}],
  [{ 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_7/TkHMap_NumberOfOnTrackCluster_TECP_W7",
     'description': "Cluster TkHistoMap  in TEC+ Wheel #7"},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_8/TkHMap_NumberOfOnTrackCluster_TECP_W8",
     'description': "Cluster TkHistoMap  in TEC+ Wheel #8"},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_9/TkHMap_NumberOfOnTrackCluster_TECP_W9",
     'description': "Cluster TkHistoMap  in TEC+ Wheel #9"}])
sistriplayout(dqmitems, "20 - TEC- Cluster TkHMap",
  [{ 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_1/TkHMap_NumberOfOnTrackCluster_TECM_W1",
     'description': "Cluster TkHistoMap  in TEC- Wheel #1"},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_2/TkHMap_NumberOfOnTrackCluster_TECM_W2",
     'description': "Cluster TkHistoMap  in TEC- Wheel #2"},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_3/TkHMap_NumberOfOnTrackCluster_TECM_W3",
     'description': "Cluster TkHistoMap  in TEC- Wheel #3"}],
  [{ 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_4/TkHMap_NumberOfOnTrackCluster_TECM_W4",
     'description': "Cluster TkHistoMap  in TEC- Wheel #4"},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_5/TkHMap_NumberOfOnTrackCluster_TECM_W5",
     'description': "Cluster TkHistoMap  in TEC- Wheel #5"},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_6/TkHMap_NumberOfOnTrackCluster_TECM_W6",
     'description': "Cluster TkHistoMap  in TEC- Wheel #6"}],
  [{ 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_7/TkHMap_NumberOfOnTrackCluster_TECM_W7",
     'description': "Cluster TkHistoMap  in TEC- Wheel #7"},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_8/TkHMap_NumberOfOnTrackCluster_TECM_W8",
     'description': "Cluster TkHistoMap  in TEC- Wheel #8"},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_9/TkHMap_NumberOfOnTrackCluster_TECM_W9",
     'description': "Cluster TkHistoMap  in TEC- Wheel #9"}])
sistriplayout(dqmitems, "21 - TIB Residuals",
  [{ 'path': "SiStrip/MechanicalView/TIB/layer_1/HitResiduals_TIB__Layer__1",
     'description': "Hit Residual in TIB Layer #1"},
   { 'path': "SiStrip/MechanicalView/TIB/layer_2/HitResiduals_TIB__Layer__2",
     'description': "Hit Residual in TIB Layer #2"}],
  [{ 'path': "SiStrip/MechanicalView/TIB/layer_3/HitResiduals_TIB__Layer__3",
     'description': "Hit Residual in TIB Layer #3"},
   { 'path': "SiStrip/MechanicalView/TIB/layer_4/HitResiduals_TIB__Layer__4",
     'description': "Hit Residual in TIB Layer #4"}])
sistriplayout(dqmitems, "22 - TOB Residuals",
  [{ 'path': "SiStrip/MechanicalView/TOB/layer_1/HitResiduals_TOB__Layer__1",
     'description': "Hit Residual in TOB Layer #1"},
   { 'path': "SiStrip/MechanicalView/TOB/layer_2/HitResiduals_TOB__Layer__2",
     'description': "Hit Residual in TOB Layer #2"},
   { 'path': "SiStrip/MechanicalView/TOB/layer_3/HitResiduals_TOB__Layer__3",
     'description': "Hit Residual in TOB Layer #3"}],
  [{ 'path': "SiStrip/MechanicalView/TOB/layer_4/HitResiduals_TOB__Layer__4",
     'description': "Hit Residual in TOB Layer #4"},
   { 'path': "SiStrip/MechanicalView/TOB/layer_5/HitResiduals_TOB__Layer__5",
     'description': "Hit Residual in TOB Layer #5"},
   { 'path': "SiStrip/MechanicalView/TOB/layer_6/HitResiduals_TOB__Layer__6",
     'description': "Hit Residual in TOB Layer #6"}])
sistriplayout(dqmitems, "23 - TID+ Residuals",
  [{ 'path': "SiStrip/MechanicalView/TID/PLUS/wheel_1/HitResiduals_TID__wheel__1",
     'description': "Hit Residuals in TID+ Wheel #1"},
   { 'path': "SiStrip/MechanicalView/TID/PLUS/wheel_2/HitResiduals_TID__wheel__2",
     'description': "Hit Residuals in TID+ Wheel #2"},
   { 'path': "SiStrip/MechanicalView/TID/PLUS/wheel_3/HitResiduals_TID__wheel__3",
     'description': "Hit Residuals in TID+ Wheel #3 "}])
sistriplayout(dqmitems, "24 - TID- Residuals",
  [{ 'path': "SiStrip/MechanicalView/TID/MINUS/wheel_1/HitResiduals_TID__wheel__1",
     'description': "Hit Residuals in TID- Wheel #1"},
   { 'path': "SiStrip/MechanicalView/TID/MINUS/wheel_2/HitResiduals_TID__wheel__2",
     'description': "Hit Residuals in TID- Wheel #2"},
   { 'path': "SiStrip/MechanicalView/TID/MINUS/wheel_3/HitResiduals_TID__wheel__3",
     'description': "Hit Residuals in TID- Wheel #3 "}])
sistriplayout(dqmitems, "25 - TEC+ Residual",
  [{ 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_1/HitResiduals_TEC__wheel__1",
     'description': "Hit Residual in TEC+ Wheel #1"},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_2/HitResiduals_TEC__wheel__2",
     'description': "Hit Residual in TEC+ Wheel #2"},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_3/HitResiduals_TEC__wheel__3",
     'description': "Hit Residual in TEC+ Wheel #3"}],
  [{ 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_4/HitResiduals_TEC__wheel__4",
     'description': "Hit Residual in TEC+ Wheel #4"},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_5/HitResiduals_TEC__wheel__5",
     'description': "Hit Residual in TEC+ Wheel #5"},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_6/HitResiduals_TEC__wheel__6",
     'description': "Hit Residual in TEC+ Wheel #6"}],
  [{ 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_7/HitResiduals_TEC__wheel__7",
     'description': "Hit Residual in TEC+ Wheel #7"},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_8/HitResiduals_TEC__wheel__8",
     'description': "Hit Residual in TEC+ Wheel #8"},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_9/HitResiduals_TEC__wheel__9",
     'description': "Hit Residual in TEC+ Wheel #9"}])
sistriplayout(dqmitems, "26 - TEC- Residual",
  [{ 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_1/HitResiduals_TEC__wheel__1",
     'description': "Hit Residual in TEC- Wheel #1"},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_2/HitResiduals_TEC__wheel__2",
     'description': "Hit Residual in TEC- Wheel #2"},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_3/HitResiduals_TEC__wheel__3",
     'description': "Hit Residual in TEC- Wheel #3"}],
  [{ 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_4/HitResiduals_TEC__wheel__4",
     'description': "Hit Residual in TEC- Wheel #4"},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_5/HitResiduals_TEC__wheel__5",
     'description': "Hit Residual in TEC- Wheel #5"},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_6/HitResiduals_TEC__wheel__6",
     'description': "Hit Residual in TEC- Wheel #6"}],
  [{ 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_7/HitResiduals_TEC__wheel__7",
     'description': "Hit Residual in TEC- Wheel #7"},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_8/HitResiduals_TEC__wheel__8",
     'description': "Hit Residual in TEC- Wheel #8"},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_9/HitResiduals_TEC__wheel__9",
     'description': "Hit Residual in TEC- Wheel #9"}])
sistriplayout(dqmitems, "27 - APVe Timing",
  [{ 'path': "SiStrip/ReadoutView/FE/APVe/FETimeDiffTECB",
     'description': "Timing difference FE - TEC-"},
   { 'path': "SiStrip/ReadoutView/FE/APVe/FETimeDiffTECF",
     'description': "Timing difference FE - TEC+"}],
  [{ 'path': "SiStrip/ReadoutView/FE/APVe/FETimeDiffTIB",
     'description': "Timing difference FE - TIB"},
   { 'path': "SiStrip/ReadoutView/FE/APVe/FETimeDiffTOB",
     'description': "Timing difference FE - TOB"}])
sistriplayout(dqmitems, "28 Strip Clusters Vs Pixel Clusters",
 [{ 'path': "SiStrip/MechanicalView/StripClusVsPixClus",
     'description': "Total number of clusters in Strip versuls the total number of clusters in Pixels", 'draw': { 'withref': "no" }}])
#  LocalWords:  TotalNumberOfClusterProfile
