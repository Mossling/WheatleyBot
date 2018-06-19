#We should add persistance for the bots config.

#Right now the bots config is universal. We could make multiple bot configs per server.

async def save_config():
	print("TODO: save_config")
	#Default config file could be default.cfg.
	#We could also have default config files for servers based on the servers name.
	#Similer to the source engine we could have config files include other config files

	#Write to config file
	#Maybe json
async def load_config():
	print("TODO: load_config")
	#Read from config file
	#Maybe json
async def set_config_variable(var, value):
	print("TODO: set_config_variable")
