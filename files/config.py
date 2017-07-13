from hubcommander.auth_plugins.enabled_plugins import AUTH_PLUGINS
import json
import os
import importlib
import requests

# Define the organizations that this Bot will examine.
ORGS = json.loads(os.environ["HUBCOMMANDER_ORGS"])
# github API Version
GITHUB_VERSION = "application/vnd.github.v3+json"
# GITHUB API PATH:
GITHUB_URL = "https://api.github.com/"

modules = {}
def load_auth_plugin(module_name, class_name):
    if modules.get(module_name, None):
        return modules[module_name]
    modules[module_name] = getattr(importlib.import_module(module_name), class_name)()

USER_COMMAND_DICT = os.environ.get("HUBCOMMANDER_USER_COMMANDS", None)
# for whatever reason, slapping a json.loads() around os.environ.get("NAME", "{}") breaks
if USER_COMMAND_DICT:
    USER_COMMAND_DICT = json.loads(USER_COMMAND_DICT)
    for k, v in USER_COMMAND_DICT.items():
        if v.get("auth", None):
           USER_COMMAND_DICT[k]["auth"]["plugin"] = AUTH_PLUGINS[v["auth"]["plugin"]]
           if not v["auth"].get("kwargs", None):
               v["auth"]["kwargs"] = {}
else:
    USER_COMMAND_DICT = {}
