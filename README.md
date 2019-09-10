# Odometer_Reading_Extraction
This repository is basically build to read the odometer reading from the image of any vehicle meter. 

#### NOTE :- Please note that while cloning this repo please download the pre-trained weights using this link https://drive.google.com/file/d/1msPPXKcNly-uZW8oKFJ0wsTw2fWZPI6h/view?usp=sharing and paste it in the cloned repo folder
## Steps in which this project is build:-
##### 1.First of all the we are provided with the images and their corresponding labels, labels are basically xml and text files containing the digits in the image( let us assume these as the classes ) and their xmin,ymin,xmax,ymax values.\n
##### 2.Now the main issue why we cant just simply use ocr is that the odometer reading are in the seven segmented figure, so ocr generally not works on it.
##### 3.Therefore the first step is to identify the digits in the image, so for that i have used faster r_cnn model to find the digits and their corresponding xmin,ymin,xmax,ymax values in the image we are given to test upon .
##### 4.once we have the digits in the image and there corresponding xmin,ymin,xmax,ymax values then we can easily find the odometer values in the image by using the concept that odometer reading are generally on the left of the "KM" in the image.
## STEPS TO JUST TEST THIS PROJECT ON YOUR IMAGES:-
##### 1. clone this repo in your system.
##### 2. and change your directory to this cloned repo in the cmd , after that just run this command "python test_frcnn.py -p (PATH TO IMAGES YOU WANT TO TEST)"
## STEPS TO TRAIN THIS PROJECT ON YOUR IMAGES:-
##### 1. First of all open "prepare_annotate_file.py" in the cloned repo and provide your opoath in the dataset_dir = "YOUR PATH TO THE FOLDER CONTAINING IMAGES AND LABELS FOLDER", you are also supposed to change "label_dir" and "img_names" few lines below the "dataset_dir". After making changes just run this python file in the cmd.
##### 2. After this we are ready to now tready to train this model on the our images. for this simply run this command in the cmd "python train_frcnn.py -o simple -p annotate.txt"
##### 3. it will take large amount of time ,but once it is trained it ready to predict numbers in the image.
##### 4. in order to test the model on the image just this commend in the cmd "python test_frcnn.py -p (PATH TO THE IMAGES YOUR WANT TO TEST)".

## For the time being now this project is built till the identificaiton of the numbers in the image but soon it will be updated to extract the odometer part
