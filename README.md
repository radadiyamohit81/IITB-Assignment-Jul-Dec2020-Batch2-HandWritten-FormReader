# Rohan_Kapoor_9599023170-IITB-Assignment-Jul-Dec2020-Batch2

## Handwritten Form Reader Web App  

### 0. my_run.sh
To predict for a folder containing images simply execute my_run.sh. This will print the predictions in the output file.
```
my_run.sh path/of/folder output/file/path/filename.txt
```

### 1. Create new environment  
If using anaconda then create new environment using this in the conda prompt else you can use the navigator as well
```
conda create -n envname python=3.7
```
If not using anaconda then see this link
https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/  

#### Note: Python version is 3.7. Now everything will be done in this environment.

To activate and use the environment 
```
conda activate envname
```

### 2. Clone this repository  
Either Install git-bash from https://git-scm.com/downloads
or 
```
pip install git
```  

Clone this repository using 
```
git clone repository_address
```  
#### After that change location to this repository (Required for all operations)  
```
cd Rohan_Kapoor_9599023170-IITB-Assignment-Jul-Dec2020-Batch2 
```

### 3. Install the required packages    
```
pip install -r requirements.txt
```

### 4. Generating images  
For generating images go to trdg folder in TextRecognitionDataGenerator and then run 'run.py' file
```
cd TextRecognitionDataGenerator/trdg
python run.py -c 100
```  
This will generate 100 images in out folder in this directory.
To check options do
```
python run.py -h
```
You can add more fonts in the fonts folder, more background images, texts, dictionaries etc according to the requirements  
Go to the official documentation https://textrecognitiondatagenerator.readthedocs.io/en/latest/index.html for more details

### 5. Preparing the dataset in tfrecords format
First you need to prepare the annotations.txt file which is just a simple text file containing the locations of all the images in the dataset and their corresponding labels
for eg
```
c:/Users/rkcha/TextRecognitionDataGenerator/trdg/out/11.jpg 7hjLcQ
c:/Users/rkcha/TextRecognitionDataGenerator/trdg/out/12.jpg Yx5vNVfg
c:/Users/rkcha/TextRecognitionDataGenerator/trdg/out/13.jpg DtbngV3Rs
```

Then use the following commands to prepare tfrecords
```
aocr dataset location/of/datasets/annotations-training.txt location/of/datasets/training.tfrecords
aocr dataset location/of/datasets/annotations-testing.txt location/of/datasets/testing.tfrecords
```

To check more options use
```
aocr dataset -h
```

### 6. For training the model
#### First copy the dataset in the tfrecords format in the dataset directory of the repository

Use the following command to train a fresh model and use the option --modcnn if you want to train using the modified cnn architecture  
```
aocr train ./dataset/nameoffile.tfrecords
aocr train --modcnn ./dataset/nameoffile.tfrecords
```  
  
For checking the options available use
```
aocr train -h
```
Here you can change number of epochs, batch size, image size etc.

### 7. Testing the model
Copy the data in the dataset folder of the repository  
To test modified model use 
```
aocr test --model-dir ./checkpoint_mod_model --modcnn ./dataset/nameoffile.tfrecords
```  
To test original model use
```
aocr test --model-dir ./checkpoint_orig_model ./dataset/nameoffile.tfrecords
```  
To test any other model (use --modcnn if trained using modified cnn)
```
aocr test path/of/checkpoints ./dataset/filename.tfrecords
aocr test --modcnn path/of/checkpoints ./dataset/filename.tfrecords
 
```
### 8. To use the web app
```
python app.py
```
and go to link http://127.0.0.1:5000/  then give the url of the image
