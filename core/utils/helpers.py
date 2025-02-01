import os
import logging
import yaml

def load_yml(file_path, prefix = None):
    """
    This funtion is to load any yaml file into a dictionary object

    :param file_path: path of the file to be loaded as a dictionary
    :param prefix: prefix to the file path

    :returns dict_out: dictionary from the yaml files
    """
    # add prefix to the path if required
    if prefix != None:
        file_path = os.path.join(prefix, file_path)
    # loading the file
    try:
        with open(file_path, 'r') as file:
            dict_out = yaml.safe_load(file)
        return dict_out
    except Exception as e:
        logging.error(e)


def print_report(l: str, v = None, format = "B", end = "\n"):
    """
    l: label,
    v: value,
    type: ("B", "U")
        for bold or underline
    """
    prefix = "\033[1m"
    suffix = "\033[0m"
    if(format == "U"):
        prefix = "\033[4m"
    
    if(v == None):
        print(f"{prefix}{l}{suffix}", end = end)
    else:
        print(f"{prefix}{l}{suffix}: {v}", end = end)
        