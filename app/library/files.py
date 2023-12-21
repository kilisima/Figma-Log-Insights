import glob
import os

def get_database_list():
    database_dir = "database/*"
    return glob.glob(database_dir)


def remove_database_file(file_path):
    os.remove(file_path)