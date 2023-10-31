% DATASET #1
addpath(genpath('/research/cisc2/projects/ward_painsig/scripts_batches/CanlabCore-master/'))
%% get array of unique subject IDs

% Define the directory path where your files are located
directory_path = '/research/cisc2/projects/ward_painsig/dataset1_neurovault_ward2017/';

% List all files in the directory
files = dir(fullfile(directory_path, '*.nii.gz'));

% Initialize an empty cell array to store the unique subject IDs
unique_subject_ids = cell(0);

% Define a regular expression pattern to match subject IDs
pattern = '(\d{2})(?=p|np)';

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
disp(unique_subject_ids)

%% get array of unique subject IDs

%one dataframe for nps, and one for vps
% one row per participant (n=41), one column per condition 
% 4 contrasts for picture 
% fill first column with subids
nps_picture = zeros(numel(unique_subject_ids),3);
vps_picture_krishnan2016 = zeros(numel(unique_subject_ids),3);
vps_picture_zhou2020 = zeros(numel(unique_subject_ids),3);

cd(directory_path)
strings = {'p','np'}

% loop over participant name 
for i = 1:numel(unique_subject_ids)
    subjectID = unique_subject_ids{i};
    
    % remove CISC and convert string to number, then add to first column
    nps_picture(i,1)=str2num(subjectID);
    vps_picture_krishnan2016(i,1)=str2num(subjectID);  
    vps_picture_zhou2020(i,1)=str2num(subjectID); 
    
    iteration_count = 0 
    
    % loop over files for each participant for pictures  
    for cond = 1:length(strings)
        suffix = [strings{cond}, '.nii.gz']
        iteration_count = iteration_count + 1
        
        %try
            nps = apply_nps([subjectID,suffix]);
            vps_old = apply_vps_krishnan2016([subjectID, suffix]);
            vps_new = apply_vps_zhou2020([subjectID,suffix]);
            co = iteration_count + 1; 
            nps_picture(i,co) = nps{1,1};
            vps_picture_krishnan2016(i,co) = vps_old{1,1};
            vps_picture_zhou2020(i,co) = vps_new{1,1};
        %catch
        %    nps=NaN;
        %    vps=NaN;
        %    co = str2num(cond) + 1; 
        %    nps_picture(i,co) = nps;
        %    vps_picture(i,co) = vps;
        %end

    end
 
end   
    

save('results.mat' ,'nps_picture', 'vps_picture_krishnan2016', 'vps_picture_zhou2020');
% save results in github dir 
cd('/its/home/ws231/Downloads/repos/pain/data/source')
writematrix(nps_picture,'nps_results_dataset1.csv')
writematrix(vps_picture_krishnan2016,'vps_results_dataset1_krishnan2016.csv')
writematrix(vps_picture_zhou2020,'vps_results_dataset1_zhou2020.csv')

