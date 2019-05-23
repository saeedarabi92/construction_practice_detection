# Construction practices detection
### This projects contains all the information and codes about construction practices detection project.
---
## Instructions to use image_slicer_script.py:
1. clone the repo
2. create _images_ and _tile_images_ folders
3. put the original images in the _images_ folder
4. run pip install image_slicer
## Notes:
1. To _Split contents of a directory into multiple sub directories_ run this code in terminal:
```
i=0;
for f in *;
do
    d=dir_$(printf %03d $((i/100+1)));
    mkdir -p $d;
    mv "$f" $d;
    let i++;
done

```
---
## Instruction for training with custom dataset
[link to tutorial](https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10)

### To pars json files to a csv file:

Creat _train_ and _eval_ folder under _models/research/object_detection/images/_ and put their images in them.

* From the root directory run:

python models/research/object_detection/json_to_csv.py

### To copy the files from folder1 (and its sub-folders) with the same name of the files in the folder2, into folder2.:

* From the root directory run:

python move_files.py --folder1 /models/research/object_detection/images/images_tiled_raw --folder2 /models/research/object_detection/images/test



### To create tf.record files:

* From the root directory, run:

_for training data_:

python models/research/object_detection/generate_tfrecord.py --csv_input=models/research/object_detection/images/train_labels.csv --image_dir=models/research/object_detection/images/train --output_path=models/research/object_detection/data/train.record

_for eval data_:

python models/research/object_detection/generate_tfrecord.py --csv_input=models/research/object_detection/images/eval_labels.csv --image_dir=models/research/object_detection/images/eval --output_path=models/research/object_detection/data/eval.record

### To run the training:
* From _tensorflow/models/research/_

python object_detection/model_main.py --pipeline_config_path=/home/saeed/Desktop/papers/manuscript1/models/research/object_detection/data/ssd_mobilenet_v1_conv.config --model_dir=/home/saeed/Desktop/papers/manuscript1/models/research/object_detection/models/model --num_train_steps=200000 --sample_1_of_n_eval_examples=1 --alsologtostderr

### To monitor the training using tensorboard:
tensorboard --logdir=/home/saeed/Desktop/papers/manuscript1/models/research/object_detection/models/model

### General notes:
* cuda version:

nvcc --version

* tensorflow version

python -c 'import tensorflow as tf; print(tf.__version__)'

watch -n 0.5 nvidia-smi

---

## ToDo:
1. Try Running the training.
