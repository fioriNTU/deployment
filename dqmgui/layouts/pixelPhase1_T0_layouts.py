def pixellayout(i, p, *rows): i["PixelPhase1/Layouts/" + p] = DQMItem(layout=rows)
pixellayout(dqmitems, "000 - PixelPhase1 ReportSummary: Layer or Disk vs subdet",
   [{ 'path':  "PixelPhase1/EventInfo/reportSummaryMap",
      'description': "Summary results of qulity tests: Layer/Disk (y-axis) vs. Subdetectors (x-axis). See the PixelPhase1/Summary/ directory for more details.",
      'draw': { 'withref': "no", 'drawopts': "COLZTEXT" }}]
   )
pixellayout(dqmitems, "00a - PixelPhase1 FED Occupancy vs Lumi Sections",
            [{ 'path': "PixelPhase1/num_feddigistrend_per_Lumisection_per_FED",
               'description': "Number of digis per FED and Lumisection",
               'draw': { 'withref': "no" }}]
              )
pixellayout(dqmitems, "00b - PixelPhase1_Error_Summary",
   [{ 'path': "PixelPhase1/FED/nerrors_per_type_per_FED",
      'description': "Number of Errors of each type per FED. Channel 0 is assigned for errors where the channel number is not known.",
      'draw': { 'withref': "no" }}]
   )
pixellayout(dqmitems, "00c - PixelPhase1_Error_Summary",
   [{ 'path': "PixelPhase1/FED/errors_per_LinkInFed_per_FED",
      'description': "Total number of errors in a map of FED channels (y-axis) vs. FED (x-axis). Channel 0 is assigned for errors where the channel number is not known.",
      'draw': { 'withref': "no" }}]
   )

pixellayout(dqmitems, "01a - PixelPhase1_Event_Rate",
  [{ 'path': "PixelPhase1/Phase1_MechanicalView/eventrate_per_BX",
     'description': "Event rate per bunch crossing",
     'draw': { 'withref': "no" }}]
  )
pixellayout(dqmitems, "01b - PixelPhase1_ClusterEvent_Rate",
  [{ 'path': "PixelPhase1/Phase1_MechanicalView/clustereventrate_per_BX",
     'description': "Cluster event rate per bunch crossing",
     'draw': { 'withref': "no" }}]
  )
pixellayout(dqmitems, "01c - PixelPhase1 Cluster Size vs Cluster Eta",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/sizeyvseta_PXBarrel",
      'description': "Cluster size along the beamline in pixel length (y-axis) vs the cluster eta position in eta (x-axis)",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}]
   )

pixellayout(dqmitems, "02 - PixelPhase1_Digi_ADC_Barrel",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/num_digis_PXBarrel",
      'description': "Number of digis per event in PXBarrel",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/adc_PXBarrel",
      'description': "Adc distribution of digis per event per barrel module",
      'draw': { 'withref': "no" }}],
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/num_digis_per_Lumisection_PXBarrel",
      'description': "Mean adc value per lumisection",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/adc_per_Lumisection_PXBarrel",
      'description': "Mean adc value per lumisection",
      'draw': { 'withref': "no" }}]
   )

pixellayout(dqmitems, "03 - PixelPhase1_Digi_ADC_Endcap",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/num_digis_PXForward",
      'description': "Number of digis per event in Forward",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/adc_PXForward",
      'description': "Adc distribution of digis per event per forward module",
      'draw': { 'withref': "no" }}],
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/num_digis_per_Lumisection_PXForward",
      'description': "Mean adc value per lumisection",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/adc_per_Lumisection_PXForward",
      'description': "Mean adc value per lumisection",
      'draw': { 'withref': "no" }}]
   )

pixellayout(dqmitems, "04 - PixelPhase1_Cluster_Number",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/num_clusters_PXBarrel",
      'description': "Number of clusters per event in Barrel",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/num_clusters_PXForward",
      'description': "Number of clusters per event in Forward",
      'draw': { 'withref': "no" }}],
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/num_clusters_per_Lumisection_PXBarrel",
      'description': "Mean cluster value per lumisection in barrel",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/num_clusters_per_Lumisection_PXForward",
      'description': "Mean cluster value per lumisection in endcap",
      'draw': { 'withref': "no" }}]
   )

