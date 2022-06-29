import numpy as np
import os
import cv2
import yaml

path_from = "data/raw/"
path_to = "data/png/"

shootings = os.listdir(path_from)

for shooting in shootings:
     samples = os.listdir(path_from + shooting)
     for sample in samples:
          sample_name, sample_extension = os.path.splitext(sample)

          params = yaml.safe_load(open("params.yaml"))["build_images"][sample_extension[1:]]
          height = params["height"]
          width = params["width"]

          path_to_sample = path_from + shooting + "/" + sample
          path_to_images = path_to + shooting + "/" + sample_extension[1:]

          images = np.fromfile(path_to_sample, "uint8")
          images = np.reshape(images, (-1, height, width))

          if not os.path.isdir(path_to_images):
               os.makedirs(path_to_images)

          for i in range(images.shape[0]):
               name = str(i) + ".png"
               cv2.imwrite(path_to_images + "/" + name, images[i])
