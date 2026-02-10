import json
from contextlib import suppress

config = {
    "llm": { #This configure which llm to use
        "base_url":"http://localhost:1234/v1",
        "api_key": "dummy",
        "model": "Llama-3.3-70B-Instruct"
    },
    "remote_backend": { #this describes who is serving direct request to enable uploading there
        "url": "http://localhost:5000/",
        "secret": "wouldn't you like to know?",
    },
    "me_as_backend": { #configure flask api access
        "secret": "wouldn't you like to know?",
        "maxstore": 100, # how many you want to store at most
        "max_reuse": 5 # how many times you want to reuse one at most
    }
}


def load_config(path_to_config:str ="config.json"):
    #only overrides the sections that are defined.
    #leaves the sections undefined as default
    with suppress(FileNotFoundError):
        with open(path_to_config, 'r') as file:
            config_in_file = json.load(file)
            for key in config_in_file:
                config[key] = config_in_file[key]


load_config()

if __name__ == "__main__":
    print(config)


