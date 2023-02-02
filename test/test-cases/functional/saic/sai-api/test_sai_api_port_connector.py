import json
import time
from pathlib import Path
from pprint import pprint

import pytest


class TestSaiPortConnector:

    def test_port_connector_create(self, dpu):

        commands = [
            {
                "name": "port_connector",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_PORT_CONNECTOR",
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values create =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_PORT_CONNECTOR Create error"

    def test_port_connector_remove(self, dpu):

        commands = [
            {
                "name": "port_connector",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_PORT_CONNECTOR",
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values remove =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_PORT_CONNECTOR Remove error"