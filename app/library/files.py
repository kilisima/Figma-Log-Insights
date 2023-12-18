import glob

def get_database_list():
    database_dir = "database/*"
    return glob.glob(database_dir)