pixellayout(dqmitems, "05 - PixelPhase1_Cluster_Charge",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/charge_PXBarrel",
      'description': "Cluster charge in the barrel modules",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/charge_PXForward",
      'description': "Distribution of raw charge for all digis recorded in the Endcap modules - dominant peak should be around 90-100 ADC",
      'draw': { 'withref': "no" }}],
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/charge_per_Lumisection_PXBarrel",
      'description': "Mean cluster charge per lumisection in barrel",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/charge_per_Lumisection_PXForward",
      'description': "Mean cluster charge per lumisection in barrel",
      'draw': { 'withref': "no" }}]
   )

pixellayout(dqmitems, "06 - PixelPhase1_Cluster_Size",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/size_PXBarrel",
      'description': "Total cluster size in the barrel modules",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/size_PXForward",
      'description': "Total cluster size in the Endcap modules",
      'draw': { 'withref': "no" }}],
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/size_per_Lumisection_PXBarrel",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/size_per_Lumisection_PXForward",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }}]
   )

pixellayout(dqmitems, "07 - PixelPhase1_Charge_Barrel",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/charge_PXLayer_1",
      'description': "Cluster charge in layer 1 of pixel barrel",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/charge_PXLayer_2",
      'description': "Cluster charge in layer 2 of pixel barrel",
      'draw': { 'withref': "no" }}],
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/charge_PXLayer_3",
      'description': "Cluster charge in layer 3 of pixel barrel",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/charge_PXLayer_4",
      'description': "Cluster charge in layer 4 of pixel barrel",
      'draw': { 'withref': "no" }}],
   )

pixellayout(dqmitems, "08 - PixelPhase1_ADC_Barrel",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/adc_PXLayer_1",
      'description': "Distribution of raw charge for all digis recorded in layer 1 of pixel barrel - dominant peak should be around 90-100 ADC",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/adc_PXLayer_2",
      'description': "Distribution of raw charge for all digis recorded in layer 2 of pixel barrel - dominant peak should be around 90-100 ADC",
      'draw': { 'withref': "no" }}],
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/adc_PXLayer_3",
      'description': "Distribution of raw charge for all digis recorded in layer 3 of pixel barrel",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/adc_PXLayer_4",
      'description': "Distribution of raw charge for all digis recorded in layer 4 of pixel barrel",
      'draw': { 'withref': "no" }}],
   )

pixellayout(dqmitems, "09 - PixelPhase1_Digi_Barrel",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/num_digis_PXLayer_1",
      'description': "Number of Digis in layer 1 of pixel barrel",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/num_digis_PXLayer_2",
      'description': "Number of Digis in layer 2 of pixel barrel",
      'draw': { 'withref': "no" }}],
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/num_digis_PXLayer_3",
      'description': "Number of Digis in layer 3 of pixel barrel",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/num_digis_PXLayer_4",
      'description': "Number of Digis in layer 4 of pixel barrel",
      'draw': { 'withref': "no" }}],
   )

pixellayout(dqmitems, "10 - PixelPhase1_Cluster_Barrel",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/num_clusters_PXLayer_1",
      'description': "Number of clusters in layer 1 of pixel barrel",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/num_clusters_PXLayer_2",
      'description': "Number of clusters in layer 2 of pixel barrel",
      'draw': { 'withref': "no" }}],
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/num_clusters_PXLayer_3",
      'description': "Number of clusters in layer 3 of pixel barrel",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/num_clusters_PXLayer_4",
      'description': "Number of clusters in layer 4 of pixel barrel",
      'draw': { 'withref': "no" }}],
   )

pixellayout(dqmitems, "11 - PixelPhase1_Cluster_Size_Barrel",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/size_PXLayer_1",
      'description': "Total cluster size in layer 1 of pixel barrel",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/size_PXLayer_2",
      'description': "Total cluster size in layer 2 of pixel barrel",
      'draw': { 'withref': "no" }}],
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/size_PXLayer_3",
      'description': "Total cluster size in layer 3 of pixel barrel",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/size_PXLayer_4",
      'description': "Total cluster size in layer 4 of pixel barrel",
      'draw': { 'withref': "no" }}],
   )

