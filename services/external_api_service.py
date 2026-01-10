import json
from datetime import datetime
import os
import threading
import requests

from utils import safe_get_request
from constants import DATA_PATH, DEFAULT_DATA_LOADING

class ExternalDataLoader:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, data_path=DATA_PATH, default_url=DEFAULT_DATA_LOADING, timeout=10):
        if hasattr(self, "session"):
            return  
        
        self.data_path = data_path
        self.default_url = default_url
        self.timeout = timeout

        self.session = requests.Session()

    def convert_to_json(self, data, content_type):
        if content_type == 'json':
            return True, data
        return False, None

    def save_as_json(self, data):
        file_name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S.json')
        path = os.path.join(self.data_path, file_name)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return path

    def load(self, url=None, params=None):
        if not url:
            url = self.default_url

        res = safe_get_request(session=self.session, url=url, params=params, timeout=self.timeout)

        if not res.get('ok'):
            raise RuntimeError(res.get("error"))

        success, json_data = self.convert_to_json(res.get('data'), res.get('format'))
        if not success:
            raise TypeError('Data is not in a format suitable for conversion to JSON.')

        try:
            path = self.save_as_json(json_data)
        except Exception:
            raise RuntimeError('Failed to save JSON file.')

        return path

  
def get_loader():
    return ExternalDataLoader()