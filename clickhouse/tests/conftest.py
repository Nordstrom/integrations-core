# (C) Datadog, Inc. 2019
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from copy import deepcopy

import pytest

from datadog_checks.dev import LazyFunction, docker_run

from . import common


class InitializeDB(LazyFunction):
    def __init__(self, config):
        self.conn_info = {
            'database': config['db'],
            'host': config['server'],
            'port': config['port'],
            'user': config['username'],
            'password': config['password'],
            'connection_timeout': config['timeout'],
        }

    def __call__(self):
        pass


@pytest.fixture(scope='session')
def dd_environment():
    with docker_run(
        common.COMPOSE_FILE
    ):
        yield common.CONFIG, common.E2E_METADATA


@pytest.fixture
def instance():
    return deepcopy(common.CONFIG)
