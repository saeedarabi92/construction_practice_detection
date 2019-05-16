import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile
import cv2
import glob
import argparse
import pandas as pd
from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image
from utils import label_map_util
from utils import visualization_utils as vis_util
import matplotlib.patches as patches


# if tf.__version__ != '1.4.0':
#   raise ImportError('Please upgrade your tensorflow installation to v1.4.0!')


parser = argparse.ArgumentParser()

parser.add_argument("--input_dir", help = "Path of the input images directory")
parser.add_argument("--frozen_graph", help = "Path of the frozen graph model")
parser.add_argument("--label_map", help = "Path of the label map file")
parser.add_argument("--output_dir", help = "Path of the output directory")
parser.add_argument("--num_output_classes", help="Defines the number of output classes",
                    type=int)

args = parser.parse_args()

def load_image_into_numpy_array(image):
  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape((im_height, im_width, 3)).astype(np.uint8)

# This is needed since the notebook is stored in the object_detection folder.
#sys.path.append("..")

PATH_TO_CKPT = args.frozen_graph
PATH_TO_LABELS = args.label_map
NUM_CLASSES = args.num_output_classes
PATH_TO_TEST_IMAGES_DIR = args.input_dir
PATH_TO_RESULT_IMAGES_DIR = args.output_dir

if not os.path.exists(args.output_dir):
    os.mkdir(args.output_dir)

# print([os.path.abspath(img) for img in os.listdir(PATH_TO_TEST_IMAGES_DIR)])
TEST_IMAGE_PATHS = glob.glob(os.path.join(PATH_TO_TEST_IMAGES_DIR, '*.*'))


JPG_PATHS = [ os.path.basename(path) for path in TEST_IMAGE_PATHS ]

RESULT_IMAGE_PATHS = [ os.path.join(PATH_TO_RESULT_IMAGES_DIR, jpg_path) for jpg_path in JPG_PATHS ]

detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)
print([keys for keys in category_index])
with detection_graph.as_default():
    with tf.Session(graph=detection_graph) as sess:
        # Definite input and output Tensors for detection_graph
        image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

        # Each box represents a part of the image where a particular object was detected.
        detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

        # Each score represent how level of confidence for each of the objects.
        # Score is shown on the result image, together with the class label.

        detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
        detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
        num_detections = detection_graph.get_tensor_by_name('num_detections:0')

        count = 0

        for image_path, result_path in zip(TEST_IMAGE_PATHS, RESULT_IMAGE_PATHS):
            # print('RESULT_IMAGE_PATHS ', RESULT_IMAGE_PATHS)
            # image_np = cv2.imread(image_path, 1)

            image = Image.open(image_path)
            image_resized = np.array(image.resize((300, 300)))
            image = np.array(image)
            # the array based representation of the image will be used later in
            # Actual detection.
            (boxes, scores, classes, num) = sess.run(
            [detection_boxes, detection_scores, detection_classes, num_detections], feed_dict={image_tensor: image_resized[None, ...]})
            # Visualization of the results of a detection.


            boxes = boxes[0] # index by 0 to remove batch dimension
            scores = scores[0]
            classes = classes[0]
            num = np.asarray(num[0])
            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)
            ax.imshow(image)
            detection_list = []
            for i in range(int(num)):
                # scale box to image coordinates
                box = boxes[i] * np.array([image.shape[0], image.shape[1], image.shape[0], image.shape[1]])
                detections = (category_index[classes[i]]['name'],scores[i],box[1], box[0],box[3],box[2])
                detection_list.append(detections)
                # display rectangle
                patch = patches.Rectangle((box[1], box[0]), box[3] - box[1], box[2] - box[0], color='g', alpha=0.4)
                if scores[i] >= .5:
                    ax.add_patch(patch)
                    # class_name = category_index[classes[i]]['name']
                    plt.text(x=box[1] + 10, y=box[2] - 10, s="{}_{}%".format( category_index[classes[i]]['name'], np.round(scores[i]*100,2)), color='w',fontsize=12,style='italic',family='serif', weight='semibold')
                column_name = ['class_name', 'score', 'left', 'top', 'width', 'height']
                detection_df = pd.DataFrame(detection_list, columns=column_name)
            # file_dir = '/home/saeed/Desktop/papers/manuscript1/AIM dataset/Annotations_AIMdataset/all/test_img_test_txt/'
            # file_path = file_dir +  r'{}.txt'.format(image_path.split('/')[-1].split('.')[0])
            # print('file_path: ', file_path)
                detection_df.to_csv(result_path.split('.')[0]+'.txt', index= None, header= None, sep=' ')
            # plt.show()
            plt.axis('off')
            plt.savefig(result_path)

            count += 1
            print('Images Processed:', count, end = '\r')
