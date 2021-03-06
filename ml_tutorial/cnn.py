# AUTOGENERATED! DO NOT EDIT! File to edit: 06_cnn.ipynb (unless otherwise specified).

__all__ = ['get_num_lines', 'load_symbols', 'load_data']

# Cell
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Activation, Flatten, Dropout
from sklearn.model_selection import train_test_split
from tqdm import tqdm
from PIL import Image
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Cell
def get_num_lines(file_name):
    """ Counts the number of lines in the file. """

    f = open(file_name, 'r')
    counter = 0;
    for i in f:
        counter += 1
    return counter


# Cell
def load_symbols(file_name):
    """ Reads the file having symbols and create two maps: `id2latex` and `latex2id`
    to encode the symbols and retrieve them easily. """

    id2latex = dict()
    latex2id = dict()
    f = open(file_name,'r')
    next(f)
    id = 0;
    for line in tqdm(f, total=get_num_lines(file_name)):
      _,latex,_,_ = line.split(',')
      if latex not in latex2id:
          latex2id[latex] = id
          id2latex[id] = latex
          id += 1
    return (id2latex,latex2id)

# Cell
def load_data(label_file_name,latex2id):
    """ Reads the data file and create and return `data` and `labels` lists. """
    data = []
    labels = []
    f = open(label_file_name,'r')
    next(f)
    for line in tqdm(f, total=get_num_lines(label_file_name)):
      image_path,symbol_id,latex,_ = line.split(',')
      img = Image.open(os.path.join(image_path)).convert('L')
      img_array = np.asarray(img).astype('float32')
      data.append(img_array)
      labels.append(latex2id[latex])
    return (data,labels)