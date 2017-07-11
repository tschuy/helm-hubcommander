Hubcommander on Kubernetes
==========================

A basic [Helm chart](https://github.com/kubernetes/helm/blob/master/docs/charts.md) for [Hubcommander](https://github.com/Netflix/hubcommander).

Config
------

* `slack_token`: a bot token for your Slack 
* `github_token`: a bot token with the proper [Github rights](https://github.com/Netflix/hubcommander/blob/develop/docs/installation.md#github-configuration-api-token)
* `github_orgs`: a JSON string containing your [organization information](https://github.com/Netflix/hubcommander/blob/master/github/config.py)

TODO
----

* make configuration less annoying / ability to use YAML instead of a JSON string
* secrets!
* Add some sort of authentication plugin that allows for better access control