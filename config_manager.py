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

class ConfigValue:
    def __init__(self, parse_func=str, is_private=False, may_vote=True):
        self.value = None
        self.parse_func = parse_func
        self.is_private = is_private
        self.may_vote = may_vote

    def set(self, value):
        self.value = self.parse_func(value)

    def get(self):
        return self.value

    def getstr(self):
        return str(self.value)

class Config:

    dict = {}
    dict["prefix"] = ConfigValue(str, False, True)
    dict["min_vote_delay"] = ConfigValue(int, False, True)
    dict["max_vote_delay"] = ConfigValue(int, False, True)
    dict["vote_delay"] = ConfigValue(int, False, True)
    dict["token"] = ConfigValue(str, True, False) #Private and non votable

    @staticmethod
    def get_value(key):
        return Config.dict[key].get()

    @staticmethod
    def set_value(key, value):
        Config.dict[key].set(value)

def save_config(config_file=default_config_file):
    cfg_text = ""

    for key, value in Config.dict.items():
        # <key>=<value>newline
        cfg_text += key
        cfg_text += "="
        cfg_text += value.getstr()
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
                Config.set_value(key, value)
        #TODO: add error checking for invalid key value pairs and incomplete config files
        return True
