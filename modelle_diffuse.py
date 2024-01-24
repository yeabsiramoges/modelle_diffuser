from system.estimation import *
from system.segmentation import *
from system.wrap_alignment import *
from system.blending_rendering import *

from PIL import Image

def person_segmentation(image):
    pass

def pose_estimation(image):
    pass

def clothing_warp(clothing_image, pose_info):
    pass

def blend_clothing(person_image, warped_clothing):
    pass

# Main Workflow
person_image = Image.open('path_to_person_image')
clothing_image = Image.open('path_to_clothing_image')

segmented_person = person_segmentation(person_image)
pose_info = pose_estimation(person_image)
warped_clothing = clothing_warp(clothing_image, pose_info)
final_image = blend_clothing(segmented_person, warped_clothing)

final_image.save('path_to_save_final_image')