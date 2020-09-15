from prometheus_client import start_http_server, Summary, Info, Gauge, REGISTRY, PROCESS_COLLECTOR, PLATFORM_COLLECTOR
import random
import time

import urllib.request, json
from datetime import datetime

NEAR_NODE_UPDATE_AVAILABLE = Gauge('near_exporter_update_available', 'Is there a new version of NEAR node?')
NEAR_NETWORK_BLOCK_TIMEDIFF = Gauge('near_exporter_block_timediff',
                                    'Time difference in seconds between local chain and network chain')


def getStat():
    with urllib.request.urlopen("https://rpc.betanet.near.org/status") as url:
        global_data = json.loads(url.read().decode())

    with urllib.request.urlopen("http://192.168.31.82:3030/status") as url:
        local_node_data = json.loads(url.read().decode())

    if global_data['version']['version'] != local_node_data['version']['version']:
        NEAR_NODE_UPDATE_AVAILABLE.set(1)
    else:
        NEAR_NODE_UPDATE_AVAILABLE.set(0)

    date_mask = "%Y-%m-%dT%H:%M:%S"
    tdelta = datetime.strptime(global_data['sync_info']['latest_block_time'][:19], date_mask) - datetime.strptime(
        local_node_data['sync_info']['latest_block_time'][:19], date_mask)
    NEAR_NETWORK_BLOCK_TIMEDIFF.set(tdelta.total_seconds())


if __name__ == '__main__':
    REGISTRY.unregister(PROCESS_COLLECTOR)
    REGISTRY.unregister(PLATFORM_COLLECTOR)
    REGISTRY.unregister(REGISTRY._names_to_collectors['python_gc_objects_collected_total'])

    start_http_server(8000)
    # Generate some requests.
    while True:
        getStat()