pixellayout(dqmitems, "12 - PixelPhase1_Charge_Endcap",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/charge_PXDisk_+1",
      'description': "Cluster charge in disk +1 of pixel endcap",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/charge_PXDisk_+2",
      'description': "Cluster charge in disk +2 of pixel endcap",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/charge_PXDisk_+3",
      'description': "Cluster charge in disk +3 of pixel endcap",
      'draw': { 'withref': "no" }}],
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/charge_PXDisk_-1",
      'description': "Cluster charge in disk -1 of pixel endcap",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/charge_PXDisk_-2",
      'description': "Cluster charge in disk -2 of pixel endcap",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/charge_PXDisk_-3",
      'description': "Cluster charge in disk -3 of pixel endcap",
      'draw': { 'withref': "no" }}],
   )

pixellayout(dqmitems, "13 - PixelPhase1_ADC_Endcap",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/adc_PXDisk_+1",
      'description': "Distribution of raw charge for all digis recorded in disk +1 of pixel endcap",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/adc_PXDisk_+2",
      'description': "Distribution of raw charge for all digis recorded in disk +2 of pixel endcap",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/adc_PXDisk_+3",
      'description': "Distribution of raw charge for all digis recorded in disk +3 of pixel endcap",
      'draw': { 'withref': "no" }}],
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/adc_PXDisk_-1",
      'description': "Distribution of raw charge for all digis recorded in disk -1 of pixel endcap",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/adc_PXDisk_-2",
      'description': "Distribution of raw charge for all digis recorded in disk -2 of pixel endcap",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/adc_PXDisk_-3",
      'description': "Distribution of raw charge for all digis recorded in disk -3 of pixel endcap",
      'draw': { 'withref': "no" }}],
   )

pixellayout(dqmitems, "14 - PixelPhase1_Digis_Endcap",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/num_digis_PXDisk_+1",
      'description': "Number of Digis in disk +1 of pixel endcap",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/num_digis_PXDisk_+2",
      'description': "Number of Digis in disk +2 of pixel endcap",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/num_digis_PXDisk_+3",
      'description': "Number of Digis in disk +3 of pixel endcap",
      'draw': { 'withref': "no" }}],
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/num_digis_PXDisk_-1",
      'description': "Number of Digis in disk -1 of pixel endcap",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/num_digis_PXDisk_-2",
      'description': "Number of Digis in disk -2 of pixel endcap",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/num_digis_PXDisk_-3",
      'description': "Number of Digis in disk -3 of pixel endcap",
      'draw': { 'withref': "no" }}],
   )

pixellayout(dqmitems, "15 - PixelPhase1_Clusters_Endcap",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/num_clusters_PXDisk_+1",
      'description': "Number of clusters in disk +1 of pixel endcap",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/num_clusters_PXDisk_+2",
      'description': "Number of clusters in disk +2 of pixel endcap",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/num_clusters_PXDisk_+3",
      'description': "Number of clusters in disk +3 of pixel endcap",
      'draw': { 'withref': "no" }}],
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/num_clusters_PXDisk_-1",
      'description': "Number of clusters in disk -1 of pixel endcap",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/num_clusters_PXDisk_-2",
      'description': "Number of clusters in disk -2 of pixel endcap",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/num_clusters_PXDisk_-3",
      'description': "Number of clusters in disk -3 of pixel endcap",
      'draw': { 'withref': "no" }}],
   )

pixellayout(dqmitems, "16 - PixelPhase1_ClusterSize_Endcap",
   [{'path': "PixelPhase1/Phase1_MechanicalView/PXForward/size_PXDisk_+1",
     'description': "Total cluster size in disk +1 of pixel endcap",
     'draw': { 'withref': "no" }},
    {'path': "PixelPhase1/Phase1_MechanicalView/PXForward/size_PXDisk_+2",
     'description': "Total cluster size in disk +2 of pixel endcap",
     'draw': { 'withref': "no" }},
    {'path': "PixelPhase1/Phase1_MechanicalView/PXForward/size_PXDisk_+3",
     'description': "Total cluster size in disk +3 of pixel endcap",
     'draw': { 'withref': "no" }}],
   [{'path': "PixelPhase1/Phase1_MechanicalView/PXForward/size_PXDisk_-1",
     'description': "Total cluster size in disk -1 of pixel endcap",
     'draw': { 'withref': "no" }},
    {'path': "PixelPhase1/Phase1_MechanicalView/PXForward/size_PXDisk_-2",
     'description': "Total cluster size in disk -2 of pixel endcap",
     'draw': { 'withref': "no" }},
    {'path': "PixelPhase1/Phase1_MechanicalView/PXForward/size_PXDisk_-3",
     'description': "Total cluster size in disk -3 of pixel endcap",
     'draw': { 'withref': "no" }}],
   )

