def get_config():
    file = 'config.ini'
    config = {}
    with open(file, "r") as file:
        for line in file:
            if "=" in line:
                key, value = line.split("=")
                config[key.strip()] = value.strip()
    return config

def get_allowed_vars():
    allowed_vars = {"P"}

    for var in get_config()['ALLOWED_VARS']:
        if var not in allowed_vars:
            allowed_vars.add(var)

    return allowed_vars