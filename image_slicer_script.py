import image_slicer
import os

def split_image_directory(directory, number_of_tiles, Package_dir):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           abspath = os.path.abspath(os.path.join(dirpath, f))
           if f != ".DS_Store":
               tiles = image_slicer.slice(abspath, number_of_tiles, save=False)
               image_slicer.save_tiles(tiles, directory=Package_dir+"/tile_images", prefix=f.split('.')[0])
           print("image ", f," processed" )

if __name__ == '__main__':
    Package_dir = os.path.dirname(os.path.realpath(__file__))
    Images_dir = Package_dir + "/images"
    # Images_dir = "/Users/saeedarabi/Box/Drone Pictures/TAMA032819"
    number_of_tiles = 12
    split_image_directory(Images_dir,number_of_tiles, Package_dir)
