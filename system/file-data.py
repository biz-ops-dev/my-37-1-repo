import os
from pathlib import Path

def count_files(folder) -> str:
    print(folder)
    files_folder_count = len(os.listdir(folder))
    file_count = sum(1 for _ in Path(folder).glob('**/*'))
    print(f'files/folder: {files_folder_count}')
    print(f'files: {file_count}')
    return

def get_size(folder):
    size = 0
    for path, dirs, files in os.walk(folder):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)
    size /= 1_000_000
    size = round(size, 0)
    print(f'Size: {size} mb')
    return

def alldata(folder):
    count_files(folder)
    get_size(folder)
    return

job_org = '/Users/pr-mbausr/Library/CloudStorage/OneDrive-Personal/Job Applications/Org- Write About'

alldata(job_org)

"""  Questions:

1. Python General
Why can't I pass dictionary object through function?

folders = {
    'jobOrg': '/Users/pr-mbausr/Library/CloudStorage/OneDrive-Personal/Job Applications/Org- Write About',
    'second': 'none yet',
}

alldata(folders['jobOrg'])

2. This module
    files_folder_count = len(os.listdir(folder))
    file_count = sum(1 for _ in Path(folder).glob('**/*'))

3. What is the size output provided in?  mb* 100,000
    287743893 = 287.5 mb

NEXT STEPS

remove '/Users/pr-mbausr/Library/CloudStorage/OneDrive-Personal/Apps/my-apps-old-structure/operating_system_functions/count_files.py'

make output go to another file
make dictionary / directory of folders for easy access
"""