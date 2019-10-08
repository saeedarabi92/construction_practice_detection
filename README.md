
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

1. Create _train_ and _eval_ folder under _models/research/object_detection/images/_ and put the related annotations and images (eval and train) in their folder.

    * To copy the files from folder1 (and its sub-folders) with the same name of the files in the folder2, into folder2.: (This is for copying annotations to _eval_ and _train_ folder)

    For example, from the root directory run:`python move_files.py --folder1 /models/research/object_detection/images/{folder_name} --folder2 /models/research/object_detection/images/{folder_name}`


2. From the root directory run: `python models/research/object_detection/json_to_csv.py`. (This will create .csv files which will later be used to create the _tfrecord_ files)


3. Create tfrecord files: once the .csv files were created, _tfrecord_ files of training and evaluation will be created for training purposes.

    * To create _tf.record_ files, from the root directory, run: (`generate_tfrecord.py` should modified based on the custom dataset annotation) `python models/research/object_detection/generate_tfrecord.py --csv_input=models/research/object_detection/images/{train/eval}_labels.csv --image_dir=models/research/object_detection/images/{train/eval} --output_path=models/research/object_detection/data/{train/eval}.record`

4. To run the training:

    * From _tensorflow/models/research/_ run: `python object_detection/model_main.py --pipeline_config_path=/home/saeed/Desktop/github/construction_practice_detection/models/research/object_detection/data/configs/ssd_mobilenet_modified.config --model_dir=/home/saeed/Desktop/github/construction_practice_detection/models/research/object_detection/data/checkpoints --num_train_steps=200000 --sample_1_of_n_eval_examples=1 --alsologtostderr`

5. To monitor the training using tensorboard:

    * Run this in a separate terminal and click on the link which provides by tensorboard in the terminal:`tensorboard --logdir=/home/saeed/Desktop/github/construction_practice_detection/models/research/object_detection/data/checkpoints`


6. To generate a frozen graph:

    * From _tensorflow/models/research/_ run: `python object_detection/export_inference_graph.py --input_type=image_tensor --pipeline_config_path=/home/saeed/Desktop/github/construction_practice_detection/models/research/object_detection/data/configs/{config file} --trained_checkpoint_prefix=/home/saeed/Desktop/github/construction_practice_detection/models/research/object_detection/data/checkpoints/model.ckpt-9804 --output_directory=/home/saeed/Desktop/github/construction_practice_detection/models/research/object_detection/data/frozen_graph`

### To run the inference:

* From _tensorflow/models/research/_

python object_detection/inference.py --input_dir /home/saeed/Desktop/github/construction_practice_detection/models/research/object_detection/data/inference/test --frozen_graph /home/saeed/Desktop/github/construction_practice_detection/models/research/object_detection/data/frozen_graph/frozen_inference_graph.pb --label_map /home/saeed/Desktop/github/construction_practice_detection/models/research/object_detection/data/label_maps/practice_detection_label_map.pbtxt --output_dir /home/saeed/Desktop/github/construction_practice_detection/models/research/object_detection/data/inference/result --num_output_classes 1



### General notes:
* cuda version:

nvcc --version

* tensorflow version

python -c 'import tensorflow as tf; print(tf.__version__)'

watch -n 0.5 nvidia-smi

---

## ToDo:
There is a problem with the Billur annotations. Xmax is not bigger than Xmin. Double check and create a new annotations. Check the Json to csv code first.
