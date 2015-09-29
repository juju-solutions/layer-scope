# Weave Scope

Weave Scope automatically generates a map of your containers, enabling you to
intuitively understand, monitor, and control your applications.


### Charm Layer

This is a reactive, composable charm layer. In order to generate this charm you
must have:

- charm-tools >= 1.6.1

    charm refresh -o /path/to/juju_repository

### Deploy the refreshed charm

    juju deploy local:trusty/weave-scope

### Place scope behind a load balancer

    juju deploy haproxy
    juju add-relation haproxy weave-scope

## Upstream Contact Info

- The [Weave Scope](http://weave.works/scope/) project site
- [Weave Works Help & Support](http://weave.works/help/index.html)


