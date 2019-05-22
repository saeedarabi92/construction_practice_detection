"""
The code will copy all the files in folder1 and its subfolder into folder2 if the name of the file in folder2 is the same as the ones in folder2.
"""
import argparse
import csv
import os
from shutil import copyfile
def copy_images_from_folder1_to_folder2_with_similar_name(folder_1, folder_2):
    for dirpath_1,_,filenames_1 in os.walk(folder_1):
       for f_1 in filenames_1:
           if f_1 != ".DS_Store":
               abspath_1 = os.path.abspath(os.path.join(dirpath_1, f_1))
               for dirpath_2,_,filenames_2 in os.walk(folder_2):
                   for f_2 in filenames_2:
                       if f_1.split('.')[0] == f_2.split('.')[0]:
                           abspath_2 = os.path.abspath(os.path.join(dirpath_2, f_1))
                           copyfile(abspath_1, abspath_2)
                           print('Image ', f_2, ' copied')

if __name__ == '__main__':
    # Package directory:
    Package_dir = os.path.dirname(os.path.realpath(__file__))

    # argument parser:
    parser = argparse.ArgumentParser(description='copy the files from folder1 with the same name of the files in the folder2, into folder2.')
    parser.add_argument('--folder1', help='folder2 name',required=True)
    parser.add_argument('--folder2',help='folder1 name', required=True)
    args = parser.parse_args()

    directory_1 = Package_dir + args.folder1
    directory_2 = Package_dir + args.folder2

    copy_images_from_folder1_to_folder2_with_similar_name(directory_1, directory_2)
