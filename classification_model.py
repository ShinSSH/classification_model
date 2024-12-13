import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import cv2 as cv
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout, Input, Conv2D, MaxPool2D
from background import removeBackgroundFolder, removeBackgroundSingle

