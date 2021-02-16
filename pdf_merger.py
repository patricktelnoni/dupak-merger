from PyPDF2 import PdfFileMerger
import os, glob
from os import listdir
from os.path import isfile, join


path    = '/home/patrick/Documents/DUPAK_LEKTOR/'
subdir  = []

def merge(files):
    merger = PdfFileMerger()
    for pdf in files:        
        merger.append(path+pdf)

    merger.write(path+"result.pdf")
    merger.close()

def open_subdirectory(path):
    '''
    pakai flag. kalau sampai direktory terbawah, flah done diset true. Lalu up 1 level.
    Besok dipikir mau pakai dictionary atau list
    '''
    pass

def open_directory(path):

    pattern = os.path.join(path, '*')
    
    for candidate in glob.glob(pattern):
        if os.path.isdir(candidate):
            print("{0} is a directory".format(candidate))
            subdir.append(candidate)
        elif os.path.isfile(candidate):  
            print("{0} is a normal file".format(candidate))  
        else:
            print('No directories found')
    # for path, subdirs, files in os.walk(path):
    #    print(subdirs)
        #for name in files:
            #print(os.path.join(path, name))
    #subdir = [f for f in listdir(path) if isfile(join(path, f))]
    #return files

open_directory(path)




