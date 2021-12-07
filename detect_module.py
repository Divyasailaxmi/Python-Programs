import argparse
import os
import sys
from pathlib import Path

import cv2
import numpy as np
import torch
import torch.backends.cudnn as cudnn

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

from models.experimental import attempt_load
from utils.datasets import LoadImages, LoadStreams
from utils.general import apply_classifier, check_img_size, check_imshow, check_requirements, check_suffix, colorstr, \
    increment_path, non_max_suppression, print_args, save_one_box, scale_coords, set_logging, \
    strip_optimizer, xyxy2xywh
from utils.plots import Annotator, colors
from utils.torch_utils import load_classifier, select_device, time_sync
from config_module import *



def letterbox(im, new_shape=(640, 640), color=(114, 114, 114), auto=True, scaleFill=False, scaleup=True, stride=32):
    # Resize and pad image while meeting stride-multiple constraints
    shape = im.shape[:2]  # current shape [height, width]
    if isinstance(new_shape, int):
        new_shape = (new_shape, new_shape)

    # Scale ratio (new / old)
    r = min(new_shape[0] / shape[0], new_shape[1] / shape[1])
    if not scaleup:  # only scale down, do not scale up (for better val mAP)
        r = min(r, 1.0)

    # Compute padding
    ratio = r, r  # width, height ratios
    new_unpad = int(round(shape[1] * r)), int(round(shape[0] * r))
    dw, dh = new_shape[1] - new_unpad[0], new_shape[0] - new_unpad[1]  # wh padding
    if auto:  # minimum rectangle
        dw, dh = np.mod(dw, stride), np.mod(dh, stride)  # wh padding
    elif scaleFill:  # stretch
        dw, dh = 0.0, 0.0
        new_unpad = (new_shape[1], new_shape[0])
        ratio = new_shape[1] / shape[1], new_shape[0] / shape[0]  # width, height ratios

    dw /= 2  # divide padding into 2 sides
    dh /= 2

    if shape[::-1] != new_unpad:  # resize
        im = cv2.resize(im, new_unpad, interpolation=cv2.INTER_LINEAR)
    top, bottom = int(round(dh - 0.1)), int(round(dh + 0.1))
    left, right = int(round(dw - 0.1)), int(round(dw + 0.1))
    im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)  # add border
    return im, ratio, (dw, dh)


def image_preprocess(image ,img_size=640, stride=32):
    # Padded resize
    img = letterbox(image, img_size , stride=stride)[0]

    # Convert
    img = img.transpose((2, 0, 1))[::-1]  # HWC to CHW, BGR to RGB
    img = np.ascontiguousarray(img)
    return img

opt = opt_config()
def load_detector(path,half,device,imgsz):
    device = select_device(device)
    half &= device.type != 'cpu' 
    model = attempt_load(weights = path, map_location=device)
    stride = int(model.stride.max())
    names = model.module.names if hasattr(model, 'module') else model.names
    #names = model.module.names if hasattr(model, 'module') else model.names  # get class names
    if half:
        model.half()  # to FP16
    imgsz = check_img_size(imgsz, s=stride)  # check image size
    # Run inference
    if True and device.type != 'cpu':
        model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))
    print("Model loaded!!!")
    return model , stride , names


def detector_get_inference(opt ,im0, names,img_size  ,stride, model, device ,half ):
    # img0 = cv2.imread(path)
    print("inside inference!!")
    predictions = []
    cord = []
    imc = im0.copy()



    img = im0.astype('float32')
    img = torch.from_numpy(im0).to(device)
    img = img.half() if half else img.float()  # uint8 to fp16/32
    img /= 255.0  # 0 - 255 to 0.0 - 1.0
    if len(img.shape) == 3:
        img = img[None]  # expand for batch dim

    pred = model(img)[0]
    pred = non_max_suppression(pred)



    # Process predictions
    for i, det in enumerate(pred):
        annotator = Annotator(im0, line_width=3, example=str(names))
        if len(det):
            # Rescale boxes from img_size to im0 size
            det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

            # Print results
            for c in det[:, -1].unique():
                n = (det[:, -1] == c).sum()  # detections per class

            # Write results
            for *xyxy, conf, cls in reversed(det):
                c = int(cls)  # integer class
                label = None if opt.hide_labels else (names[c] if opt.hide_conf else f'{names[c]} {conf:.2f}')
                annotator.box_label(xyxy, label, color=colors(c, True))
    
    return im0

def detector_get_inference1(opt ,im0, names,img_size  ,stride, model, device ,half ):
    # img0 = cv2.imread(path)
    print("inside inference!!")
    predictions = []
    cord = []

    img = image_preprocess(im0 , img_size = img_size ,stride = stride)
    # img = torch.from_numpy(im0).to(device)
    if True: # pt
        img = torch.from_numpy(img).to(device)
        img = img.half() if half else img.float() 
    img /= 255.0  # 0 - 255 to 0.0 - 1.0
    if len(img.shape) == 3:
        img = img[None]

    #Inference
    pred = model(img, augment=False, visualize=False)[0]

    # NMS
    pred = non_max_suppression(pred, conf_thres = opt.crop_conf, iou_thres = opt.crop_iou, classes = None, agnostic = False, max_det=1000)

    # Process predictions
    for i, det in enumerate(pred):  # detections per image
        gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
        imc = im0.copy()
        
        annotator = Annotator(im0, line_width=opt.line_thickness, example=str(names))
        if len(det):
            # Rescale boxes from img_size to im0 size
            det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()
            # Write results
            for *xyxy, conf, cls in reversed(det):

                xmin = int(xyxy[0].item())
                ymin = int(xyxy[1].item())
                xmax = int(xyxy[2].item())
                ymax = int(xyxy[3].item())




                c = int(cls)  # integer class
                if names[c] in list(opt.individual_thres.keys()):
                    if conf > opt.individual_thres[names[c]] :
                        label = None if opt.hide_labels else (names[c] if opt.hide_conf else f'{names[c]} {conf:.2f}')
                        if bool(opt.defects) :
                            if names[c] in opt.defects:
                                bndbox_color = [60,20,250]#RED
                            else:
                                bndbox_color = [0,128,0]#GREEN
                        else:
                            bndbox_color = colors(c, True)
                        
                        annotator.box_label(xyxy, label, color=bndbox_color)
                        predictions.append(names[c])
                        cord.append({label:[xmin,ymin,xmax,ymax]})
                else:
                    label = None if opt.hide_labels else (names[c] if opt.hide_conf else f'{names[c]} {conf:.2f}')
                    if bool(opt.defects) :
                        if names[c] in opt.defects:
                            bndbox_color = [60,20,250]#RED
                        else:
                            bndbox_color = [0,128,0]#GREEN
                    else:
                        bndbox_color = colors(c, True)
                    
                    annotator.box_label(xyxy, label, color=bndbox_color)
                    predictions.append(names[c])
                    cord.append({label:[xmin,ymin,xmax,ymax]})
                

    torch.cuda.empty_cache()
    return im0 , predictions,cord


                
