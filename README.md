# Weave Scope

**Note:** This repository hasn't been updated in a while.
It might or might not work for you. We are keeping it around for informational purposes.

For up-to-date documentation around products and projects started by Weaveworks, please refer to:

Weaveworks products: <https://weave.works/docs>

Open Source projects started at Weaveworks:

- Cortex (CNCF): <https://cortexmetrics.io/docs>
- Flagger (CNCF): <https://docs.flagger.app>
- Flux (CNCF): <https://fluxcd.io/docs>
- Grafanalib: <https://grafanalib.rtfd.org>
- Ignite: <https://ignite.rtfd.org>
- Weave GitOps: <https://docs.gitops.weave.works>
- wksctl: <https://wksctl.rtfd.org>

---

Weave Scope automatically generates a map of your containers, enabling you to
intuitively understand, monitor, and control your applications.


### Charm Layer

This is a reactive, buildable charm layer. In order to generate this charm you
must have:

- charm-tools >= 1.6.1

    charm build -o $JUJU_REPOSITORY

### Deploy the assembled charm

    juju deploy local:trusty/weave-scope

### Pin the weave-scope version

    juju set weave-scope version=0.6.0

the `version` configuration option accepts the format of the container tag
publised by the weave scope maintainers.

valid values can be found on [docker hub](https://hub.docker.com/r/weaveworks/scope/tags/)

### Place scope behind a load balancer

    juju deploy haproxy
    juju add-relation haproxy weave-scope

## Upstream Contact Info

- The [Weave Scope](http://weave.works/scope/) project site
- [Weave Works Help & Support](http://weave.works/help/index.html)


