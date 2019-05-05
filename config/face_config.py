# import the necessary packages
import os

# initialize the base path for the face detection dataset
MODEL_PATH = "./models"
BASE_MODEL_PATH = "./base_models/mobilenet_1_0_224_tf.h5"
# build the path to the output training and testing record files,

# The directories that contain the annotations.
ANNOTATIONS_DIR = '../../data/WIDER-to-VOC-annotations'
# The paths to the each annotations file.
TRAIN_IMAGE_ANNOTATIONS_DIR = os.path.sep.join((ANNOTATIONS_DIR, "WIDER_train_annotations"))
VAL_IMAGE_ANNOTATIONS__DIR = os.path.sep.join((ANNOTATIONS_DIR, "WIDER_val_annotations"))

# The directories that contain the images.
COLAB_BASE_PATH = "../../data"  # Google Colab base path
# The paths to the image sets
TRAIN_WIDER_IMAGES_DIR = os.path.sep.join((COLAB_BASE_PATH, "WIDER_train/images"))
VAL_WIDER_IMAGE_DIR = os.path.sep.join((COLAB_BASE_PATH, "WIDER_val/images"))
TEST_WIDER_IMAGE_DIR = os.path.sep.join((COLAB_BASE_PATH, "WIDER_test/images"))

# The file contains path to images
TRAIN_IMAGE_SET_FILENAMES = os.path.sep.join((COLAB_BASE_PATH, "WIDER_train/wider_face_train_filelist.txt"))
VAL_IMAGE_SET_FILENAMES = os.path.sep.join((COLAB_BASE_PATH, "WIDER_val/wider_face_val_filelist.txt"))
TEST_IMAGE_SET_FILENAMES = os.path.sep.join((COLAB_BASE_PATH, "WIDER_test/wider_face_test_filelist.txt"))

# Small size to test
TRAIN_IMAGE_SET_FILENAMES_SMALL = os.path.sep.join((COLAB_BASE_PATH, "WIDER_train/wider_face_train_filelist_small.txt"))
VAL_IMAGE_SET_FILENAMES_SMALL = os.path.sep.join((COLAB_BASE_PATH, "WIDER_val/wider_face_val_filelist_small.txt"))
