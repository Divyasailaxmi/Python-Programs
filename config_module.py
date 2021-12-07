import os
import sys

from utils.torch_utils import select_device

class opt_config():
    def __init__(self):
        self.base_path = ""
        self.detector_weights_path = '/home/lincode/Downloads/exp/weights/best.pt' 
        # self.detector_weights_path = '/home/lincode/manju/yolo_final/exp3/weights/best.pt'
        
        self.crop_detector_weights_path = '/home/lincode/Downloads/half/best.pt'
        self.separate_crop_model = False
        self.classifier_weights = ""
        self.segmentor_weights = ""
        self.ocr_weights = ""
        self.detector_input_image_size = 640 #1280(indo_auto) #640(sup) #640(conrod)
        self.common_conf_thres = 0.2
        self.iou_thres = 0.25
        self.max_det = 1000
        self.device = ""
        self.line_thickness = 2
        self.hide_labels = False
        self.hide_conf = True
        self.half = False
        self.crop = False
        self.crops_folder_path = 'crops'
        self.cord = []
        self.crop_class = ""
        self.min_crop_size = None
        self.max_crop_size = None
        self.crop_conf = 0.25
        self.crop_iou = 0.25
        self.padding  = 50
        self.crop_resize = (640,640)
        self.crop_hide_labels = True
        self.crop_hide_conf = True
        self.classes = None
        self.defects = ["Screw_Absence","Not_Connected","Dent","Scratch","Paint_Peal_Off","Routing_Bad"]
        self.feature = []
        self.visualize = False
        self.individual_thres = {"Screw_Absence":0.1,"Not_Connected":0.1,"Dent":0.1,"Scratch":0.1,"Paint_Peal_Off":1,"Routing_Bad":1,"Routing_Good":1,"Screw_Presence":0.1,"Connected":0.1}