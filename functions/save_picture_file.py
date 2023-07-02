import requests
import os
import shutil
import logging
from functions.utils import path_to_save_files 


def create_images_directory(output_path: str) -> None:
    """
    The function creates a directory named "images" at the specified output path.
    
    :param output_path: The `output_path` parameter is a string that represents the path where the
    directory should be created
    :type output_path: str
    """
    directory_name = "images"
    path = os.path.join(output_path, directory_name)

    try:
        os.mkdir(path)
    except FileExistsError:
        logging.warning("The directory already exists")
    except Exception as e:
        logging.error("Error while directory was been created %s", str(e))

def save_picture(image_uri: str, filename: str) -> None:
    """
    The `save_picture` function downloads an image from a given URI and saves it to a specified file
    path.
    
    :param image_uri: The `image_uri` parameter is a string that represents the URI (Uniform Resource
    Identifier) of the image you want to save. It could be a URL pointing to an image file on the
    internet or a local file path on your computer
    :type image_uri: str
    :param filename: The `filename` parameter is a string that represents the name of the file to be
    saved. It is used to specify the name of the file when saving the image
    :type filename: str
    """

    #Finals
    export_path = path_to_save_files()
    img_directory = os.path.join(export_path, 'images')

    #Process
    create_images_directory(export_path) 
    if image_uri != "N/A":
        img_data = requests.get(image_uri).content
        file_path = os.path.join(img_directory, filename)
        with open(file_path, 'wb') as handler:
            handler.write(img_data)

def export_to_zip() -> None:
    """
    The function `export_to_zip` creates a zip file containing all the files in an images directory.
    """
    img_directory = path_to_save_files()
    filename = os.path.join(img_directory, "images")
    shutil.make_archive(filename, 'zip', filename)

