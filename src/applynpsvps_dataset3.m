%DATASET #3
addpath(genpath('/research/cisc2/projects/ward_painsig/scripts_batches/CanlabCore-master/'))
%% get array of unique subject IDs

% Define the directory path where your files are located
directory_path = '/research/cisc1/projects/ward_painsig/VolumeData2_3D';

% List all files in the directory
files = dir(fullfile(directory_path, '*.nii'));

% Initialize an empty cell array to store the unique subject IDs
unique_subject_ids = cell(0);

% Define a regular expression pattern to match subject IDs
pattern = 'CISC\d+';

% Loop through the files and extract subject IDs
for i = 1:length(files)
    % Extract the file name
    filename = files(i).name;
   
    % Use regular expression to match subject ID
    match = regexp(filename, pattern, 'match');
   
    if ~isempty(match)
        % Add the subject ID to the unique_subject_ids array
        unique_subject_ids = [unique_subject_ids; match];
    end
end

% Convert the cell array to a unique array of subject IDs
unique_subject_ids = unique(unique_subject_ids);

% Display the list of unique subject IDs
disp(unique_subject_ids);

%% load data and  choose conditions 

cd(directory_path)
% DATASET #3
%one dataframe for nps, and one for vps
% one row per participant, determined by numbber of unqiue CISC ids in dir 
%one column per condition 
% 44 conds in total, 36 contrasts for video, 8 for picture 
% fill first column with subids
nps_picture = zeros(numel(unique_subject_ids),9);
nps_video = zeros(numel(unique_subject_ids),37);

vps_picture_krishnan2016 = zeros(numel(unique_subject_ids),9);
vps_video_krishnan2016 = zeros(numel(unique_subject_ids),37);

vps_picture_zhou2020 = zeros(numel(unique_subject_ids),9);
vps_video_zhou2020 = zeros(numel(unique_subject_ids),37);

cd('/research/cisc1/projects/ward_painsig/VolumeData2_3D')

% loop over participant names 
for i = 1:numel(unique_subject_ids)
    subjectID = unique_subject_ids{i};
    
    % remove CISC and convert string to number, then add to first column
    nps_picture(i,1)=str2num(strrep(subjectID, 'CISC', ''));
    nps_video(i,1)=str2num(strrep(subjectID, 'CISC', ''));
    vps_picture(i,1)=str2num(strrep(subjectID, 'CISC', ''));
    vps_video(i,1)=str2num(strrep(subjectID, 'CISC', ''));
    
    
    % loop over files for each participant for pictures  
    for cond = 1:8
        suffix = sprintf('%05d.nii',cond);
        cond = num2str(cond);  
        try
            nps = apply_nps([subjectID, '_results_picture_mni_',suffix]);
            vps_old = apply_vps_krishnan2016([subjectID, '_results_picture_mni_',suffix]);
            vps_new = apply_vps_zhou2020([subjectID, '_results_picture_mni_',suffix]);
            co = str2num(cond) + 1; 
            nps_picture(i,co) = nps{1,1};
            vps_picture_krishnan2016(i,co) = vps_old{1,1};
            vps_picture_zhou2020(i,co) = vps_new{1,1};
        catch
            nps=NaN;
            vps=NaN;
            co = str2num(cond) + 1; 
            nps_picture(i,co) = nps;
            vps_picture_krishnan2016(i,co) = vps;
            vps_picture_zhou2020(i,co) = vps;
        end

    end
    
    % loop over files for each participant for video  
    for cond = 1:36
        suffix = sprintf('%05d.nii',cond);
        cond = num2str(cond);
        try
            nps = apply_nps([subjectID, '_results_video_mni_',suffix]);
            vps_old = apply_vps_krishnan2016([subjectID, '_results_video_mni_',suffix]);
            vps_new = apply_vps_zhou2020([subjectID, '_results_video_mni_',suffix]);
            
            co = str2num(cond) + 1; 
            
            nps_video(i,co) = nps{1,1};
            vps_video_krishnan2016(i,co) = vps_old{1,1};
            vps_video_zhou2020(i,co) = vps_new{1,1};
            
        catch
            co = str2num(cond) + 1; 
            nps_video(i,co) = NaN;
            vps_video_krishnan2016(i,co) = NaN;
            vps_video_zhou2020(i,co) = NaN;
        end

    end
 
end   
    
nps_results = [nps_picture, nps_video(:,2:end)];
vps_results_krishnan2016 = [vps_picture_krishnan2016, vps_video_krishnan2016(:,2:end)];
vps_results_zhou2020 = [vps_picture_zhou2020, vps_video_zhou2020(:,2:end)];

save('results.mat' ,'nps_results', 'vps_results_krishnan2016', 'vps_results_zhou2020');
cd('/its/home/ws231/Downloads/repos/pain/data/source')
writematrix(nps_results,'nps_results_dataset3.csv')
writematrix(vps_results_krishnan2016,'vps_results_dataset3_krishnan2016.csv')
writematrix(vps_results_zhou2020,'vps_results_dataset3_zhou2020.csv')

