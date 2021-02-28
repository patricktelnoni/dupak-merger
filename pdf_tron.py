import site
site.addsitedir("../../../PDFNetC/Lib")
import sys
from PDFNetPython3 import *


def main():
    
    # Relative path to the folder containing the test files.
    input_path      = "/home/patrick/Documents/DUPAK_LEKTOR/"
    output_path     = "/home/patrick/Documents/DUPAK_LEKTOR/"
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
	
    
if __name__ == '__main__':
    main()