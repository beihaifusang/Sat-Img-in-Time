# coding: utf-8

import matplotlib.pyplot as plt
import scipy.io as sio
import skimage.io
import numpy as np
import h5py
import sys
import gc

from optparse import OptionParser

sys.path.append('../../Visualization/')
from Visualization import *


parser = OptionParser()
parser.add_option("--path", dest="pred_dir")
parser.add_option("--name", dest="pred_name")

parser.add_option("--train", dest="path_train_set", default="../../Data/090085/Road_Data/motor_trunk_pri_sec_tert_uncl_track/posneg_topleft_coord_split_8_train")
parser.add_option("--cv", dest="path_cv_set", default="../../Data/090085/Road_Data/motor_trunk_pri_sec_tert_uncl_track/posneg_topleft_coord_split_8_cv")

parser.add_option("--pred_weight", type="float", default=0.5, dest="pred_weight")
parser.add_option("--analyze_train", action='store_true', default=False, dest="analyze_train")
parser.add_option("--analyze_CV", action='store_true', default=False, dest="analyze_CV")

(options, args) = parser.parse_args()

pred_dir = options.pred_dir
pred_name = options.pred_name
path_train_set = options.path_train_set
path_cv_set = options.path_cv_set
pred_weight = options.pred_weight

analyze_train = options.analyze_train
analyze_CV = options.analyze_CV

h5f = h5py.File(pred_dir + pred_name, 'r')
train_pred = np.array(h5f['train_pred'])
CV_pred = np.array(h5f['CV_pred'])
h5f.close()

save_name = pred_name.split('.')[0]

if analyze_train:
    # Load training set
    train_set = h5py.File(path_train_set, 'r')
    train_raw_image = np.array(train_set['raw_image'])
    train_road_mask = np.array(train_set['road_mask'])
    train_set.close()

    show_pred_prob_with_raw(train_raw_image, train_pred, train_road_mask, pred_weight=pred_weight, figsize=(150,150), 
    						show_plot=False, save_path=pred_dir + save_name + '_train_' + str(pred_weight).replace('.', '_') + '.png')
    plt.close()

if analyze_CV:
    # Load cross-validation set
    CV_set = h5py.File(path_cv_set, 'r')
    CV_raw_image = np.array(CV_set['raw_image'])
    CV_road_mask = np.array(CV_set['road_mask'])
    CV_set.close()
    gc.collect()

    show_pred_prob_with_raw(CV_raw_image, CV_pred, CV_road_mask, pred_weight=pred_weight, figsize=(150,150), 
    						show_plot=False, save_path=pred_dir + save_name + '_CV_' + str(pred_weight).replace('.', '_') + '.png')
    plt.close()