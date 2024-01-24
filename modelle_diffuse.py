from system.estimation import *
from system.segmentation import *
from system.wrap_alignment import *
from system.blending_rendering import *

from system.helper.constants import *

from PIL import Image

def person_segmentation(image):
    return Segmentation(image)

def pose_estimation(image):
    return Estimation(image)

def clothing_warp(clothing_image, pose_info):
    return Wrap_Alignment(clothing_image, pose_info)

def blend_clothing(person_image, warped_clothing):
    return Blending_Rendering(person_image, warped_clothing)

# Main Workflow
person_image = Image.open(PERSON_IMAGE_PATH)
clothing_image = Image.open(CLOTHING_IMAGE_PATH)

segmented_person = person_segmentation(person_image)
pose_info = pose_estimation(person_image)
warped_clothing = clothing_warp(clothing_image, pose_info)
final_image = blend_clothing(segmented_person, warped_clothing)

final_image.save(FINAL_IMAGE_PATH)