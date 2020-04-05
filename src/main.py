import os
import random
import numpy as np
import pandas as pd
import librosa
import librosa.display
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn import model_selection
from sklearn import preprocessing
import IPython.display as ipd


def main():
    # define directories
    base_dir = "./"
    esc_dir = os.path.join(base_dir, "../data")
    meta_file = os.path.join(esc_dir, "meta/esc50.csv")
    audio_dir = os.path.join(esc_dir, "audio/")

    # load metadata
    meta_data = pd.read_csv(meta_file)

    # get data size
    data_size = meta_data.shape
    print(data_size)

    # arrange target label and its name
    class_dict = {}
    for i in range(data_size[0]):
        if meta_data.loc[i, "target"] not in class_dict.keys():
            class_dict[meta_data.loc[i, "target"]
                       ] = meta_data.loc[i, "category"]

if __name__ == "__main__":
    main()
