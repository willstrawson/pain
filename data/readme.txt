
- data/source contains the raw output of the matlab scripts in src/
- data/derivatives contains the processed output of these raw data using src/wrangleresults.py 

- three fMRI datasets have been processed here:
1. dataset1, input data: # TODO - download from neurovault
2. dataset2, input data: '/research/cisc2/projects/ward_painsig/AMY_APOLLO/' # TODO: Mengze uploading full dataset 
3a. dataset3a, input data: '/research/cisc1/projects/ward_painsig/VolumeData2_3D'
3b. dataset3b, input data: /research/cisc1/projects/ward_painsig/uploading_neurovault/processData/

- for each fMRI dataset, three .csv files will be produced:
1. NPS, mask: see applynps.m
2. VPS (old): see applyvps_krishnan2016.m 
3. VPS (new): see applyvps_zhou2020.m 
