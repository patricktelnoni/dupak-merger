from PyPDF2 import PdfFileMerger
import os, glob
from os import listdir
from os.path import isfile, join

path    = os.path.dirname(os.path.realpath(__file__))
# path    = "/home/patrick/Documents/DUPAK_LEKTOR/Bidang_C/" 
subdir  = []

def merge(files, final_path):
    merger = PdfFileMerger(strict=False)
    for pdf in files:        
        merger.append(pdf)    
    merger.write(final_path+"/result.pdf")
    merger.close()

    splitted        = final_path.split("/")
    splitted[-1]    = "Done-"+splitted[-1]
    new_root        = "/".join(splitted) 
    os.rename(final_path, new_root)
    
def open_subdirectory(path):
    '''
    pakai flag. kalau sampai direktory terbawah, flah done diset true. Lalu up 1 level.
    Besok dipikir mau pakai dictionary atau list
    '''
    if len(path) > 0:
        for folder in path:
            for root, dir, files  in os.walk(folder):    
                if len(files) > 1 and "result.pdf" not in files:
                    print("Merging at ", root)
                    files = [root+"/"+file for file in files]
                    # print(files)
                    merge(files, root)               

def open_directory(path):
    pattern = os.path.join(path, '*')
    
    for candidate in glob.glob(pattern):
        if os.path.isdir(candidate):
            # print("{0} is a directory".format(candidate))
            subdir.append(candidate)
        elif os.path.isfile(candidate):  
            print("{0} is a normal file".format(candidate))  
        else:
            print('No directories found')
    
    open_subdirectory(subdir)

open_directory(path)