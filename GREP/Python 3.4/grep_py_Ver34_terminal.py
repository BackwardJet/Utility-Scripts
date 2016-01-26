import os
import sys

rootdir = sys.argv[1] #input('Name of root directory: ')
input_str = sys.argv[2] #input('String to search for: ')

files_with_str = []
for root, subFolders, files in os.walk(rootdir):
    for filename in files:
        fullpath = os.path.join(root, filename)
        with open(fullpath, 'r') as f:
            file_text = f.read()
            if input_str in file_text:
                files_with_str.append(fullpath)

if len(files_with_str) == 0:
    print('There are no files that match that string.')
else:
    for path in files_with_str:
        print(path)
