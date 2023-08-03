import json


def create_message(command, info):
    return json.dumps({
        "command": command,
        "info": info
    })