# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import pandas as pd

# wrangle nps/vps data for dataset 1, 2 (TODO), and 3

df_nps_1 = pd.read_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/source/nps_results_dataset1.csv', header=None)
df_vps_1 = pd.read_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/source/vps_results_dataset1.csv', header=None)

df_nps_3 = pd.read_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/source/nps_results_dataset3.csv', header=None)
df_vps_3 = pd.read_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/source/vps_results_dataset3.csv', header=None)


# create dictionary of column header numbers to key names 
column_keys_dataset1 =
    {
        0:'subject_id',
        1:'contrast1',
        2:'contrast2',
        3:'contrast3',
        4:'contrast4'
    }

column_keys_dataset3 = 
    {
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

# name columns as per keys above
df_nps_1.rename(columns=column_keys_dataset1, inplace=True)
df_vps_1.rename(columns=column_keys_dataset1, inplace=True)

df_nps_3.rename(columns=column_keys_dataset3, inplace=True)
df_vps_3.rename(columns=column_keys_dataset3, inplace=True)

# prefix CISC to subject ids
df_nps_1['subject_id']+'CISC'+df['subject_id'].astype(str)
df_vps_1['subject_id']+'CISC'+df['subject_id'].astype(str)

df_nps_3['subject_id']+'CISC'+df['subject_id'].astype(str)
df_vps_3['subject_id']+'CISC'+df['subject_id'].astype(str)

# save 
df_nps_1.to_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/derivatives/nps_results_dataset1.csv')
df_vps_1.to_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/derivatives/vps_results_dataset1.csv')

df_nps_3.to_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/derivatives/nps_results_dataset3.csv')
df_vps_3.to_csv('/Users/willstrawson/Documents/PhD/repos/pain/data/derivatives/vps_results_dataset3.csv')






