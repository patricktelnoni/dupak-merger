import os, cv2, site, sys
from pdf2image import convert_from_path
from PIL import Image
import numpy as np
site.addsitedir("../../../PDFNetC/Lib")
from PDFNetPython3 import *


glob_path    = os.path.dirname(os.path.realpath(__file__))

def compress(path):
    # Relative path to the folder containing the test files.
    input_path      = path
    output_path     = path
    input_filename  = "result"
    
  
    PDFNet.Initialize()
        
    doc = PDFDoc(input_path + input_filename + ".pdf")
    doc.InitSecurityHandler()
    image_settings = ImageSettings()

    image_settings.SetCompressionMode(ImageSettings.e_jpeg)
    image_settings.SetQuality(1)

    image_settings.SetImageDPI(144,96)

    image_settings.ForceRecompression(True)


    opt_settings = OptimizerSettings()
    opt_settings.SetColorImageSettings(image_settings)
    opt_settings.SetGrayscaleImageSettings(image_settings)

    # use the same settings for both color and grayscale images
    Optimizer.Optimize(doc, opt_settings)
    
    doc.Save(output_path + input_filename + "_opt2.pdf", SDFDoc.e_linearized)
    doc.Close()

def find_incomplete(path):
    incomplete = []
    for root, dir, files  in os.walk(path):  
        for root1, dir1, files1 in os.walk(root):  
            if 'result.pdf' in files1 \
                and ".git" not in root1 \
                and ".vscode" not in root1:                
                
                if os.stat(root1 + "/result.pdf").st_size >= 5000000:
                    print( "Compressing at " + root1, os.stat(root1 + "/result.pdf").st_size)
                    compress(root1+"/")
                    
                    '''
                    image = cv2.imread(root1 + '/result.pdf', cv2.IMREAD_UNCHANGED)
                    print(image)
                    image = cv2.resize (image, (841,595), interpolation=cv2.INTER_CUBIC)
                    image = Image.fromarray (image)
                    
                    image.save (root1 + "/result_compressed.pdf", resolution = 200)
                    '''
                    
    

find_incomplete(glob_path)