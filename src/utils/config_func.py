import configparser
import os

def load_config():
    config = configparser.ConfigParser()

    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_path, "config.ini")

    config.read(config_path, encoding="utf-8")
    return config
