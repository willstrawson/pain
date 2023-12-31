# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import pandas as pd
import numpy as np

# wrangle nps/vps data for dataset 1, 2 (TODO), and 3

df_nps_1 = pd.read_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/source/nps_results_dataset1.csv', header=None)
df_vps_1_old = pd.read_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/source/vps_results_dataset1_krishnan2016.csv', header=None)
df_vps_1_new = pd.read_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/source/vps_results_dataset1_zhou2020.csv', header=None)

df_nps_2 = pd.read_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/source/nps_results_dataset2.csv', header=None)
df_vps_2_old = pd.read_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/source/vps_results_dataset2_krishnan2016.csv', header=None)
df_vps_2_new = pd.read_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/source/vps_results_dataset2_zhou2020.csv', header=None)

df_nps_3a = pd.read_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/source/nps_results_dataset3.csv', header=None)
df_vps_3a_old = pd.read_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/source/vps_results_dataset3_krishnan2016.csv', header=None)
df_vps_3a_new = pd.read_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/source/vps_results_dataset3_zhou2020.csv', header=None)

df_nps_3b = pd.read_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/source/nps_results_dataset1.csv', header=None)
df_vps_3b_old = pd.read_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/source/vps_results_dataset1_krishnan2016.csv', header=None)
df_vps_3b_new = pd.read_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/source/vps_results_dataset1_zhou2020.csv', header=None)


# create dictionary of column header numbers to key names 
column_keys_dataset1 = {
        0:'subject_id',
        1:'pain',
        2:'no_pain',
    }

column_keys_dataset2 = {
        0:'subject_id',
        1:'beta1',
        2:'beta2',
        3:'beta3',
        4:'beta4',
        5:'beta5',
        6:'beta6',
        7:'beta7',
        8:'beta8',
        9:'beta9',
        10:'beta10',
        11:'beta11',
        12:'beta12',
        13:'beta13',
        14:'beta14'
    }

column_keys_dataset3a = {
        0:'subject_id',
        1:'foot_nopain',
        2:'foot_pain',
        3:'hand_nopain',
        4:'hand_pain',
        5:'foot_nopain_fix',
        6:'foot_pain_fix',
        7:'hand_nopain_fix',
        8:'hand_pain_fix',
        9:'cue_self1hand',
        10:'cue_other1hand',
        11:'cue_self2hand',
        12:'cue_other2hand',
        13:'cue_self3hand',
        14:'cue_other3hand',
        15:'cue_self1foot',
        16:'cue_other1foot',
        17:'cue_self2foot',
        18:'cue_other2foot',
        19:'cue_self3foot',
        20:'cue_other3foot',
        21:'shock_self1hand',
        22:'shock_other1hand',
        23:'shock_self2hand',
        24:'shock_other2hand',
        25:'shock_self3hand',
        26:'shock_other3hand',
        27:'shock_self1foot',
        28:'shock_other1foot',
        29:'shock_self2foot',
        30:'shock_other2foot',
        31:'shock_self3foot',
        32:'shock_other3foot',
        33:'circle_self1hand',
        34:'circle_other1hand',
        35:'circle_self2hand',
        36:'circle_other2hand',
        37:'circle_self3hand',
        38:'circle_other3hand',
        39:'circle_self1foot',
        40:'circle_other1foot',
        41:'circle_self2foot',
        42:'circle_other2foot',
        43:'circle_self3foot',
        44:'circle_other3foot'
    }

column_keys_dataset3b = {
        0:'subject_id',
        1:'contrast1',
        2:'contrast2',
        3:'contrast3',
        4:'contrast4'
    }


# name columns as per keys above
df_nps_1.rename(columns=column_keys_dataset1, inplace=True)
df_vps_1_old.rename(columns=column_keys_dataset1, inplace=True)
df_vps_1_new.rename(columns=column_keys_dataset1, inplace=True)

df_nps_2.rename(columns=column_keys_dataset2, inplace=True)
df_vps_2_old.rename(columns=column_keys_dataset2, inplace=True)
df_vps_2_new.rename(columns=column_keys_dataset2, inplace=True)

df_nps_3a.rename(columns=column_keys_dataset3a, inplace=True)
df_vps_3a_old.rename(columns=column_keys_dataset3a, inplace=True)
df_vps_3a_new.rename(columns=column_keys_dataset3a, inplace=True)

df_nps_3b.rename(columns=column_keys_dataset3b, inplace=True)
df_vps_3b_old.rename(columns=column_keys_dataset3b, inplace=True)
df_vps_3b_new.rename(columns=column_keys_dataset3b, inplace=True)

# prefix CISC to subject ids
df_nps_2['subject_id']='CISC'+df_nps_2['subject_id'].astype(str)
df_vps_2_old['subject_id']='CISC'+df_vps_2_old['subject_id'].astype(str)
df_vps_2_new['subject_id']='CISC'+df_vps_2_new['subject_id'].astype(str)

df_nps_3a['subject_id']='CISC'+df_nps_3a['subject_id'].astype(str)
df_vps_3a_old['subject_id']='CISC'+df_vps_3a_old['subject_id'].astype(str)
df_vps_3a_new['subject_id']='CISC'+df_vps_3a_new['subject_id'].astype(str)

df_nps_3b['subject_id']='CISC'+df_nps_3b['subject_id'].astype(str)
df_vps_3b_old['subject_id']='CISC'+df_vps_3b_old['subject_id'].astype(str)
df_vps_3b_new['subject_id']='CISC'+df_vps_3b_new['subject_id'].astype(str)

# fill empty cells with NaN
df_nps_2.fillna(np.nan, inplace=True)
df_vps_2_old.fillna(np.nan, inplace=True)
df_vps_2_new.fillna(np.nan, inplace=True)

df_nps_3a.fillna(np.nan, inplace=True)
df_vps_3a_old.fillna(np.nan, inplace=True)
df_vps_3a_new.fillna(np.nan, inplace=True)

df_nps_3b.fillna(np.nan, inplace=True)
df_vps_3b_old.fillna(np.nan, inplace=True)
df_vps_3b_new.fillna(np.nan, inplace=True)

# save 
df_nps_1.to_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/derivatives/nps_results_dataset1.csv')
df_vps_1_old.to_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/derivatives/vps_results_dataset1_krishnan2016.csv')
df_vps_1_new.to_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/derivatives/vps_results_dataset1_zhou2020.csv')

df_nps_2.to_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/derivatives/nps_results_dataset2.csv')
df_vps_2_old.to_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/derivatives/vps_results_dataset2_krishnan2016.csv')
df_vps_2_new.to_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/derivatives/vps_results_dataset2_zhou2020.csv')

df_nps_3a.to_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/derivatives/nps_results_dataset3a.csv')
df_vps_3a_old.to_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/derivatives/vps_results_dataset3a_krishnan2016.csv')
df_vps_3a_new.to_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/derivatives/vps_results_dataset3a_zhou2020.csv')

df_nps_3b.to_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/derivatives/nps_results_dataset3b.csv')
df_vps_3b_old.to_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/derivatives/vps_results_dataset3b_krishnan2016.csv')
df_vps_3b_new.to_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/derivatives/vps_results_dataset3b_zhou2020.csv')





