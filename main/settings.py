import os

# TODO: Get path to "data","downloads" folder


def get_data_path():
    # Construct the path to the "data" folder
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
    # Create the folder if it does not exist
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def get_downloads_path():
    # Construct the path to the "downloads" folder
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "downloads"))
    # Create the folder if it does not exist
    if not os.path.exists(path):
        os.makedirs(path)
    return path
