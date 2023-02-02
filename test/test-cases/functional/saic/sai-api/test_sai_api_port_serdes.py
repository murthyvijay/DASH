import json
import time
from pathlib import Path
from pprint import pprint

import pytest


class TestSaiPortSerdes:

    def test_port_serdes_create(self, dpu):

        commands = [
            {
                "name": "port_serdes",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_PORT_SERDES",
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values create =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_PORT_SERDES Create error"

    def test_port_serdes_remove(self, dpu):

        commands = [
            {
                "name": "port_serdes",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_PORT_SERDES",
            },
        ]
        results = [*dpu.process_commands(commands)]
        print("\n======= SAI commands RETURN values remove =======")
        pprint(results)

        assert all(results), "SAI_OBJECT_TYPE_PORT_SERDES Remove error"