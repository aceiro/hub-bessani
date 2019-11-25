import json
import uuid

class ConfigParser:
    _config = {
        "uuid": uuid.uuid1(), 
        "file": "./config.json"
    }

    def __init__(self):
        pass

    def parser(self):
        with open(self._config['file'], 'r') as f:
            config_data = f.read()
        return json.loads(config_data)
