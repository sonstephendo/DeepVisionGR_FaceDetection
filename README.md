# Facial-Detecion

## Overview
Using WIDER FACE Dataset to detect human face using Single Shot Detection

## Installation

The necessary dependencies are in the requirements.txt file so just run this before running the actual code to get them installed. May require some extra effort for OpenCV though.

``
pip3 install -r requirements.txt
``

## Usage

Download the dataset and either change "DRIVE_BASE_PATH" in config/path.py or put the dataset into dataset folder.

Follow the instruction in face_train.ipynb for "base model" and face_train_large_mul.ipynb for "bigger base model" 
(included 2 bigger feature maps before conv4_3 to increase small faces detection performance) 

## Model Weight: 

Available checkpoints:

Base model:

https://drive.google.com/drive/folders/1FM9HKf_7m8T3uwCpeUdjLea_hI04Flo1?fbclid=IwAR1e8qremq6p-oytBnKximrzQwGdSW4XmwK3115J1TqNuVXWFD3GP_CUJeE

Large model:

https://drive.google.com/drive/folders/19qg2-Gp17rPrxv6bhhqawmc74Re4uRrd?fbclid=IwAR1LfZ5vx99OAWFzYfkAdjGY8GKBpa3Hu5J5jytBkOAC71q5_P27bclh3N0