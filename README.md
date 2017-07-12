Hubcommander on Kubernetes
==========================

A basic [Helm chart](https://github.com/kubernetes/helm/blob/master/docs/charts.md) for [Hubcommander](https://github.com/Netflix/hubcommander).

Config
------

* `slack_token`: a bot token for your Slack 
* `github_token`: a bot token with the proper [Github rights](https://github.com/Netflix/hubcommander/blob/develop/docs/installation.md#github-configuration-api-token)
* `github_orgs`: a JSON string containing your [organization information](https://github.com/Netflix/hubcommander/blob/master/github/config.py)

Recommended test deploy:

* create `organizations.yaml` with organization configuration
* create `secrets.yaml` with `slack_token` and `github_token`
* `helm install . -f secret-values.yaml -f organizations.yaml`

TODO
----

* Add some sort of authentication plugin that allows for better access control