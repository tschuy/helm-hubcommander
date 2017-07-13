"""
.. module: hubcommander.auth_plugins.rollcontrol.plugin
"""
import json
import yaml
import collections
import requests

from hubcommander.bot_components.bot_classes import BotAuthPlugin
from hubcommander.bot_components.slack_comm import send_info, send_error, send_success

test_config = """
teams:
    mvp-platform:
        - brian.harrington@coreos.com
        - evan.tschuy@coreos.com
        - another-team:
            - tschuye@oregonstate.edu
            - kristy.querna@coreos.com
        - coreos-part-time:
            - kristy.querna@coreos.com
            - alex.crawford@coreos.com
        - rkt-developers:
            - luca.bruno@coreos.com
    coreos-inc:
        - evan.tschuy@coreos.com
"""

class RollPlugin(BotAuthPlugin):
    def __init__(self):
        print("Initializing RollControl plugin", flush=True)
        super().__init__()

        # a mapping of command names to the function we use to parse their permissions
        self.command_mapping = {
            '!AddUserToTeam': self.add_user_to_team
        }

    def setup(*args, **kwargs):
        return
      

    def add_user_to_team(self, permissions, data):
        # right now, we assume the data is stored as "teams" -> org -> emails & teams
        # "!AddUserToTeam <UserGitHubId> <Org> <Team> <Role>"
        Command = collections.namedtuple("command", ['command', 'userid', 'org', 'team', 'role'])
        command = Command(*data["text"].split(" "))
        emails = []

        # load the org permissions
        for perm in permissions['teams'].get(command.org, []):
            # add all org-level email strings to the valid list
            if type(perm) is str:
                emails.append(perm)
            else:
                # if perm is the team-level permissions for the team we're adding to,
                # # add its email list to the org list
                emails = emails + perm.get(command.team, [])
        return emails

    # returns a list of users that have the right to run a given command
    def valid_users(self, data):
        try:
            permissions = yaml.load(test_config)
        except: # this should go to an error channel
            send_error(data["channel"], "😞 I couldn't load the ⚙️ configuration file 💾")
            return []
        command_name = data["text"].split(" ")[0]
        return self.command_mapping[command_name](permissions, data)


    def authenticate(self, data, user_data, **kwargs):
        try:
            valid = user_data["profile"]["email"] in self.valid_users(data)
        except Exception as e:
            send_error(data["channel"], str(e))
        if not valid:
            send_error(data["channel"], ":frowning: it looks like you don't have permission to do that.")
        return valid