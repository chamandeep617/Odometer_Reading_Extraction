# Odometer_Reading_Extraction
This repository is basically build to read the odometer reading from the image of any vehicle meter. 
## Steps in which this project is build:-
##### 1.First of all the we are provided with the images and their corresponding labels, labels are basically xml and text files containing the digits in the image( let us assume these as the classes ) and their xmin,ymin,xmax,ymax values.\n
##### 2.Now the main issue why we cant just simply use ocr is that the odometer reading are in the seven segmented figure, so ocr generally not works on it.
##### 3.Therefore the first step is to identify the digits in the image, so for that i have used faster r_cnn model to find the digits and their corresponding xmin,ymin,xmax,ymax values in the image we are given to test upon .
##### 4.once we have the digits in the image and there corresponding xmin,ymin,xmax,ymax values then we can easily find the odometer values in the image by using the concept that odometer reading are generally on the left of the "KM" in the image.
## STEPS TO JUST TEST THIS PROJECT ON YOUR IMAGES:-
##### 1. clone this repo in your system.
##### 2. and change your directory to this cloned repo in the cmd , after that just run this command "python test_frcnn.py -p (PATH TO IMAGES YOU WANT TO TEST)"
