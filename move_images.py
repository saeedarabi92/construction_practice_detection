import argparse
import csv
import os
from shutil import copyfile
def copy_images_from_folder1_to_folder2_with_similar_name(folder_1, folder_2):
   for dirpath_1,_,filenames_! in os.walk(folder_1):
       for f_1 in filenames_1:
           abspath_1 = os.path.abspath(os.path.join(dirpath_1, f_1))
           if f_1 != ".DS_Store":
               for dirpath_2,_,filenames_2 in os.walk(folder_2):
                   for f_2 in filenames_2:
                       if f_1.split('.')[0] == f_2.split('.')[0]:
                           abspath_2 = os.path.abspath(os.path.join(dirpath_2, f_1))
                           copyfile(abspath_1, abspath_2)

if __name__ == '__main__':
    # Package directory:
    Package_dir = os.path.dirname(os.path.realpath(__file__))

    # argument parser:
    parser = argparse.ArgumentParser(description='copy the files from folder1 with the same name of the files in the folder2, into folder2.')
    parser.add_argument('--folder1', help='folder2 name',required=True)
    parser.add_argument('--folder2',help='folder1 name', required=True)
    args = parser.parse_args()

    folder1 = Package_dir + args.folder1
    folder2 = Package_dir + args.folder2

    copy_images_from_folder1_to_folder2_with_similar_name(directory_1, directory_2)
