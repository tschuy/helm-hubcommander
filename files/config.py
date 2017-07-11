from hubcommander.auth_plugins.enabled_plugins import AUTH_PLUGINS
import json
import os
# Define the organizations that this Bot will examine.
print(os.environ["HUBCOMMANDER_ORGS"])
ORGS = json.loads(os.environ["HUBCOMMANDER_ORGS"])
# github API Version
GITHUB_VERSION = "application/vnd.github.v3+json"   # Is this still needed?
# GITHUB API PATH:
GITHUB_URL = "https://api.github.com/"
# You can use this to add/replace fields from the command_plugins dictionary:
USER_COMMAND_DICT = os.environ.get("HUBCOMMANDER_USER_COMMANDS", None)
# for whatever reason, slapping a json.loads() around os.environ.get("NAME", "{}") breaks
if USER_COMMAND_DICT:
    USER_COMMAND_DICT = json.loads(USER_COMMAND_DICT)
else:
    USER_COMMAND_DICT = {}