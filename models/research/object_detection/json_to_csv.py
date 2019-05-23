import os
import glob
import pandas as pd
import csv
import json
from ast import literal_eval



def json_to_csv(path):
    json_list = []
    for json_file in glob.glob(path + '/*.json'):
        print('json file: ', json_file)
        json_object = json.load(open(json_file))
        for i in range(len(json_object["shapes"])):
            value = (json_object['imagePath'],
                    json_object['imageHeight'],
                    json_object['imageWidth'],
                    json_object['shapes'][i]['label'],
                    json_object['shapes'][i]['points'][0][0],
                    json_object['shapes'][i]['points'][0][1],
                    json_object['shapes'][i]['points'][1][0],
                    json_object['shapes'][i]['points'][1][1])
            json_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    json_df = pd.DataFrame(json_list, columns=column_name)
    print('labels added to csv')
    return json_df

def main():
    for folder in ['eval, train']:
        image_path = os.path.join(os.getcwd(), ('models/research/object_detection/images/' + folder))
        print('image_path: ', image_path)
        json_df = json_to_csv(image_path)
        json_df.to_csv(('models/research/object_detection/images/' + folder + '_labels.csv'), index=None)
    print('Successfully converted json to csv.')


if __name__ == "__main__":
    main()
