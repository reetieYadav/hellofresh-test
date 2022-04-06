import json
import os


def from_env():
    return json.loads(os.environ.get("CONFIG"))


def from_file():
    try:

        root = os.path.dirname(os.path.abspath(__file__))
        loaded_config = json.load(open(f'{root}/config.json', 'r'))
        return loaded_config
    except FileNotFoundError:
        raise


try:
    config = from_env()
except TypeError:
    config = from_file()
