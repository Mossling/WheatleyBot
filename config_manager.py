import json

#We should add persistance for the bots config.

#Right now the bots config is universal. We could make multiple bot configs per server.

default_config_file = "default.cfg"

#Global config dict
config = {}
config["min_vote_delay"] = 5
config["max_vote_delay"] = 300
config["vote_delay"] = 10
config["prefix"] = "!"

def save_config(config_file=default_config_file):

    #Open config file
    with open(config_file, "w") as f:
        json.dump(config, f)

	#Default config file could be default.cfg.
	#We could also have default config files for servers based on the servers name.
	#Similer to the source engine we could have config files include other config files
def load_config(config_file=default_config_file):

    #Open config file
    with open(config_file, "r") as f:
        if f==None:
            return False
        config = json.load(f)
        #TODO: add error checking for invalid or incomplete config files
        return True

def set_config_variable(key, value):
    config[key] = value
    save_config()

def get_config_variable(key):
    return config[key]
