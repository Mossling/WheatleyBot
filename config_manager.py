import json

#We should add persistance for the bots config.

#Right now the bots config is universal. We could make multiple bot configs per server.

default_config_file = "default.cfg"
value_parser = {}
value_parser["prefix"] = str
value_parser["min_vote_delay"] = int
value_parser["max_vote_delay"] = int
value_parser["vote_delay"] = int
value_parser["token"] = str
#Global config dict
config = {}

def save_config(config_file=default_config_file):
    cfg_text = ""

    for key, value in config.items():
        # <key>=<value>newline
        cfg_text += key
        cfg_text += "="
        cfg_text += value
        cfg_text += "\n"
    #Open config file
    with open(config_file, "w") as f:
        f.write(cfg_text)

	#Default config file could be default.cfg.
	#We could also have default config files for servers based on the servers name.
	#Similer to the source engine we could have config files include other config files
def load_config(config_file=default_config_file):

    #Open config file
    with open(config_file, "r") as f:
        if f==None:
            return False
        for line in f:
            #Ignore comments
            if line[0] != "#":
                line = line[:-1]
                key, value = line.split("=")
                value = value_parser[key](value)
                set_config_variable(key, value)
        #TODO: add error checking for invalid key value pairs and incomplete config files
        print(json.dumps(config))
        return True

def set_config_variable(key, value):
    config[key] = value

def get_config_variable(key):
    return config[key]
