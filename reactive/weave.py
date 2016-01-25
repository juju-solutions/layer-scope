from charmhelpers.core import hookenv
from charmhelpers.core import unitdata
from charmhelpers.core.templating import render

from charms import reactive
from charms.docker.compose import Compose
from charms.reactive import hook
from charms.reactive import when
from charms.reactive import when_not

db = unitdata.kv()
config = hookenv.config()


@hook('upgrade-charm')
def upgrade_charm():
    hookenv.status_set('maintenance', 'Stopping and upgrading weave scope')
    stop_scope()
    install_scope()


@when('docker.available')
def install_scope():
    render('docker-compose.yml', 'files/scope/docker-compose.yml', config)
    reactive.set_state('scope.available')


@when('scope.available')
@when_not('scope.started')
def run_scope():
    compose = Compose('files/scope')
    compose.up()
    hookenv.open_port(4040)
    hookenv.status_set('active', 'Weave Started. Visit me on port 4040')
    reactive.set_state('scope.started')


@when('scope.started', 'website.available')
def configure_website_port(http):
    '''
    Relationship context, used in tandem with the http relation stub to provide
    an ip address (default to private-address) and set the port for the
    relationship data
    '''
    serve_port = 4040
    http.configure(port=serve_port)
    hookenv.status_set('active', 'related to load balancer/reverse proxy')
    hookenv.status_set('active', '')


def stop_scope():
    compose = Compose('files/scope')
    compose.kill()
    compose.rm()
    hookenv.close_port(4040)
    reactive.remove_state('scope.started')
    hookenv.status_set('maintenance', 'Weave stopped.')
