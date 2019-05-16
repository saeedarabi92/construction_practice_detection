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

### To create tf.record files:
* From tensorflow/models/research/
python object_detection/dataset_tools/create_pet_tf_record.py \
    --label_map_path=object_detection/data/pet_label_map.pbtxt \
    --data_dir=`pwd` \
    --output_dir=`pwd`
    
### To run the training:
* From tensorflow/models/research/
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
1. Add scripts to README.md
