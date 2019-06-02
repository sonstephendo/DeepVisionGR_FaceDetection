# import the necessary packages
import os

# The directories that contain the images.
DRIVE_BASE_PATH = "../dataset"  # Google Colab base path
# The paths to the image sets
TRAIN_WIDER_IMAGES_DIR = os.path.sep.join((DRIVE_BASE_PATH, "WIDER_train/images"))
VAL_WIDER_IMAGE_DIR = os.path.sep.join((DRIVE_BASE_PATH, "WIDER_val/images"))
TEST_WIDER_IMAGE_DIR = os.path.sep.join((DRIVE_BASE_PATH, "WIDER_test/images"))

ANNOTATIONS_DIR = "./dataset"
# The file contains path to images
TRAIN_IMAGE_SET_FILENAMES = os.path.sep.join(
    (ANNOTATIONS_DIR, "wider_face_train_filelist.txt")
)
VAL_IMAGE_SET_FILENAMES = os.path.sep.join(
    (ANNOTATIONS_DIR, "wider_face_val_filelist.txt")
)
TEST_IMAGE_SET_FILENAMES = os.path.sep.join(
    (ANNOTATIONS_DIR, "wider_face_test_filelist.txt")
)

# Small size to test
TRAIN_IMAGE_SET_FILENAMES_SMALL = os.path.sep.join(
    (ANNOTATIONS_DIR, "wider_face_train_filelist_300.txt")
)
VAL_IMAGE_SET_FILENAMES_SMALL = os.path.sep.join(
    (ANNOTATIONS_DIR, "wider_face_val_filelist_100.txt")
)

# initialize the base path for the face detection dataset
MODEL_PATH = "./models"
BASE_MODEL_PATH = "./base_models/mobilenet_1_0_224_tf.h5"