pixellayout(dqmitems, "17 - PixelPhase1 Charge: Ladder vs Module barrel summary",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/charge_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_1",
      'description': "Profile of cluster charge per event by signed ladder (y-axis) vs signed module (x-axis) in layer 1 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/charge_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_2",
      'description': "Profile of cluster charge per event by signed ladder (y-axis) vs signed module (x-axis) in layer 2 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/charge_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_3",
      'description': "Profile of cluster charge per event by signed ladder (y-axis) vs signed module (x-axis) in layer 3 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/charge_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_4",
      'description': "Profile of cluster charge per event by signed ladder (y-axis) vs signed module (x-axis) in layer 4 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   )

pixellayout(dqmitems, "18 - PixelPhase1 ADC: Ladder vs Module barrel summary",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/adc_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_1",
      'description': "Profile of raw charge for all digis by signed ladder (y-axis) vs signed module (x-axis) in layer 1 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/adc_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_2",
      'description': "Profile of raw charge for all digis by signed ladder (y-axis) vs signed module (x-axis) in layer 2 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/adc_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_3",
      'description': "Profile of raw charge for all digis by signed ladder (y-axis) vs signed module (x-axis) in layer 3 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/adc_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_4",
      'description': "Profile of raw charge for all digis by signed ladder (y-axis) vs signed module (x-axis) in layer 4 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   )

pixellayout(dqmitems, "19 - PixelPhase1 Cluster Position: Z vs Phi barrel summary",
	[{'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/clusterposition_zphi_PXLayer_1",
  	  'description': "Cluster position in global coordinates by Global Phi (y-axis) vs Global Z (x-axis) in layer 1 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
     {'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/clusterposition_zphi_PXLayer_2",
      'description': "Cluster position in global coordinates by Global Phi (y-axis) vs Global Z (x-axis) in layer 2 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
    [{'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/clusterposition_zphi_PXLayer_3",
      'description': "Cluster position in global coordinates by Global Phi (y-axis) vs Global Z (x-axis) in layer 3 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
     {'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/clusterposition_zphi_PXLayer_4",
      'description': "Cluster position in global coordinates by Global Phi (y-axis) vs Global Z (x-axis) in layer 4 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   )

pixellayout(dqmitems, "20 - PixelPhase1 Cluster Position: X vs Y endcap summary",
    [{'path': "PixelPhase1/Phase1_MechanicalView/PXForward/clusterposition_xy_PXDisk_+1",
      'description': "Cluster position in global coordinates by Global Y (y-axis) vs Global X (x-axis) in disk +1 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
     {'path': "PixelPhase1/Phase1_MechanicalView/PXForward/clusterposition_xy_PXDisk_+2",
      'description': "Cluster position in global coordinates by Global Y (y-axis) vs Global X (x-axis) in disk +2 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
     {'path': "PixelPhase1/Phase1_MechanicalView/PXForward/clusterposition_xy_PXDisk_+3",
      'description': "Cluster position in global coordinates by Global Y (y-axis) vs Global X (x-axis) in disk +3 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
    [{'path': "PixelPhase1/Phase1_MechanicalView/PXForward/clusterposition_xy_PXDisk_-1",
      'description': "Cluster position in global coordinates by Global Y (y-axis) vs Global X (x-axis) in disk -1 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
     {'path': "PixelPhase1/Phase1_MechanicalView/PXForward/clusterposition_xy_PXDisk_-2",
      'description': "Cluster position in global coordinates by Global Y (y-axis) vs Global X (x-axis) in disk -2 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
     {'path': "PixelPhase1/Phase1_MechanicalView/PXForward/clusterposition_xy_PXDisk_-3",
      'description': "Cluster position in global coordinates by Global Y (y-axis) vs Global X (x-axis) in disk -3 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
	)

pixellayout(dqmitems, "21 - PixelPhase1 Digis: Ladder vs Module barrel summary",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/num_digis_per_SignedModule_per_SignedLadder_PXLayer_1",
      'description': "Profile of digis per event and DetID by signed ladder (y-axis) vs signed module (x-axis) in layer 1 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/num_digis_per_SignedModule_per_SignedLadder_PXLayer_2",
      'description': "Profile of digis per event and DetID by signed ladder (y-axis) vs signed module (x-axis) in layer 2 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/num_digis_per_SignedModule_per_SignedLadder_PXLayer_3",
      'description': "Profile of digis per event and DetID by signed ladder (y-axis) vs signed module (x-axis) in layer 3 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/num_digis_per_SignedModule_per_SignedLadder_PXLayer_4",
      'description': "Profile of digis per event and DetID by signed ladder (y-axis) vs signed module (x-axis) in layer 4 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   )

pixellayout(dqmitems, "22 - PixelPhase1 Clusters: Ladder vs Module barrel summary",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/num_clusters_per_SignedModule_per_SignedLadder_PXLayer_1",
      'description': "Profile of number of clusters per event by signed ladder (y-axis) vs signed module (x-axis) in layer 1 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/num_clusters_per_SignedModule_per_SignedLadder_PXLayer_2",
      'description': "Profile of number of clusters per event by signed ladder (y-axis) vs signed module (x-axis) in layer 2 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/num_clusters_per_SignedModule_per_SignedLadder_PXLayer_3",
      'description': "Profile of number of clusters per event by signed ladder (y-axis) vs signed module (x-axis) in layer 3 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/num_clusters_per_SignedModule_per_SignedLadder_PXLayer_4",
      'description': "Profile of number of clusters per event by signed ladder (y-axis) vs signed module (x-axis) in layer 4 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   )

pixellayout(dqmitems, "23 - PixelPhase1 Cluster Size: Ladder vs Module barrel summary",
  [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/size_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_1",
      'description': "Total cluster size by signed ladder (y-axis) vs signed module (x-axis) in layer 1 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
   { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/size_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_2",
      'description': "Total cluster size by signed ladder (y-axis) vs signed module (x-axis) in layer 2 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
  [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/size_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_3",
      'description': "Total cluster size by signed ladder (y-axis) vs signed module (x-axis) in layer 3 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
   { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/size_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_4",
      'description': "Total cluster size by signed ladder (y-axis) vs signed module (x-axis) in layer 4 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
  )

pixellayout(dqmitems, "24 - PixelPhase1 Digi Occupancy: Ladder vs Module barrel summary",
  [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_1",
      'description': "Digi Occupancy by signed ladder (y-axis) vs signed module (x-axis) in layer 1 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
   { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_2",
      'description': "Digi Occupancy by signed ladder (y-axis) vs signed module (x-axis) in layer 2 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
  [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_3",
      'description': "Digi Occupancy by signed ladder (y-axis) vs signed module (x-axis) in layer 1 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
   { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/digi_occupancy_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_4",
      'description': "Digi Occupancy by signed ladder (y-axis) vs signed module (x-axis) in layer 2 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
  )

pixellayout(dqmitems, "25 - PixelPhase1 Cluster Occupancy: Ladder vs Module barrel summary",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_1",
      'description': "Number of clusters per event by signed ladder (y-axis) vs signed module (x-axis) in layer 1 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_2",
      'description': "Number of clusters per event by signed ladder (y-axis) vs signed module (x-axis) in layer 2 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_3",
      'description': "Number of clusters per event by signed ladder (y-axis) vs signed module (x-axis) in layer 3 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/clusters_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_4",
      'description': "Number of clusters per event by signed ladder (y-axis) vs signed module (x-axis) in layer 4 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   )


pixellayout(dqmitems, "26 - PixelPhase1 Charge: BladePannel vs Disk endcap summary",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/charge_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_1",
      'description': "Profile of cluster charge per event by signed blade pannel (y-axis) vs signed disk (x-axis) in ring 1 of endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/charge_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_2",
      'description': "Profile of cluster charge per event by signed blade pannel (y-axis) vs signed disk (x-axis) in ring 2 of endap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   )

pixellayout(dqmitems, "27 - PixelPhase1 ADC: BladePannel vs Disk endcap summary",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/adc_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_1",
      'description': "Profile of raw charge for all digis by signed blade pannel (y-axis) vs signed disk (x-axis) in ring 1 of endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/adc_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_2",
      'description': "Profile of raw charge for all digis by signed blade pannel (y-axis) vs signed disk (x-axis) in ring 2 of endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
    )

pixellayout(dqmitems, "28 - PixelPhase1 Digis: BladePannel vs Disk endcap summary",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/num_digis_per_PXDisk_per_SignedBladePanel_PXRing_1",
      'description': "Profile of number of digis per event and detId by signed blade pannel (y-axis) vs signed disk (x-axis) in ring 1 of endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/num_digis_per_PXDisk_per_SignedBladePanel_PXRing_2",
      'description': "Profile of number of digis per event and detId by signed blade pannel (y-axis) vs signed disk (x-axis) in ring 2 of endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   )

pixellayout(dqmitems, "29 - PixelPhase1 Clusters: BladePannel vs Disk endcap summary",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/num_clusters_per_PXDisk_per_SignedBladePanel_PXRing_1",
      'description': "Profile of number of clusters per event by signed blade pannel (y-axis) vs signed disk (x-axis) in ring 1 of endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/num_clusters_per_PXDisk_per_SignedBladePanel_PXRing_2",
      'description': "Profile of number of clusters per event by signed blade pannel (y-axis) vs signed disk (x-axis) in ring 2 of endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   )

pixellayout(dqmitems, "30 - PixelPhase1 Cluster Occupancy: BladePannel vs Disk endcap summary",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/clusters_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_1",
      'description': "Number of clusters per event by signed blade pannel (y-axis) vs signed disk (x-axis) in ring 1 of endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/clusters_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_2",
      'description': "Number of clusters per event by signed blade pannel (y-axis) vs signed disk (x-axis) in ring 2 of endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   )

pixellayout(dqmitems, "31 - ntracks",
  [{ 'path': "PixelPhase1/Tracks/ntracks",
     'description': "Number of Tracks in all pixel det",
     'draw': {'withref' : "no"}},
   { 'path': "PixelPhase1/Tracks/ntracksinpixvolume",
     'description': "Number of Tracks in pix volume",
     'draw': {'withref' : "no"}}]
  )

pixellayout(dqmitems, "32 - Charge and size",
  [{ 'path': "PixelPhase1/Tracks/charge_PXBarrel",
     'description': "charge PXBarrel",
     'draw': {'withref' : "no"}},
   { 'path': "PixelPhase1/Tracks/charge_PXForward",
     'description': "charge PXForward",
     'draw': {'withref' : "no"}}],
  [{ 'path': "PixelPhase1/Tracks/size_PXBarrel",
     'description': "size of PXBarrel",
     'draw': {'withref' : "no"}},
   { 'path': "PixelPhase1/Tracks/size_PXForward",
     'description': "size of PXForward",
     'draw': {'withref' : "no"}}]
  )

pixellayout(dqmitems, "33 - Cluster on track and vertices per lumi",
  [{ 'path': "PixelPhase1/Tracks/num_clusters_ontrack_per_Lumisection_PXAll",
     'description': "# of cluster on track per Lumisection",
     'draw': {'withref' : "no"}}],
  [{ 'path': "PixelPhase1/Tracks/num_vertices_per_Lumisection",
     'description' : "# vertices per lumisection",
     'draw': {'withref' : "no"}},
   { 'path': "PixelPhase1/Tracks/num_vertices",
     'description' : "# vertices ",
     'draw': {'withref' : "no"}}]
  )

pixellayout(dqmitems, "34 -  Ontrack PXLayer",
  [{ 'path': "PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_1",
     'description': "clusterposition_zphi_ontrack_PXLayer_1",
     'draw': {'withref' : "no", 'drawopts': "COLZ"}},
     { 'path': "PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_2",
        'description': "clusterposition_zphi_ontrack_PXLayer_2",
        'draw': {'withref' : "no", 'drawopts': "COLZ"}}],
   [{ 'path': "PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_3",
      'description': "clusterposition_zphi_ontrack_PXLayer_3",
      'draw': {'withref' : "no", 'drawopts': "COLZ"}},
      { 'path': "PixelPhase1/Tracks/PXBarrel/clusterposition_zphi_ontrack_PXLayer_4",
         'description': "clusterposition_zphi_ontrack_PXLayer_4",
         'draw': {'withref' : "no", 'drawopts': "COLZ"}}]
  )

pixellayout(dqmitems, "35 - Ontrack Disk",
  [{'path': "PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+1",
  'description': "Cluster on track positions in global coordinates by Global Y (y-axis) vs Global X (x-axis) in disk +1 of pixel endcap",
  'draw': { 'withref': "no"}},
  {'path': "PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+2",
  'description': "Cluster on track positions in global coordinates by Global Y (y-axis) vs Global X (x-axis) in disk +2 of pixel endcap",
  'draw': { 'withref': "no"}},
  {'path': "PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_+3",
  'description': "Cluster on track positions in global coordinates by Global Y (y-axis) vs Global X (x-axis) in disk +3 of pixel endcap",
  'draw': { 'withref': "no"}}],
  [{'path': "PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-1",
  'description': "Clusteron on track positions in global coordinates by Global Y (y-axis) vs Global X (x-axis) in disk -1 of pixel endcap",
  'draw': { 'withref': "no"}},
  {'path': "PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-2",
  'description': "Cluster on track positions in global coordinates by Global Y (y-axis) vs Global X (x-axis) in disk -2 of pixel endcap",
  'draw': { 'withref': "no"}},
  {'path': "PixelPhase1/Tracks/PXForward/clusterposition_xy_ontrack_PXDisk_-3",
  'description': "Cluster on track positions in global coordinates by Global Y (y-axis) vs Global X (x-axis) in disk -3 of pixel endcap",
  'draw': { 'withref': "no"}}],
  )


pixellayout(dqmitems, "36 - Hit Efficiency Barrel",
  [{ 'path': "PixelPhase1/Tracks/PXBarrel/hitefficiency_per_SignedModule_per_SignedLadder_PXLayer_1",
     'description': "hitefficiency_per_SignedModule_per_SignedLadder_PXLayer_1",
     'draw': {'withref' : "no", 'drawopts': "COLZ"}},
     { 'path': "PixelPhase1/Tracks/PXBarrel/hitefficiency_per_SignedModule_per_SignedLadder_PXLayer_2",
        'description': "hitefficiency_per_SignedModule_per_SignedLadder_PXLayer_2",
        'draw': {'withref' : "no", 'drawopts': "COLZ"}}],
  [{ 'path': "PixelPhase1/Tracks/PXBarrel/hitefficiency_per_SignedModule_per_SignedLadder_PXLayer_3",
     'description': "hitefficiency_per_SignedModule_per_SignedLadder_PXLayer_3",
     'draw': {'withref' : "no", 'drawopts': "COLZ"}},
     { 'path': "PixelPhase1/Tracks/PXBarrel/hitefficiency_per_SignedModule_per_SignedLadder_PXLayer_4",
        'description': "hitefficiency_per_SignedModule_per_SignedLadder_PXLayer_4",
        'draw': {'withref' : "no", 'drawopts': "COLZ"}}]
  )
pixellayout(dqmitems, "37 - Hit Efficiency Forward",
   [{'path': "PixelPhase1/Tracks/PXForward/hitefficiency_per_PXDisk_per_SignedBladePanel_PXRing_1",
     'description': "hitefficiency_per_PXDisk_per_SignedBl",
     'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    {'path': "PixelPhase1/Tracks/PXForward/hitefficiency_per_PXDisk_per_SignedBladePanel_PXRing_2",
     'description': "hitefficiency_per_PXDisk_per_SignedB2",
     'draw': { 'withref': "no", 'drawopts': "COLZ" }}
    ]
   )
