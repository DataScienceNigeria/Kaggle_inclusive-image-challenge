import numpy as np
import pandas as pd
import cv2
import time
import matplotlib.pyplot as plt

description = pd.read_csv('dataset/class-descriptions.csv',
                          names=['label', 'description'])
bounding_boxes = pd.read_csv('dataset/train_bounding_boxes.csv',
                           names=['img_id', 'source', 'label', 'confidence', 'xmin', 'xmax', 'ymin', 'ymax',
                                  'isoccluded', 'istruncated', 'isgroupof', 'isdepiction', 'isinside'],
                           nrows=13, skiprows=[0])

print("Creating Label to Feature Dictionary ....................")
label2feature = {}
for label, feature in zip(description.label, description.description):
    label2feature[label] = feature

print("Evaluating ....................")
for row in bounding_boxes.itertuples():
    img = cv2.imread('dataset/training_imgs/train_0/{:s}.jpg'.format(row.img_id))
    length, width = img.shape[0], img.shape[1]
    # cv2.imshow('origin_img', img)
    # cv2.waitKey(0)

    xmin, xmax = int(length*row.xmin), int(length*row.xmax)
    ymin, ymax = int(length*row.ymin), int(length*row.ymax)
    cropped_img = img[ymin:ymax, xmin:xmax]
    cv2.imshow('cropped_img', cropped_img)
    cv2.waitKey(0)

    print(label2feature[row.label])
    cv2.destroyAllWindows()

print(len(label2feature))