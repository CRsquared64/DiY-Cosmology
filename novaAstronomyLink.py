import json
import requests

config_file = 'config/userdata.json'  # usermade confi


class NovaAstronomyLink:
    def __init__(self, config, img):
        self.config = config
        self.img = img

    def load_config(self):
        with open(self.config) as f:
            key = json.load(f)
            key = key["api key:"]
            print(f"Nova Astronomy API key found! {key}")

    def __call__(self, *args, **kwargs):
        self.load_config()



#novaAstronomy = NovaAstronomyLink(config_file)
#novaAstronomy()