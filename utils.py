def key_exists(key: str, config: object):
    return key in config


def key_not_exists(key: str, config: object):
    return key not in config
