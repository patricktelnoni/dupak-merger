import os, glob

glob_path    = os.path.dirname(os.path.realpath(__file__))

def find_incomplete(path):
    incomplete = []
    for root, dir, files  in os.walk(path):  
        for root1, dir1, files1 in os.walk(root):  
            if 'result.pdf' not in files1 \
                and ".git" not in root1 \
                and ".vscode" not in root1 \
                and len(files1) > 0 \
                and root != glob_path:
                if root1 not in incomplete:
                    incomplete.append(root1)
    
    for folder in incomplete:
        print(folder, "\n")

find_incomplete(glob_path)